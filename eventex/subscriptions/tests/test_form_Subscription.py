from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):
    def setUp(self):
        self.form = SubscriptionForm()
        self.expected = ['name','cpf','email','phone']

    def test_form_has_filds(self):
        self.assertSequenceEqual(self.expected, list(self.form.fields))
