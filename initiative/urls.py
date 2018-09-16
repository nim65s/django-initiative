from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.index, name='index'),
    path('round', views.round, name='round'),
    path('initiative/list', views.InitiativeListView.as_view(), name='initiative_list'),
    path('initiative/new', views.InitiativeCreateView.as_view(), name='initiative_create'),
    path('initiative/mod/<slug:slug>', views.InitiativeUpdateView.as_view(), name='initiative_update'),
    path('initiative/del/<slug:slug>', views.InitiativeDeleteView.as_view(), name='initiative_delete'),
    path('effet/list', views.EffetListView.as_view(), name='effet_list'),
    path('effet/new', views.EffetCreateView.as_view(), name='effet_create'),
    path('effet/mod/<slug:slug>', views.EffetUpdateView.as_view(), name='effet_update'),
    path('effet/del/<slug:slug>', views.EffetDeleteView.as_view(), name='effet_delete'),
]
