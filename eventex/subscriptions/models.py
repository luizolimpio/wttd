from django.core.exceptions import ValidationError
from django.db import models
from eventex.subscriptions.validater import validate_cpf


class Subscription(models.Model):
    name = models.CharField('Nome',max_length=100)
    cpf = models.CharField('Cpf',max_length=11,validators=[validate_cpf])
    email = models.EmailField('e-mail',blank=True)
    phone = models.CharField('Telefone',max_length=20,blank=True)
    created_at = models.DateTimeField('Criado em',auto_now=20)
    paid = models.BooleanField('Pago',default=False)

    class Meta:
        verbose_name_plural = 'inscrições'
        verbose_name = 'inscrição'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name








