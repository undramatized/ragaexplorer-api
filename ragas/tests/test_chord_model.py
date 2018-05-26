# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json, datetime

from django.test import TestCase
from ragas.models import Chord

class ChordTestCase(TestCase):
    def setUp(self):
        Chord.objects.create(
            id = 1,
            name = "Major",
            formula = "1 3 5",
            affix = "maj",
            description = "Named after the major 3rd interval between root and 3"
        )
        Chord.objects.create(
            id = 2,
            name = "Min 7th",
            formula = "1 b3 5 b7",
            affix = "min7",
            description = ""
        )
        Chord.objects.create(
            id = 3,
            name = "5th",
            formula = "1 5",
            affix = "5",
            description = ""
        )

    def test_get_root_chord(self):
        maj = Chord.objects.get(pk=1)
        get_maj_chord = maj.get_root_chord('C')

        maj_chord = {
            'name' : "C Major",
            'short' : "Cmaj",
            'notes' : [{'note': "C", 'omitted': False},{'note': "E", 'omitted': False},{'note': "G", 'omitted': False},],
            'formula' : "1 3 5",
        }
        self.assertCountEqual(get_maj_chord, maj_chord)
