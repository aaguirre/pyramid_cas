import logging
from urllib import urlencode, urlopen
from urlparse import urljoin
from xml.etree import ElementTree

from pyramid.httpexceptions import HTTPFound

logger = logging.getLogger(__name__)


class CASProvider(object):
    """
    Provides Jasig CAS authentication mechanism for pyramid
    """

    def getserviceurl(self, request):
        """
        Returns current application's url
        """
        if 'HTTP_X_FORWARDED_HOST' in request.headers:
            # TODO get the http from the request
            applicationurl = 'http://' + request['HTTP_X_FORWARDED_HOST']
        else:
            applicationurl = request.host_url + request.path
        return applicationurl

    def getloginurl(self, request, service):
        """
        Generates login url
        """
        params = {'service': service}
        config = request.registry.settings
        cas_server = config.get('pyramid_cas.cas_server')
        return urljoin(cas_server, 'login') + '?' + urlencode(params)

    def verifycas20(self, request, ticket, service):
        """Verifies CAS 2.0+ XML-based authentication ticket.
        Returns username on success and None on failure.
        """
        params = {'ticket': ticket, 'service': service}
        config = request.registry.settings
        cas_server = config.get('pyramid_cas.cas_server')
        url = (urljoin(cas_server, 'serviceValidate') + '?' + urlencode(params))
        page = urlopen(url)
        try:
            response = page.read()
            tree = ElementTree.fromstring(response)
            if tree[0].tag.endswith('authenticationSuccess'):
                return tree[0][0].text
            else:
                return None
        finally:
            page.close()

    def getlogouturl(self, request):
        """Generates CAS logout URL"""
        config = request.registry.settings
        cas_server = config.get('pyramid_cas.cas_server')
        url = urljoin(cas_server, 'logout?service=%s'.format(self.getserviceurl(request)))
        return url

    def sendtoservice(self, request):
        return HTTPFound(location=self.getloginurl(request, self.getserviceurl(request)))
