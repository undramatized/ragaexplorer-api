# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Raga(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    melakarta = models.ForeignKey('Raga', null=True)
    arohanam = models.CharField(max_length=100, blank=False, null=False)
    avarohanam = models.CharField(max_length=100, blank=False, null=False)
