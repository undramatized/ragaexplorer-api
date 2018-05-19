from ragas.models import Raga
from rest_framework import generics, filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from ragas.serializers import RagaSerializer

# ragas/ => Returns all ragas
# ragas/?search=char => Returns ragas starting with search string
# ragas/?swaras=S%20R2%20G2 => Returns ragas containing those swaras

class SwaraFilterBackend(filters.BaseFilterBackend):
    """
    Filter that only allows users to see their own objects.
    """
    def filter_queryset(self, request, queryset, view):
        print "Filtering queryset based on swaras"
        swaras = request.query_params.get('swaras', None)
        if swaras:
            return Raga.objects.filter_swaras_queryset(swaras, queryset)
        else:
            return queryset

    def to_html(self, request, queryset, view):
        pass

class RagaList(generics.ListAPIView):
    """
    Return a list of all the existing ragas.
    """
    queryset = Raga.objects.all()
    serializer_class = RagaSerializer
    filter_backends = (filters.SearchFilter, SwaraFilterBackend, )
    search_fields = ['^name']
    filter_fields = ['swaras']



class RagaDetail(generics.RetrieveAPIView):
    """
    Return the raga detail.
    """
    serializer_class = RagaSerializer

    def get_queryset(self):
        return Raga.objects.filter(pk=self.kwargs['pk'])
