from django import template
import json
register = template.Library()


@register.filter(name="format_meters")
def meters_to_kms(value):
    try:
        return round(value / 1000)
    except:
        return "NaN"

@register.filter(name="format_daily_meters_hourly_rate")
def meters_per_day_to_km_per_hour(value):
    try:
        return (value / 24) / 1000
    except:
        return "0"

@register.filter(name='json')
def jsonit(obj):
    return json.dumps(obj)

@register.filter(name='dict_get')
def dict_get(tdict, key):
    if type(tdict) is not dict:
        tdict = tdict.__dict__
    return tdict.get(key, None)


@register.filter(name='format')
def format(format, var):
    return format.format(var)

@register.simple_tag
def stringformat(value, *args):
    return value.format(*args)

@register.filter(name="percentage")
def percentage(value, *args):
    if not value:
        return "NaN"
    try:
        return str(round(float(value) * 100)) + "%"
    except ValueError:
        return value
