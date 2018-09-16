from django.db import models
from django.urls import reverse

from ndh.models import NamedModel


class Initiative(NamedModel):
    initiative = models.PositiveIntegerField(default=0)

    def __str__(self):
        return 'initiative: %2i pour %s' % (self.initiative, self.name)

    class Meta:
        ordering = ('-initiative', 'slug')

    def get_absolute_url(self):
        return reverse('index')


class Effet(NamedModel):
    temps_restant = models.PositiveIntegerField(default=0)

    def __str__(self):
        return '%3i rounds restant sur %s' % (self.temps_restant, self.name)

    class Meta:
        ordering = ('-temps_restant', 'slug')

    def get_absolute_url(self):
        return reverse('index')

    @staticmethod
    def round():
        Effet.objects.filter(temps_restant__gt=0).update(temps_restant=models.F('temps_restant') - 1)
