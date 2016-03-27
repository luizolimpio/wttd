from django import forms
from django.core.exceptions import ValidationError
from eventex.subscriptions.models import Subscription
from eventex.subscriptions.validater import validate_cpf

'''
class SubscriptionFormOld(forms.Form):
    name = forms.CharField(label='Nome')
    cpf = forms.CharField(label='Cpf',validators=[validate_cpf])
    email = forms.EmailField(label='Email',required=False)
    phone = forms.CharField(label='Telefone',required=False)'''


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['name','cpf','email','phone']

    def clean_name(self):
        self.cleaned_data = super().clean()
        name = self.cleaned_data['name']
        name = [n.capitalize() for n in name.split()]
        return ' '.join(name)

    def clean(self):

        if not self.cleaned_data.get('email') and not self.cleaned_data.get('phone'):
            raise ValidationError('Informe seu e-mail ou telefone.')
        return self.cleaned_data





