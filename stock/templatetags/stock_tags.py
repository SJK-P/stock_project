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


@register.filter(name='cap_format')
def cap_format(value):
    tril = 1000000000000
    number = value/tril
    return round(number, 2)


@register.filter(is_safe=True)
def add_ch(value, ch):
    return ch+str(value)

@register.filter(is_safe=True)
def add_ch_end(value, ch):
    return str(value)+ch


        