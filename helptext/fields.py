from django import forms
from django.core import validators
from django.db import models
from django.forms import widgets


class TextCheckboxSelectMultiple(widgets.CheckboxSelectMultiple):
    """
    Set checked values based on a comma separated list instead of a python list
    """
    def render(self, name, value, **kwargs):
        if isinstance(value, basestring):
            value = value.split(",")
        return super(TextCheckboxSelectMultiple, self).render(name, value, **kwargs)


class TextMultiField(forms.MultipleChoiceField):
    """
    Work in conjunction with TextCheckboxSelectMultiple to store a
    comma separated list of multiple choice values in a CharField/TextField
    """
    widget = TextCheckboxSelectMultiple
    def clean(self, value):
        val = super(TextMultiField, self).clean(value)
        return ",".join(val)