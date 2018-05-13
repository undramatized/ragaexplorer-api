from ragas.models import Raga
from rest_framework import generics
from rest_framework.response import Response


from ragas.serializers import RagaSerializer


class RagaList(generics.ListCreateAPIView):
    queryset = Raga.objects.all()
    serializer_class = RagaSerializer


class RagaDetail(generics.RetrieveAPIView):
    serializer_class = RagaSerializer

    def get_queryset(self):
        print "pk value:", self.kwargs['pk']
        return Raga.objects.filter(pk=self.kwargs['pk'])
