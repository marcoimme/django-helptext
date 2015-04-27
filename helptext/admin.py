# -*- coding: utf-8 -*-
from django import forms
from django.contrib.admin import ModelAdmin, site
from helptext.fields import TextMultiField
from helptext.models import HelpText, Selector


class EnhWidget(forms.Textarea):
    def __init__(self, attrs=None, editor_options=None):
        super(EnhWidget, self).__init__(attrs)

try:
    from suit_redactor.widgets import RedactorWidget as EnhWidget
except ImportError:
    pass

try:
    from suit_ckeditor.widgets import CKEditorWidget as EnhWidget
except ImportError:
    pass


class HelpTextForm(forms.ModelForm):
    classes = TextMultiField(choices=HelpText.CLASSES, required=False)

    class Meta:
        widgets = {
            'html_content': EnhWidget(editor_options={'lang': 'en'})
        }


class HelpTextAdmin(ModelAdmin):
    list_display = ('selector', 'html_content', 'date', 'enabled')
    form = HelpTextForm

class SelectorAdmin(ModelAdmin):
    list_display = ('type', )

site.register(HelpText, HelpTextAdmin)
site.register(Selector, SelectorAdmin)
