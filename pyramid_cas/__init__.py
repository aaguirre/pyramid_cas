from pyramid.exceptions import ConfigurationError


def includeme(config):
    settings = config.registry.settings
    if 'pyramid_cas.cas_server' not in settings:
        raise ConfigurationError('The CAS server has not been defined')
    if 'pyramid_cas.redirect_route' not in settings:
        raise ConfigurationError('The redirect route has not been defined')
    config.scan('pyramid_cas.views')

