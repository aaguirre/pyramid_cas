# python
import sys
import logging

# pyramid
from pyramid.httpexceptions import HTTPFound
from pyramid.security import remember, forget,unauthenticated_userid
from pyramid.view import view_config


## pyramid_cs
from pyramid_cas.services import CASProvider
logger = logging.getLogger(__name__)

cas = CASProvider()

@view_config(name='cas-login',renderer='string')
@view_config(context='pyramid.httpexceptions.HTTPForbidden')
def casLogin(request):
    """
    Cas login and user challenger view
    """
    service = cas.getServiceUrl(request)
    username = unauthenticated_userid(request)
    if username is None:
        ticket = request.GET.get('ticket')
        if ticket is None:
            return cas.sendToService(request)
        username = cas.verifyCas20(request,ticket,service)
        if username is None:
            return 'no user'

        settings = request.registry.settings
        if 'pyramid_cas.callback.get_user' in settings:
            callable = settings['pyramid_cas.callback.get_user']
            module = callable.split('.')[0] + '.' + callable.split('.')[1]
            caller = sys.modules[module]
            method = getattr(caller,callable.split('.')[2])
            user = method(username,request)
        else:
            user = username
        headers = remember(request,user,max_age = '86400')
        return HTTPFound(location=request.route_url('home'),headers=headers)
    else:
        return HTTPFound(location='/not-allowed')


@view_config(name='cas-logout',renderer='string')
def casLogout(request):
    """
    Cas logout page
    """
    headers = forget(request)
    request.session.clear()
    return HTTPFound(location=cas.getLogoutUrl(request),headers=headers)


@view_config(name="not-allowed",renderer='string')
def notAllowed(request):
    return 'Not Allowed'
