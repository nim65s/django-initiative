from django.db.models import CharField, F, IntegerField, Model
from django.urls import reverse


class Initiative(Model):
    slug = CharField('Nom', max_length=100, primary_key=True)
    initiative = IntegerField(default=0)

    def __str__(self):
        return 'initiative: %2i pour %s' % (self.initiative, self.slug)

    class Meta:
        ordering = ('-initiative', 'slug')

    def get_absolute_url(self):
        return reverse('index')


class Effet(Model):
    slug = CharField('Nom', max_length=100, primary_key=True)
    temps_restant = IntegerField(default=0)

    def __str__(self):
        return '%3i rounds restant sur %s' % (self.temps_restant, self.slug)

    class Meta:
        ordering = ('-temps_restant', 'slug')

    def get_absolute_url(self):
        return reverse('index')

    @staticmethod
    def round():
        Effet.objects.filter(temps_restant__gt=0).update(temps_restant=F('temps_restant') - 1)
