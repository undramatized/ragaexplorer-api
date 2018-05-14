from ragas.models import Raga
from rest_framework import generics
from rest_framework.response import Response


from ragas.serializers import RagaSerializer


class RagaList(generics.ListAPIView):
    queryset = Raga.objects.all()
    serializer_class = RagaSerializer
    def get_queryset(self):
        namestring = self.request.GET.get('name', None)
        if(namestring or namestring == ''):
            return Raga.objects.filter(name__istartswith = namestring)
        else:
            return Raga.objects.all()




class RagaDetail(generics.RetrieveAPIView):
    serializer_class = RagaSerializer

    def get_queryset(self):
        return Raga.objects.filter(pk=self.kwargs['pk'])
