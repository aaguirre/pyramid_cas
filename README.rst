=======================
pyramid_cas v0.3
=======================

Introduction
============

    `pyramid_cas` allows your application to authenticate against a Jasig CAS server.
    It takes borrowed concepts from different packages like django.cas, anz.client, and collective.cas.

License
============

    `pyramid_cas` is licensed under the Apache License 2.0.

Installation
============
::

    pip install pyramid_cas

Instructions
============
    Required:

        Include pyramid_cas under pyramid.includes directive in your .ini file like this::

            pyramid.includes =
                [... other packages ...]
                pyramid_cas

        Set the cas server that will be used for authentication::

            pyramid_cas.cas_server = your-cas-server
            pyramid_cas.redirect_route    - allows you to specify what route name to redirect to after succesful authentication

    Optional::

        pyramid_cas.callback.get_user - allows you to use a callback function to store a different User object after CAS authentication.
                                        By default pyramid_cas will store (using the pyramid remember method) only the user id returned by CAS.
        
    Example::

        pyramid_cas.callback.get_user = adminsite.security.getUserObject
        pyramid_cas.redirect_route = profile  # redirects to profile page on successful authentication

    Use the following route names for login and logout in your application::

        cas-login
        cas-logout

TODO
====
    - Implement CAS 1.0 protocol
    - Add login and logout by injection and makes it configurable using tweens
    - Add tests
    - Add demos
    - Prevent adding pyramid_cas without settings
    - Add came_from parameter
