
sources=[{'type':'couchbase','class':'CouchbaseReader','example':'couchbase://bucket:password@example.com:8091/bucket'}]
destinations=[{'type':'couchbase','class':'CouchbaseWriter','example':'couchbase://bucket:password@example.com:8091/bucket'}]

import re
import json
import uuid
from urlparse import urlparse
import urllib

import couchbase

import migrator

class CouchbaseReader(migrator.Reader):
    def __init__(self, source):
        # couchbase://username:password@example.com:8091/bucket
        url = urlparse(source)
        self.username = url.username
        self.password = url.password
        self.host = url.hostname
        self.port = url.port
        self.bucket_name = url.path[1:]

        self.page_limit = 100

        cb = couchbase.Server(self.host + ":" + str(self.port),
                              username=self.username,
                              password=self.password)
        self.bucket = cb[self.bucket_name]

        self.items = self.bucket.view('_all_docs', limit=self.page_limit+1, stale=False, reduce=False, include_docs=True)

    def __iter__(self):
        return self

    def next(self):
        if len(self.items) < 1:
            raise StopIteration()
        elif len(self.items) == 1:
            next_startkey = urllib.quote_plus(self.items[0]['key'].replace('"','\\"').encode('utf-8'))
            next_startkey_docid = urllib.quote_plus(self.items[0]['doc']['_id'].replace('"','\\"').encode('utf-8'))
            self.items = self.bucket.view('_all_docs', limit=self.page_limit+1, startkey=next_startkey, startkey_docid=next_startkey_docid, stale=False, reduce=False, include_docs=True)
            data = self.items.pop(0)
        else:
            data = self.items.pop(0)

        record = {'id':data['doc']['_id']}
        record['value'] = dict((k,v) for (k,v) in data['doc'].iteritems() if not k.startswith('$'))
        return record


class CouchbaseWriter(migrator.Writer):
    def __init__(self, destination):
        # couchbase://username:password@example.com:8091/bucket
        url = urlparse(destination)
        self.username = url.username
        self.password = url.password
        self.host = url.hostname
        self.port = url.port
        self.bucket_name = url.path[1:]

        self.verbose = False

        cb = couchbase.Server(self.host + ":" + str(self.port),
                              username=self.username,
                              password=self.password)
        self.bucket = cb[self.bucket_name]

    def write(self, record):
        record_save = record['value']
        record_save['_id'] = record['id'].encode('utf-8')
        self.bucket.save(record_save)
