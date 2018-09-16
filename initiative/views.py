from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from ndh.mixins import NDHDeleteMixin, NDHFormMixin

from .models import Effet, Initiative


def index(request):
    return render(
        request,
        'index.html',
        context={
            'initiative_list': Initiative.objects.all(),
            'effet_list': Effet.objects.all(),
        })


def round(request):
    Effet.round()
    return redirect('index')


class InitiativeMixin(object):
    model = Initiative
    fields = ('name', 'initiative')
    success_url = reverse_lazy('index')


class InitiativeListView(InitiativeMixin, ListView):
    pass


class InitiativeCreateView(NDHFormMixin, InitiativeMixin, CreateView):
    pass


class InitiativeUpdateView(NDHFormMixin, InitiativeMixin, UpdateView):
    pass


class InitiativeDeleteView(NDHDeleteMixin, InitiativeMixin, DeleteView):
    pass


class EffetMixin(object):
    model = Effet
    fields = ('name', 'temps_restant')
    success_url = reverse_lazy('index')


class EffetListView(EffetMixin, ListView):
    pass


class EffetCreateView(NDHFormMixin, EffetMixin, CreateView):
    pass


class EffetUpdateView(NDHFormMixin, EffetMixin, UpdateView):
    pass


class EffetDeleteView(NDHDeleteMixin, EffetMixin, DeleteView):
    pass
