from django.test import TestCase
from django.shortcuts import resolve_url as r
from eventex.core.models import Talk, Speaker, Course


class TalkListGet(TestCase):
    def setUp(self):
        t1 = Talk.objects.create(title='Titulo da Palestra',start='10:00',description='Descrição da palestra.')
        t2 = Talk.objects.create(title='Titulo da Palestra',start='13:00',description='Descrição da palestra.')
        course = Course.objects.create(title='Titulo do Curso', start='09:00', description='Descricao do Curso',slots=20)
        speaker = course.speakers.create(
            name='Henrique Bastos',
            slug='henrique-bastos',
            photo='henrique-bastos'
        )



        t1.speakers.add(speaker)
        t2.speakers.add(speaker)

        self.resp = self.client.get(r('talk_list'))

    def test_get(self):
        self.assertEqual(self.resp.status_code,200)

    def test_template(self):
        self.assertTemplateUsed(self.resp,'core/talk_list.html')

    def test_html(self):
        contents = [
            (2,'Titulo da Palestra'),
            (1,'10:00'),
            (1,'13:00'),
            (3,'/palestrantes/henrique-bastos/'),
            (3,'Henrique Bastos'),
            (2,'Descrição da palestra.'),
            (1,'Titulo do Curso'),
            (1,'09:00'),
            (1,'Descricao do Curso')
            ]
        for count, expected in contents:
            with self.subTest():
                self.assertContains(self.resp,expected,count)

    def test_context(self):
        variables = ['morning_talks','afternoon_talks','courses']

        for key in variables:
            with self.subTest():
                self.assertIn(key,self.resp.context)

class TalkListGetEmpty(TestCase):
    def test_get_empty(self):
        response = self.client.get(r('talk_list'))
        self.assertContains(response,'Ainda não existem palestras de manhã.')
        self.assertContains(response,'Ainda não existem palestras de tarde.')




