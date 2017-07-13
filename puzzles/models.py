# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

# Create your models here.
@python_2_unicode_compatible
class PuzzleType(models.Model):
  description = models.CharField(max_length=128)
  token       = models.CharField(max_length=32, editable=False)

  def __str__(self):
    return self.description

@python_2_unicode_compatible
class Puzzle(models.Model):
  number   = models.IntegerField(default=0)
  title    = models.CharField(max_length=128)
  width    = models.IntegerField(default=0)
  height   = models.IntegerField(default=0)
  rowhints = models.TextField()
  colhints = models.TextField()

  puzzletype = models.ForeignKey(PuzzleType, null=True)

  def __str__(self):
    return '%d. %s' % (self.number, self.title)

