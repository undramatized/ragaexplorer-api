from ragas.models import Raga
from rest_framework import generics, filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from ragas.serializers import RagaSerializer

# ragas/
# ragas/?search=char => Charukeshi

class RagaList(generics.ListAPIView):
    """
    Return a list of all the existing ragas.
    """
    queryset = Raga.objects.all()
    serializer_class = RagaSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ['^name']
    # filter_fields = ['arohanam', 'avarohanam']


class RagaDetail(generics.RetrieveAPIView):
    """
    Return the raga detail.
    """
    serializer_class = RagaSerializer

    def get_queryset(self):
        return Raga.objects.filter(pk=self.kwargs['pk'])
