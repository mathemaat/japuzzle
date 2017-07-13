# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse

# Create your views here.
def index(request):
  return HttpResponse("Hello, world. You're at the puzzles index.")

def insert(request):
  return HttpResponse("You're inserting a puzzle")

def edit(request, puzzleId):
  return HttpResponse("You're editing puzzle %s" % puzzleId)

def view(request, puzzleId):
  return HttpResponse("You're viewing puzzle %s" % puzzleId)

