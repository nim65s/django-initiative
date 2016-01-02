from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from .models import Initiative


class InitiativeMixin(object):
    model = Initiative
    fields = ('slug', 'initiative')
    success_url = reverse_lazy('initiative_list')


class InitiativeListView(InitiativeMixin, ListView): pass


class InitiativeCreateView(InitiativeMixin, CreateView): pass


class InitiativeUpdateView(InitiativeMixin, UpdateView): pass


class InitiativeDeleteView(InitiativeMixin, DeleteView): pass
