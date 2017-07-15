from django.conf.urls import url

from . import views

app_name = 'puzzles'
urlpatterns = [
  # /puzzles
  url(r'^$', views.index, name='index'),
  # /puzzles/insert/
  url(r'^insert/$', views.insert, name='insert'),
  # /puzzles/insert/step1-metadata
  url(r'^insert/step1', views.insertMetadata, name='insert-metadata'),
  # /puzzles/insert/step2-hints
  url(r'^insert/step2', views.insertHints, name='insert-hints'),
  # /puzzles/8/edit/
  url(r'^(?P<puzzleId>[0-9]+)/edit/$', views.edit, name='edit'),
  # /puzzles/8/view/
  url(r'^(?P<puzzleId>[0-9]+)/view/$', views.view, name='view'),
]

