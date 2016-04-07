from django.db import models
from django.shortcuts import resolve_url as r
from eventex.core.managers import KindQuerySet, StartQuerySet


class Speaker(models.Model):

    name = models.CharField('Nome',max_length=255)
    slug = models.SlugField('Slug',unique=True)
    photo = models.URLField('Foto')
    website = models.URLField('Website',blank=True)
    description = models.TextField('Descrição',blank=True)

    class Meta:
        verbose_name = 'palestrante'
        verbose_name_plural = 'palestrantes'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return r('speakers_detail',slug=self.slug)


class Contact(models.Model):
    EMAIL = 'E'
    PHONE = 'P'
    KINDS=(
        (EMAIL,'Email'),
        (PHONE,'Tefone')
    )

    speaker = models.ForeignKey('Speaker',verbose_name='palestrante')
    kind = models.CharField('Tipo',max_length=1,choices=KINDS)
    value = models.CharField('Valor',max_length=255)

    objects = KindQuerySet().as_manager()

    class Meta:
        verbose_name = 'contato'
        verbose_name_plural = 'contatos'

    def __str__(self):
        return self.value

class Talk(models.Model):
    title = models.CharField('Titulo',max_length=200)
    start = models.TimeField('Início',blank=True,null=True)
    description = models.TextField('Descrição',blank=True)
    speakers = models.ManyToManyField('Speaker',verbose_name='palestrante',blank=True)

    objects = StartQuerySet()

    class Meta:
        verbose_name = 'palestra'
        verbose_name_plural = 'palestras'

    def __str__(self):
        return self.title












