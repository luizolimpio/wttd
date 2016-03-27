from django.test import TestCase
from django.shortcuts import resolve_url as r
from eventex.core.models import Speaker

class SpearkerDetailGet(TestCase):
    def setUp(self):
        Speaker.objects.create( name='Grace Hopper',
                                slug='grace-hopper',
                                website='http://hbn.link/hopper-site',
                                photo='http://hbn.link/hopper-pic',
                                description='Programadora e almirante.',
                               )
        self.response = self.client.get(r('speakers_detail',slug='grace-hopper'))

    def test_get(self):
        """Get should return status 200"""
        self.assertEqual(self.response.status_code,200)

    def test_template(self):
        self.assertTemplateUsed(self.response,'core/speaker_detail.html')

    def test_html(self):
        contents = ['Grace Hopper',
                   'Programadora e almirante.',
                   'http://hbn.link/hopper-pic',
                   'http://hbn.link/hopper-site',
                   ]

        for expected in contents:
            with self.subTest():
                self.assertContains(self.response,expected)

    def test_context(self):
        speaker = self.response.context['speaker']
        self.assertIsInstance(speaker,Speaker)

class SpeakerDetailNotFound(TestCase):

    def test_not_found(self):
        response = self.client.get(r('speakers_detail',slug='not-found'))
        self.assertEqual(response.status_code,404)






