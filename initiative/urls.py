from django.conf.urls import url
from django.contrib import admin

from .views import InitiativeListView, InitiativeCreateView, InitiativeUpdateView, InitiativeDeleteView

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', InitiativeListView.as_view(), name='initiative_list'),
    url(r'^new$', InitiativeCreateView.as_view(), name='initiative_create'),
    url(r'mod/(?P<slug>[^/]+)$', InitiativeUpdateView.as_view(), name='initiative_update'),
    url(r'del/(?P<slug>[^/]+)$', InitiativeDeleteView.as_view(), name='initiative_delete'),
]
