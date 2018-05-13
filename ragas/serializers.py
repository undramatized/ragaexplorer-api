from rest_framework import serializers

from ragas.models import Raga

class RagaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Raga
        fields = ('id', 'name', 'melakarta', 'arohanam', 'avarohanam')
