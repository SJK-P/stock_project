from django import template
import datetime
import math

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


@register.filter(is_safe=True)
def add_ch(value, ch):
    return ch+str(value)

@register.filter(is_safe=True)
def add_ch_end(value, ch):
    return str(value)+ch


millnames = ['','K','M','B','T']

@register.filter(name='millify')
def millify(n):
    n = float(n)
    millidx = max(0,min(len(millnames)-1,
                        int(math.floor(0 if n == 0 else math.log10(abs(n))/3))))

    return '{:.2f}{}'.format(n / 10**(3 * millidx), millnames[millidx])

@register.filter
def percentage(value):
    return format(value, ".1%")