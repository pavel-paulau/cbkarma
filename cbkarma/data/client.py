import json

from cbkarma.lib.couchbase.couchbaseclient import VBucketAwareCouchbaseClient
from cbkarma.lib.couchbase.rest_client import RestConnection

class CbClient:
    """Abstract couchbase client"""

    def __init__(self, host='localhost', port='8091', bucket='default',
                 username='Administrator', password='password'):
        protocol = "http://"
        api = "/pools/default"
        uri = protocol + host + ":" + port + api

        self.client = VBucketAwareCouchbaseClient(uri, bucket, password, True)

        self.bucket = bucket

        server = {
            'ip': host,
            'port': port,
            'username': username,
            'password': password,
        }
        self.rest_client = RestConnection(server)

    def insert(self, test_id, doc={}):
        doc = json.dumps(doc)
        return self.client.set(str(test_id), 0, 0, doc)

    def find(self, test_id):
        try:
            doc = self.client.get(str(test_id))
            return json.loads(doc[-1])
        except:
            return {}

    def update(self, test_id, doc={}):
        current = self.find(test_id)
        current.update(doc)
        return self.insert(test_id, current)

    def query(self, bucket='default', ddoc='', view='', params=[], limit=100):
        return self.rest_client.view_results(bucket, ddoc, view, params, limit)