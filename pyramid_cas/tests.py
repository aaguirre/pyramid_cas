import unittest

from pyramid import testing

class ViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_first_call_cas_login(self):
        from pyramid_cas.views import casLogin
        request = testing.DummyRequest()
        info = casLogin(request)
        ticket = request.GET.get('ticket')
        self.assertEqual(ticket, None)


    def test_cas_logout(self):
        from pyramid_cas.views import casLogout
        request = testing.DummyRequest()
        info = casLogout(request)
        self.assertEqual(info.status , '302 Found')

