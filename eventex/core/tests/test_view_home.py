from django.test import TestCase
from django.shortcuts import resolve_url as r

class hometest(TestCase):
    def setUp(self):
        self.response = self.client.get(r('home'))
    def test_get(self):
        """GET/ MUST RETURN STATUS CODE 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):

        self.assertTemplateUsed(self.response,'index.html')

    def test_subscription_link(self):
        expected = 'href="{}"'.format(r('subscriptions:new'))
        self.assertContains(self.response, expected)





