from uuid import uuid4

from pyramid.view import view_config
from pyramid.response import Response

@view_config(route_name='init')
def init(request):
    response = Response(uuid4().hex)
    return response