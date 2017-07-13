# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, Http404
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
  try:
    puzzle = Puzzle.objects.get(pk=puzzleId)
  except Puzzle.DoesNotExist:
    raise Http404("Puzzle does not exist")
  context = {'puzzle': puzzle}
  return render(request, 'puzzles/view.html', context)

