# -*- coding: utf-8 -*-
from __future__ import absolute_import
import datetime
from django.template import Library
from helptext.models import HelpText
from django.db.models import Q


register = Library()


@register.inclusion_tag('helptext/helptext_slug.html', takes_context=True)
def helptext_slug(context, slug):
    ctx = {}
    try:
        ht = HelpText.objects.get(enabled=True, selector__type='slug', selector__selector=slug)
        ctx.update({'helptext': ht})
    except HelpText.DoesNotExist:
        ctx.update({})

    return ctx


@register.inclusion_tag('helptext/helptext.html', takes_context=True)
def helptext(context):
    ctx = {}
    ht = HelpText.objects.filter(enabled=True, selector__type='css_selector')
    ctx.update({'objects': ht})

    return ctx