from rest_framework import serializers

from ragas.models import Raga, Chord

class RagaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Raga
        fields = ('id', 'format_name', 'name', 'melakarta', 'arohanam', 'avarohanam')

class ChordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chord
        fields = ('id', 'name', 'description', 'formula', 'affix')
