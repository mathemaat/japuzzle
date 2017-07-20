from django import template

register = template.Library()

@register.filter(name='times')
def times(number):
  return range(number)

@register.filter(name='fifth')
def fifth(number):
  return number % 5 == 0

