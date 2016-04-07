from django.db import models

class KindQuerySet(models.QuerySet):
    def emails(self):
        return self.filter(kind=self.model.EMAIL)

    def phones(self):
        return self.filter(kind=self.model.PHONE)

class StartQuerySet(models.Manager):

    MIDDAY = '12:00'

    def morning(self):
        return self.filter(start__lt=self.MIDDAY)

    def afternoon(self):
        return self.filter(start__gte=self.MIDDAY)

