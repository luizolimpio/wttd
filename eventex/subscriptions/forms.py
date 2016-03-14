from django import forms
from django.core.exceptions import ValidationError

def validate_cpf(value):
    if not value.isdigit():
        raise ValidationError('CPF deve conter apenas números.', 'digits')
    if len(value) != 11:
        raise ValidationError('CPF deve ter 11 números.','length')

class SubscriptionForm(forms.Form):
    name = forms.CharField(label='Nome')
    cpf = forms.CharField(label='Cpf',validators=[validate_cpf])
    email = forms.EmailField(label='Email',required=False)
    phone = forms.CharField(label='Telefone',required=False)

    def clean_name(self):
        name = self.cleaned_data['name']
        name = [n.capitalize() for n in name.split()]
        return ' '.join(name)

    def clean(self):
        if not self.cleaned_data.get('email') and not self.cleaned_data.get('phone'):
            raise ValidationError('Informe seu e-mail ou telefone.')
        return self.cleaned_data





