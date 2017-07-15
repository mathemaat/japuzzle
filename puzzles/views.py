# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Puzzle

# Create your views here.
def index(request):
  puzzles = Puzzle.objects.all()
  context = {
    'puzzles': puzzles
  }
  return render(request, 'puzzles/index.html', context)

def insert(request):
  return HttpResponseRedirect(reverse('puzzles:insert-metadata'))

def insertMetadata(request):
  fields = ['number', 'title', 'width', 'height']
  context = {}
  for field in fields:
    context[field] = None
  if (len(request.POST) >= 1):
    for field in fields:
      if field not in request.POST:
        return Http404("Field '%s' was not posted" % field)
      context[field] = request.POST[field]
  if None in context.values():
    return render(request, 'puzzles/insert/metadata.html', context)
  else:
    return HttpResponseRedirect(reverse('puzzles:insert-hints'))

def insertHints(request):
  return HttpResponse("You're inserting the puzzle's hints")

def edit(request, puzzleId):
  return HttpResponse("You're editing puzzle %s" % puzzleId)

def view(request, puzzleId):
  puzzle = get_object_or_404(Puzzle, pk=puzzleId)
  context = {'puzzle': puzzle}
  return render(request, 'puzzles/view.html', context)

