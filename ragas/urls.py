from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(r'^ragas/$', views.RagaList.as_view(), name='raga-list'),
    url(r'^ragas/(?P<pk>[0-9]+)/$', views.RagaDetail.as_view(), name='raga-detail'),
    url(r'^chords/$', views.ChordList.as_view(), name='chord-list'),
]
