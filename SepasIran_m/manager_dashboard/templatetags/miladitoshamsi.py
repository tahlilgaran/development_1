__author__ = 'M'
import jalali
from django import template
import datetime
register = template.Library()
#@register.filter(name='miladitoshamsi')

@register.filter
def miladitoshamsi(date):
    try:
        d = jalali.Gregorian(date).persian_string()
    except:
        d2 = datetime.date(date.year,date.month,date.day)
        d = jalali.Gregorian(d2).persian_string()

    return d