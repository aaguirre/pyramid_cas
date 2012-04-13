::pyramid_cas README

Introduction
------------

pyramid_cas allows your application to authenticate againts a Jasig CAS server. 

It takes borrowed concepts from different packages like django.cas, anz.client, and collective.cas. 


Instructions
-------------
Include pyramid_cas under pyramid.includes directive in your .ini file like this.

pyramid.includes=
    pyramid_cas

Set the cas server directive

pyramid_cas.cas_server = ''

Optional:

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
- Solve callback error
