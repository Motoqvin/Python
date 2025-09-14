from django import template

register = template.Library()

@register.filter
def readtime(value):
    words = len(value.split())
    minutes = max(1, int(round(words / 200.0)))
    return f'~{minutes} мин'