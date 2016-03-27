from django.test import TestCase
from django.shortcuts import resolve_url as r

class hometest(TestCase):
    fixtures=['Keynotes.json']
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

    def test_speakers(self):
        '''Must Show keynote speakers'''
        context = [
                   'href="{}"'.format(r('speakers_detail',slug='gracer-hopper')),
                   'Grace Hopper',
                   'http://hbn.link/hopper-pic',
                   'href="{}"'.format(r('speakers_detail',slug='alan-turing')),
                   'Alan Turing',
                   'http://hbn.link/turing-pic'
                   ]
        for expected in context:
            with self.subTest():
                self.assertContains(self.response,expected)

    def test_speakers_link(self):
        expected = 'href="{}#speakers"'.format(r('home'))
        self.assertContains(self.response,expected)








