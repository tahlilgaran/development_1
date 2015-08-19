__author__ = 'M'
import jalali
from django import template

register = template.Library()
#@register.filter(name='miladitoshamsi')

@register.filter
def miladitoshamsi(date):
    d = jalali.Gregorian(date).persian_string()
    return d