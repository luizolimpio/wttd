from django.core import mail
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm

class SubscribeGet(TestCase):
    def setUp(self):
        self.response = self.client.get('/inscricao/')


    def test_get(self):
        """Get /inscricao/must return status code 200"""
        self.assertEqual(200,self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response,'subscriptions/subscription_form.html')

    def test_html(self):
        tag = (
            ('<form',1),
            ('<input',6),
            ('type="text"',3),
            ('type="email"',1),
            ('type="submit"',1)
        )
        for texto,quantidade in tag:
            with self.subTest():
                self.assertContains(self.response, texto,quantidade )

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        form = self.response.context['form']
        self.assertIsInstance(form, SubscriptionForm)

class SubcribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Henrique Bastos',cpf='12345678901',email='henrique@bastos.net',phone='21-99618-6180')
        self.response = self.client.post('/inscricao/',data)

    def test_post(self):
        """valida redirecionamento apos o post para /inscricao/"""
        self.assertEqual(302,self.response.status_code)

    def test_send_subscribe_email(self):
        self.assertEqual(1, len(mail.outbox))

class SubscribePostInvalid(TestCase):
    def setUp(self):
        self.response = self.client.post('/inscricao/', {})

    def test_post(self):
        self.assertEqual(200, self.response.status_code)
    def test_template(self):
        self.assertTemplateUsed(self.response,'subscriptions/subscription_form.html')

    def test_has_form(self):
        form = self.response.context['form']
        self.assertIsInstance(form,SubscriptionForm)

    def test_has_form_erros(self):
        form = self.response.context['form']
        self.assertTrue(form.errors)

class SubscribeSucessMessage(TestCase):
    def test_message(self):
        data = dict(name='henriquebastos',cpf='12345678901',email='henrique@bastos.net',phone='35411611')
        response = self.client.post('/inscricao/',data, follow=True)
        self.assertContains(response,'Inscrição realizada com sucesso!')


