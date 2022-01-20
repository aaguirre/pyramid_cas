import unittest

from pyramid import testing


class ViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_first_call_cas_login(self):
        from pyramid_cas.views import caslogin
        request = testing.DummyRequest()
        info = caslogin(request)
        ticket = request.GET.get('ticket')
        self.assertEqual(ticket, None)

    def test_cas_logout(self):
        from pyramid_cas.views import caslogout
        request = testing.DummyRequest()
        info = caslogout(request)
        self.assertEqual(info.status, '302 Found')

