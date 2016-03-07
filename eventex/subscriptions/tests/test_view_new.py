from django.shortcuts import resolve_url as r
from django.core import mail
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


class SubscriptionNewGet(TestCase):
    def setUp(self):
        self.response = self.client.get(r('subscriptions:new'))


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

class SubscriptionNewPostValid(TestCase):
    def setUp(self):
        data = dict(name='Henrique Bastos',cpf='12345678901',email='henrique@bastos.net',phone='21-99618-6180')
        self.response = self.client.post(r('subscriptions:new'),data)

    def test_post(self):
        """valida redirecionamento apos o post para /inscricao/"""
        self.assertRedirects(self.response, r('subscriptions:detail', 1))

    def test_send_subscribe_email(self):
        self.assertEqual(1, len(mail.outbox))

    def test_save_subscription(self):
        self.assertTrue(Subscription.objects.exists())

class SubscriptionNewPostInvalid(TestCase):
    def setUp(self):
        self.response = self.client.post(r('subscriptions:new'), {})

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

    def test_dont_save_subscriptions(self):
        self.assertFalse(Subscription.objects.exists())




