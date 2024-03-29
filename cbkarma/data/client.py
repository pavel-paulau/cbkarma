import json

from cbkarma.lib.couchbase.rest_client import RestConnection
import memcache

class CbClient:
    """Abstract couchbase client"""

    def __init__(self, host='localhost', port='8091', username='Administrator',
                 password='password'):
        """Initialize memcache and couchbase clients"""

        server = {'ip': host, 'port': port,
                  'username': username, 'password': password}
        self.rest_client = RestConnection(server)

        self.mc_client = memcache.Client([host + ':11211'], debug=0)

    def insert(self, test_id, doc={}):
        doc = json.dumps(doc)
        return self.mc_client.set(str(test_id), doc)

    def find(self, test_id):
        try:
            doc = self.mc_client.get(str(test_id))
            return json.loads(doc[-1])
        except:
            return {}

    def update(self, test_id, doc={}):
        current = self.find(test_id)
        current.update(doc)
        return self.insert(test_id, current)

    def query(self, bucket='default', ddoc='', view='', params=[], limit=100):
        return self.rest_client.view_results(bucket, ddoc, view, params, limit)