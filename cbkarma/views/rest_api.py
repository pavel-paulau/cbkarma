import time
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

    doc = {'build': build,
           'spec': spec,
           'description': description,
           'events': {timestamp: {'phase': phase, 'status': status}},
           'type': 'update'}

    client.update_(id, doc)

    response = Response(id)
    return response