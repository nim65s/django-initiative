from django.core.urlresolvers import reverse
from django.db.models import Model, CharField, IntegerField


class Initiative(Model):
    slug = CharField('Nom', max_length=100, primary_key=True)
    initiative = IntegerField(default=0)

    class Meta:
        ordering = ('-initiative', 'slug')

    def get_absolute_url(self):
        return reverse('initiative_list')
