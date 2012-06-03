import json

from cbkarma.lib.couchbase.couchbaseclient import VBucketAwareCouchbaseClient

class CbClient:
    """Abstract couchbase client"""

    def __init__(self, host='localhost', port='8091', bucket='default',
                 password='password'):
        protocol = "http://"
        api = "/pools/default"
        uri = protocol + host + ":" + port + api

        self.client = VBucketAwareCouchbaseClient(uri, bucket, password, True)

    def insert(self, id, doc={}):
        doc = json.dumps(doc)
        return self.client.set(id, 0, 0, doc)

    def find(self, id):
        doc = self.client.get(id)
        return json.loads(doc[-1])

    def update_(self, id, doc={}):
        current = self.find(id)
        current.update(doc)
        return self.client.set(id, 0, 0, doc)