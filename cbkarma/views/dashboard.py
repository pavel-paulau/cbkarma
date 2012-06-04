from pyramid.view import view_config
from cbkarma.data.client import CbClient

@view_config(route_name='home', renderer='/home/core.mako')
def home(request):
    # Couchbase client
    client = CbClient()

    # Output dictionary
    data = list()

    for row in client.query(ddoc='karma', view='uid')['rows']:
        test = client.find(str(row['id']))

        latest_timestamp = max(test['events'].keys())
        status = "{0}: {1}".format(test['events'][latest_timestamp]['phase'],
                                   test['events'][latest_timestamp]['status'])

        data.append({'test_id': row['id'],
                     'build': test['build'],
                     'spec': test['spec'],
                     'description': test['description'],
                     'status': status,
                     'timestamp': latest_timestamp
        })

    return {'data': data}