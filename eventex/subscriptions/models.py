from django.db import models


class Subscription(models.Model):
    name = models.CharField('Nome',max_length=100)
    cpf = models.CharField('Cpf',max_length=11)
    email = models.EmailField('e-mail')
    phone = models.CharField('Telefone',max_length=20)
    created_at = models.DateTimeField('Criado em',auto_now=20)

    class Meta:
        verbose_name_plural = 'inscrições'
        verbose_name = 'inscrição'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name






