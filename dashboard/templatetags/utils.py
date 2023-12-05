from datetime import datetime

from django import template
from django.contrib.auth.models import User
from django.urls import reverse

register = template.Library()


@register.filter
def count_contributors(contributors):
    return contributors.count()


@register.simple_tag(takes_context=True)
def abs_url(context, view_name, *args, **kwargs):
    # Could add except for KeyError, if rendering the template
    # without a request available.
    return context['request'].build_absolute_uri(
        reverse(view_name, args=args, kwargs=kwargs)
    )


@register.filter
def get_contri_length(contributors: list):
    if len(contributors) > 7:
        return len(contributors[6:])


@register.filter
def as_abs_url(path, request):
    return request.build_absolute_uri(path)


@register.filter
def get_image_url(image_inst):
    if image_inst:
        return image_inst.url
    else:
        return ''


@register.filter
def calculate_percentage(value, args: int):
    if value == 0 or args == 0:
        return 0
    if value > args:
        return 100
    return (value / args) * 100


@register.filter
def days_until(date):
    delta = date - datetime.now().date()
    return delta.days


@register.filter
def get_full_user_name(user: User):
    return user.get_full_name()
