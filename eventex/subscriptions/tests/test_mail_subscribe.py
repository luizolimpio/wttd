from django.core import mail
from django.test import TestCase


class SubcribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Henrique Bastos',cpf='12345678901',email='henrique@bastos.net',phone='21-99618-6180')
        self.client.post('/inscricao/',data)
        self.email = mail.outbox[0]


    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'
        self.assertEqual(self.email.subject,expect)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'
        self.assertEqual(self.email.from_email, expect)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br','henrique@bastos.net']
        self.assertEqual(expect,self.email.to)

    def test_subscription_email_body(self):
        data = [
            'Henrique Bastos',
            '12345678901',
            'henrique@bastos.net',
            '21-99618-6180'
        ]
        for contem in data:
            with self.subTest():
                self.assertIn(contem,self.email.body)





