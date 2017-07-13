# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

from .models import Puzzle

# Create your views here.
def index(request):
  puzzles = Puzzle.objects.all()
  context = {
    'puzzles': puzzles
  }
  return render(request, 'puzzles/index.html', context)

def insert(request):
  return HttpResponse("You're inserting a puzzle")

def edit(request, puzzleId):
  return HttpResponse("You're editing puzzle %s" % puzzleId)

def view(request, puzzleId):
  return HttpResponse("You're viewing puzzle %s" % puzzleId)

