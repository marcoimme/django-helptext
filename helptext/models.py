# -*- coding: utf-8 -*-
from datetime import datetime
from django.db import models
from django.db.models.fields import CommaSeparatedIntegerField
from django.utils.translation import gettext as _


class Selector(models.Model):

    CHOICE_TYPES = (
        ('slug', 'Slug'),
        ('css_selector', 'CSS Selector'),
    )

    type = models.CharField(choices=CHOICE_TYPES, max_length=25)
    selector = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return "{} ({})".format(self.get_type_display(), self.selector)

    class Meta:
        verbose_name = _("Selector")
        verbose_name_plural = _("Selectors")
        unique_together = (("type", "selector"),)


class HelpText(models.Model):

    POSITION_TYPES = (
        ('right top', 'Right Top'),
        ('right center', 'Right Center'),
        ('right bottom', 'Right Bottom'),
        ('top center', 'Top Center'),
        ('top right', 'Top Right'),
        ('top left', 'Top Left'),
        ('bottom right', 'Bottom Right'),
        ('bottom left', 'Bottom Left'),
        ('bottom center', 'Bottom Center'),
        ('left top', 'Left Top'),
        ('left center', 'Left Center'),
        ('left bottom', 'Left Bottom'),

    )

    CLASSES = (
        ('qtip-plain', 'Plain (CSS2 style)'),
        ('qtip-light', 'Light (CSS2 style)'),
        ('qtip-dark', 'Dark (CSS2 style)'),
        ('qtip-red', 'Red (CSS2 style)'),
        ('qtip-green', 'Green (CSS2 style)'),
        ('qtip-blue', 'Blue (CSS2 style)'),
        ('qtip-shadow', 'Adds a shadows to your tooltips (CSS3+ style)'),
        ('qtip-rounded', 'Adds a rounded corner to your tooltips (CSS3+ style)'),
        ('qtip-bootstrap', 'Bootstrap style (CSS3+ style)'),
        ('qtip-tipsy', 'Tipsy style (CSS3+ style)'),
        ('qtip-youtube', 'Youtube style (CSS3+ style)'),
        ('qtip-jtools', 'jTools tooltip style (CSS3+ style)'),
        ('qtip-cluetip', 'ClueTip style (CSS3+ style)'),
        ('qtip-tipped', 'Tipped style (CSS3+ style)'),
    )

    selector = models.ForeignKey(Selector)
    date = models.DateField(default=datetime.today)
    html_content = models.TextField(help_text=_('HTML content'))
    enabled = models.BooleanField(default=False, help_text=_('Enabled'))
    position = models.CharField(help_text=_('Positions'), choices=POSITION_TYPES, max_length=25, default='top left')
    classes = models.CharField(help_text=_('CSS classes'), null=True, blank=True, max_length=255)

    @property
    def selected_classes(self):
        if self.classes:
            return self.classes.replace(",", " ")
        return None

    def __str__(self):
        return "{} {}".format(self.selector, self.date)

    class Meta:
        verbose_name = _("HelpText")
        verbose_name_plural = _("HelpText")
