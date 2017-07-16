from django.conf.urls import url

from . import views

app_name = 'puzzles'
urlpatterns = [
  # /puzzles
  url(r'^$', views.index, name='index'),
  # /puzzles/8/
  url(r'^(?P<puzzleId>[0-9]+)/$', views.view, name='view'),
  # /puzzles/8/edit/
  url(r'^(?P<puzzleId>[0-9]+)/edit/$', views.edit, name='edit'),
]

