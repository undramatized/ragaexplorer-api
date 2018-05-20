import json, datetime
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ragas.models import Raga
from ragas.serializers import RagaSerializer

# initialize the APIClient app
client = Client()

class GetRagasTestCase(TestCase):
    def setUp(self):
        Raga.objects.create(
            id = 1,
            created = datetime.time().strftime('%Y-%m-%d %H:%M:%S'),
            name = "dIrashankarAbharanam",
            format_name = "Shankarabharanam",
            melakarta = None,
            arohanam = "S R2 G2 M1 P D2 N2 S",
            avarohanam = "S N2 D2 P M1 G2 R2 S",
        )
        Raga.objects.create(
            id = 2,
            created = datetime.time().strftime('%Y-%m-%d %H:%M:%S'),
            name = "HarikAmbhOji",
            format_name = "Harikamboji",
            melakarta = None,
            arohanam = "S R2 G2 M1 P D2 N1 S",
            avarohanam = "S N1 D2 P M1 G2 R2 S",
        )
        Raga.objects.create(
            id = 3,
            created = datetime.time().strftime('%Y-%m-%d %H:%M:%S'),
            name = "mOhanam",
            format_name = "Mohanam",
            melakarta = Raga.objects.get(pk=2),
            arohanam = "S R2 G2 P D2 S",
            avarohanam = "S D2 P G2 R2 S",
        )
        Raga.objects.create(
            id = 4,
            created = datetime.time().strftime('%Y-%m-%d %H:%M:%S'),
            name = "vasanthA",
            format_name = "Vasantha",
            melakarta = Raga.objects.get(pk=1),
            arohanam = "S G2 M1 D2 N2 S",
            avarohanam = "S N2 D2 M1 G2 R1 S",
        )

    def test_get_all_ragas(self):
        # get API response
        response = client.get('/ragas/')
        # get data from db
        ragas = Raga.objects.all().order_by('format_name')
        serializer = RagaSerializer(ragas, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_valid_raga(self):
        # get API response
        response = client.get('/ragas/2/')

        # get data from db
        ragas = Raga.objects.get(pk=2)
        serializer = RagaSerializer(ragas)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_raga(self):
        # get API response
        response = client.get('/ragas/10/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_search_valid_raga(self):
        response = client.get('/ragas/?search=moha')
        # get data from db
        ragas = Raga.objects.filter(pk=3)
        serializer = RagaSerializer(ragas, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_search_invalid_raga(self):
        response = client.get('/ragas/?search=kam')
        self.assertEqual(response.data, [])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
