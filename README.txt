::pyramid_cas README

Introduction
------------

pyramid_cas allows your application to authenticate against a Jasig CAS server.

It takes borrowed concepts from different packages like django.cas, anz.client, and collective.cas. 

Install
-------
1. Download the package.

2. python setup.py develop


Instructions
-------------
Include pyramid_cas under pyramid.includes directive in your .ini file like this.

Required:

pyramid.includes=
    pyramid_cas

Set the cas server that will be used for authentication

pyramid_cas.cas_server = your-cas-server

Optional:

pyramid_cas.callback.get_user directive allows you to use a callback function to store a different User object after CAS authentication.

By default pyramid_cas will store (using the pyramid remember method) only the user id returned by CAS.

Example:
pyramid_cas.callback.get_user = adminsite.security.getUserObject

Use the following actions for login and logout in the application that is including pyramid_cas

/cas-login
/cas-logout

TODO:
- Implement CAS 1.0 protocol
- Add login and logout by injection and makes it configurable using tweens
- Add tests!!!!!!!!!!!
- Add demos
- Prevent adding pyramid_cas without settings
- Add came_from parameter
