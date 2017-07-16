# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from .models import Puzzle

# Create your views here.
def index(request):
  puzzles = Puzzle.objects.all()
  context = {'puzzles': puzzles}
  return render(request, 'puzzles/index.html', context)

def edit(request, puzzleId):
  puzzle = get_object_or_404(Puzzle, pk=puzzleId)
  context = {'puzzle': puzzle}
  return render(request, 'puzzles/edit.html', context)

def view(request, puzzleId):
  puzzle = get_object_or_404(Puzzle, pk=puzzleId)
  context = {'puzzle': puzzle}
  return render(request, 'puzzles/view.html', context)

