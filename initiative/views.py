from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.shortcuts import render, redirect

from .models import Initiative, Effet


def index(request):
    return render(request, 'index.html', context={
        'initiative_list': Initiative.objects.all(),
        'effet_list': Effet.objects.all(),
        })


def round(request):
    Effet.round()
    return redirect('index')


class InitiativeMixin(object):
    model = Initiative
    fields = ('slug', 'initiative')
    success_url = reverse_lazy('index')


class InitiativeListView(InitiativeMixin, ListView): pass


class InitiativeCreateView(InitiativeMixin, CreateView): pass


class InitiativeUpdateView(InitiativeMixin, UpdateView): pass


class InitiativeDeleteView(InitiativeMixin, DeleteView): pass


class EffetMixin(object):
    model = Effet
    fields = ('slug', 'temps_restant')
    success_url = reverse_lazy('index')


class EffetListView(EffetMixin, ListView): pass


class EffetCreateView(EffetMixin, CreateView): pass


class EffetUpdateView(EffetMixin, UpdateView): pass


class EffetDeleteView(EffetMixin, DeleteView): pass
