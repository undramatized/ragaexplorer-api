# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from ragas.helpers import chord_helper, raga_helper

# Create your models here.

class Chord(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    description = models.CharField(max_length=1000, blank=True, null=True)
    formula = models.CharField(max_length=20, blank=False, null=False)
    affix = models.CharField(max_length=20, blank=False, null=False)

    # Returns the semitones that make up the chord formula
    def get_semitones(self):
        return chord_helper.get_chord_semitones(self)

    # Returns a full chord, based on root note
    def get_root_chord(self, root):
        chord_full_name = root + " " + self.name
        chord_name = root + self.affix
        chord_notes = chord_helper.get_chord_notes(self, root)
        chord_obj = {
            'name' : chord_full_name,
            'short' : chord_name,
            'notes' : chord_notes,
            'formula' : self.formula,
        }
        return chord_obj

class RagaManager(models.Manager):
    def filter_swaras(self, swaras):
        iter_qs = self.get_queryset()
        filter_qs = self.get_queryset()

        for raga in iter_qs:
            if not raga.has_swaras(swaras):
                filter_qs = filter_qs.exclude(id=raga.id)

        return filter_qs

    def filter_swaras_queryset(self, swaras, queryset):
        iter_qs = queryset
        filter_qs = queryset

        for raga in iter_qs:
            if not raga.has_swaras(swaras):
                filter_qs = filter_qs.exclude(id=raga.id)

        return filter_qs


class Raga(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    format_name = models.CharField(max_length=100, blank=False, null=False, default="")
    melakarta = models.ForeignKey('Raga', null=True)
    arohanam = models.CharField(max_length=100, blank=False, null=False)
    avarohanam = models.CharField(max_length=100, blank=False, null=False)


    objects = RagaManager()

    # Returns a list of swaras in the arohanam
    def get_aro_swaras(self):
        return self.arohanam.split(" ")

    # Returns a list of swaras in the avarohanam
    def get_ava_swaras(self):
        return self.avarohanam.split(" ")

    # Returns a list of swaras in both the arohanam & avarohanam
    def get_swaras(self):
        aro = set(self.arohanam.split(" "))
        ava = set(self.avarohanam.split(" "))
        return list(aro | ava)

    # Checks if a string of space-seperated swaras are contained in a raga
    # Returns boolean
    def has_swaras(self, swaras):
        filter_swaras = set(swaras.split(" "))
        all_swaras = set(self.get_swaras())
        return filter_swaras.issubset(all_swaras)

    # Given a root note, get all chords that can work within a raga
    def get_chords(self, root):
        swaras = self.get_swaras()
        chords = Chord.objects.all()
        return raga_helper.get_chords_from_swaras(swaras, chords, root)
