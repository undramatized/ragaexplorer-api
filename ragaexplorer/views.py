from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
       'ragas': reverse('ragas:raga-list', request=request, format=format),
       'chords': reverse('ragas:chord-list', request=request, format=format),
    })
