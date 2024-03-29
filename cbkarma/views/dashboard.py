from pyramid.view import view_config
from cbkarma.data.client import CbClient
from cbkarma.lib.histo import LatencyDict

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

@view_config(route_name='details', renderer='/details/core.mako')
def details(request):
    # Couchbase client
    client = CbClient()

    # Phases
    test_id = request.GET['id']

    events = client.find(test_id)['events']

    phases = []
    for event in sorted(events):
        phases.append("{0} phase {1} at {2}".format(events[event]['phase'],
                                                    events[event]['status'],
                                                    event))

    histograms = client.find(test_id).get('histograms', {})
    histograms = dict((d, LatencyDict(a)) for d, a in histograms.iteritems())

    reports = client.find(test_id).get('reports', {})

    return {'phases': phases, 'histograms': histograms, 'reports': reports,
            'build': client.find(test_id)['build'],
            'spec': client.find(test_id)['spec'],
            'test_id': test_id}