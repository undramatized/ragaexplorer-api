# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json, datetime

from django.test import TestCase, Client
from ragas.models import Raga, Chord
# Create your tests here.

class RagaTestCase(TestCase):
    def setUp(self):
        Raga.objects.create(
            id = 1,
            created = datetime.time().strftime('%Y-%m-%d %H:%M:%S'),
            name = "dIrashankarAbharanam",
            format_name = "Shankarabharanam",
            melakarta = None,
            arohanam = "S R2 G3 M1 P D2 N3 S",
            avarohanam = "S N3 D2 P M1 G3 R2 S",
        )
        Raga.objects.create(
            id = 2,
            created = datetime.time().strftime('%Y-%m-%d %H:%M:%S'),
            name = "mOhanam",
            format_name = "Mohanam",
            melakarta = None,
            arohanam = "S R2 G2 P D2 S",
            avarohanam = "S D2 P G2 R2 S",
        )
        Raga.objects.create(
            id = 3,
            created = datetime.time().strftime('%Y-%m-%d %H:%M:%S'),
            name = "vasanthA",
            format_name = "Vasantha",
            melakarta = None,
            arohanam = "S G2 M1 D2 N2 S",
            avarohanam = "S N2 D2 M1 G2 R1 S",
        )
        Chord.objects.create(
            id = 1,
            name = "Major",
            formula = "1 3 5",
            affix = "maj",
            description = "Named after the major 3rd interval between root and 3"
        )
        Chord.objects.create(
            id = 2,
            name = "Minor",
            formula = "1 b3 5",
            affix = "min",
            description = "Minor is just the major with a flat 3rd"
        )

    def test_get_swaras(self):
        shankara = Raga.objects.get(id = 1)
        self.assertCountEqual(
            shankara.get_swaras(), ["S", "R2", "G3", "M1", "P", "D2", "N3"])

    def test_get_aro(self):
        shankara = Raga.objects.get(id = 1)
        self.assertEqual(
            shankara.get_aro_swaras(), ["S", "R2", "G3", "M1", "P", "D2", "N3", "S"])

    def test_get_ava(self):
        shankara = Raga.objects.get(id = 1)
        self.assertEqual(
            shankara.get_ava_swaras(), ["S", "N3", "D2", "P", "M1", "G3", "R2", "S"])

    def test_has_swaras(self):
        shankara = Raga.objects.get(id = 1)
        swaras1 = "S R2 P D2 N3"
        swaras2 = "S R2 M2 P N2"
        self.assertTrue(shankara.has_swaras(swaras1))
        self.assertFalse(shankara.has_swaras(swaras2))

    def test_get_chords(self):
        shankara = Raga.objects.get(id = 1)
        root = 'C'
        chords_res = {
            'S' : {'note': 'C', 'chord_ids': [1]},
            'R2' : {'note': 'D', 'chord_ids': [2]},
            'G3' : {'note': 'E', 'chord_ids': [2]},
            'M1' : {'note': 'F', 'chord_ids': [1]},
            'P' : {'note': 'G', 'chord_ids': [1]},
            'D2' : {'note': 'A', 'chord_ids': [2]},
            'N3' : {'note': 'B', 'chord_ids': []},
        }
        self.assertCountEqual(
            shankara.get_chords('C'), chords_res)
