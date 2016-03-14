from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):

    def test_form_has_filds(self):
        form = SubscriptionForm()
        expected = ['name','cpf','email','phone']
        self.assertSequenceEqual(expected, list(form.fields))

    def test_cpf_is_digit(self):
        """CPF must only accept digits."""
        form = self.make_validated_form(cpf='asdda123')
        self.assertFormErrorCode(form,'cpf','digits')

    def test_cpf_has_11_digits(self):
        """CPF must have 11 digits"""
        form = self.make_validated_form(cpf='1234')
        self.assertFormErrorCode(form,'cpf','length')

    def test_name_must_be_capitalized(self):
        form = self.make_validated_form(name='HENRIQUE bastos')
        self.assertEqual('Henrique Bastos',form.cleaned_data['name'])

    def test_email_is_optional(self):
        """Email is optional"""
        form = self.make_validated_form(email='')
        self.assertFalse(form.errors)

    def test_phone_is_optional(self):
        """phone is opitional"""
        form = self.make_validated_form(phone='')
        self.assertFalse(form.errors)

    def test_must_inform_email_or_phone(self):
        """Email or phone are optional, but on must te informed"""
        form = self.make_validated_form(email='',phone='')
        self.assertListEqual(['__all__'],list(form.errors))

    def assertFormErrorCode(self,form,fild,code):
        form = form
        form.is_valid()
        error = form.errors.as_data()
        error_list = error[fild]
        exception = error_list[0]
        self.assertEqual(code,exception.code)

    def make_validated_form(self, **kwargs):
        valid = dict(name='Luiz Olimpio',cpf='12345678901',email='luiz-olimpio@hotmail.com',phone='35411611')
        data = dict(valid,**kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form




