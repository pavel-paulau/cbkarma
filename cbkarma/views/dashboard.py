from pyramid.view import view_config

@view_config(route_name='home', renderer='/home/core.mako')
def home(request):
    return {}