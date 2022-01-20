# python
import sys
import logging

# pyramid
from pyramid.httpexceptions import HTTPFound, HTTPForbidden
from pyramid.security import remember, forget, unauthenticated_userid
from pyramid.view import view_config


## pyramid_cs
from pyramid_cas.services import CASProvider
logger = logging.getLogger(__name__)

cas = CASProvider()


@view_config(name='cas-login', renderer='string')
def caslogin(request, return_url=None):
    """
    Cas login and user challenger view
    """
    service = cas.getserviceurl(request)
    username = unauthenticated_userid(request)
    if username is None:
        ticket = request.GET.get('ticket')
        if ticket is None:
            return cas.sendtoservice(request)
        username = cas.verifycas20(request, ticket, service)
        if username is None:
            return 'no user'

        settings = request.registry.settings
        if 'pyramid_cas.callback.get_user' in settings:
            callable = settings['pyramid_cas.callback.get_user']
            module = callable.split('.')[0] + '.' + callable.split('.')[1]
            caller = sys.modules[module]
            method = getattr(caller, callable.split('.')[2])
            user = method(username, request)
        else:
            user = username
        headers = remember(request, user, max_age='86400')

        # fall back to setting from config file if return_url isn't provided
        redirect_to = return_url or request.route_url(settings['pyramid_cas.redirect_route'])
        return HTTPFound(location=redirect_to, headers=headers)
    else:
        raise HTTPForbidden


@view_config(name='cas-logout', renderer='string')
def caslogout(request):
    """
    Cas logout page
    """
    headers = forget(request)
    request.session.clear()
    return HTTPFound(location=cas.getlogouturl(request), headers=headers)
