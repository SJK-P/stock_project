from django import template
import datetime

register = template.Library()

@register.filter(name='date_format', expects_localtime=True)
def date_format(value, format_string):
    api_date_format = '%Y-%m-%dT%H:%M:%S.%f%z'
    try:    
        value = datetime.datetime.strptime(value, api_date_format)
        print("sdafsdfasdfasfasdf",format_string, value)
        return value.strftime(format_string)
    except:
        return ''

