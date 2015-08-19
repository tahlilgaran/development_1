__author__ = 'M'
from django import template
import datetime
register = template.Library()

@register.filter
def miladitoshamsi(datetime):
    return str(datetime.hour)+":"+str(datetime.minute)