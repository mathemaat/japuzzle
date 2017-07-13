from django.conf.urls import url

from . import views

urlpatterns = [
  # /puzzles
  url(r'^$', views.index, name='index'),
  # /puzzles/insert/
  url(r'^insert/$', views.insert, name='insert'),
  # /puzzles/8/edit/
  url(r'^(?P<puzzleId>[0-9]+)/edit/$', views.edit, name='edit'),
  # /puzzles/8/view/
  url(r'^(?P<puzzleId>[0-9]+)/view/$', views.view, name='view'),
]

