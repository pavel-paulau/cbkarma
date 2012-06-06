import time
import json
from uuid import uuid4

from pyramid.view import view_config
from pyramid.response import Response

from cbkarma.data.client import CbClient

@view_config(route_name='init')
def init(request):
    response = Response(uuid4().hex)
    return response

@view_config(route_name='update')
def update(request):
    client = CbClient()

    id = request.POST.get('id', uuid4().hex)

    build = request.POST.get('build', '')
    spec = request.POST.get('spec', '')
    description = request.POST.get('description', '')
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    phase = request.POST.get('phase', '')
    status = request.POST.get('status', '')

    events = client.find(id).get('events', {})
    events.update({timestamp: {'phase': phase, 'status': status}})

    doc = {'build': build,
           'spec': spec,
           'description': description,
           'events': events,
           'type': 'update'}

    client.update(id, doc)

    response = Response(id)
    return response

@view_config(route_name='histo')
def histo(request):
    client = CbClient()

    id = request.POST.get('id', uuid4().hex)
    description = request.POST.get('description', uuid4().hex)
    attachment = request.POST.get('attachment', '')
    attachment = json.loads(str(attachment))

    histograms = client.find(id).get('histograms', {})
    histograms.update({description: attachment})

    doc = {'histograms': histograms}

    client.update(id, doc)

    response = Response(id)
    return response