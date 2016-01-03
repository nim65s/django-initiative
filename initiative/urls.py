from django.conf.urls import url
from django.contrib import admin

from .views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', index, name='index'),
    url(r'^round$', round, name='round'),

    url(r'^initiative/list$', InitiativeListView.as_view(), name='initiative_list'),
    url(r'^initiative/new$', InitiativeCreateView.as_view(), name='initiative_create'),
    url(r'^initiative/mod/(?P<slug>[^/]+)$', InitiativeUpdateView.as_view(), name='initiative_update'),
    url(r'^initiative/del/(?P<slug>[^/]+)$', InitiativeDeleteView.as_view(), name='initiative_delete'),

    url(r'^effet/list$', EffetListView.as_view(), name='effet_list'),
    url(r'^effet/new$', EffetCreateView.as_view(), name='effet_create'),
    url(r'^effet/mod/(?P<slug>[^/]+)$', EffetUpdateView.as_view(), name='effet_update'),
    url(r'^effet/del/(?P<slug>[^/]+)$', EffetDeleteView.as_view(), name='effet_delete'),
]
