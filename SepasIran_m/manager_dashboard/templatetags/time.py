__author__ = 'M'
from django import template
register = template.Library()

@register.filter
def time(datetime):
    return str(datetime.hour)+":"+str(datetime.minute)