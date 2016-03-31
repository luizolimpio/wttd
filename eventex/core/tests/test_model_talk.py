from django.test import TestCase
from eventex.core.models import Talk

class TalkeModelTest(TestCase):
    def setUp(self):
        self.talke = Talk.objects.create(
            title='Título da Palestra',
        )
    def test_create(self):
        self.assertTrue(Talk.objects.exists())

    def test_has_speakers(self):
        """Talk han many Speakers and vice-versa"""
        self.talke.speakers.create(
            name='Henrique Bastos',
            slug='henrique-bastos',
            website='http://henriquebastos.net'
        )
        self.assertEqual(1,self.talke.speakers.count())

    def test_description_blank(self):
        field = Talk._meta.get_field('description')
        self.assertTrue(field.blank)

    def test_speakers_black(self):
        field = Talk._meta.get_field('speakers')
        self.assertTrue(field.blank)

    def test_start_black(self):
        field = Talk._meta.get_field('start')
        self.assertTrue(field.blank)

    def test_start_null(self):
        field = Talk._meta.get_field('start')
        self.assertTrue(field.null)

    def test_str(self):
        self.assertEqual('Título da Palestra',str(self.talke))


