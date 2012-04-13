from pyramid.exceptions import ConfigurationError

def includeme(config):
    settings = config.registry.settings
    if 'pyramid_cas.cas_server' not in settings:
        raise ConfigurationError('The CAS server has not been defined')
    config.scan('pyramid_cas.views')

