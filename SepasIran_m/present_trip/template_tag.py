__author__ = 'farzanehtahooni'
from django.template import Library

register = Library()

@register.filter(name= 'sub')
def subtract(value, arg):
    return value - arg
