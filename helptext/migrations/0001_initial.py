# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HelpText',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(default=datetime.datetime.today)),
                ('html_content', models.TextField(help_text=b'HTML content')),
                ('enabled', models.BooleanField(default=False, help_text=b'Enabled')),
                ('position', models.CharField(default=b'top left', help_text=b'Positions', max_length=25, choices=[(b'right top', b'Right Top'), (b'right center', b'Right Center'), (b'right bottom', b'Right Bottom'), (b'top center', b'Top Center'), (b'top right', b'Top Right'), (b'top left', b'Top Left'), (b'bottom right', b'Bottom Right'), (b'bottom left', b'Bottom Left'), (b'bottom center', b'Bottom Center'), (b'left top', b'Left Top'), (b'left center', b'Left Center'), (b'left bottom', b'Left Bottom')])),
                ('classes', models.CharField(help_text=b'CSS classes', max_length=255, null=True, blank=True)),
            ],
            options={
                'verbose_name': 'HelpText',
                'verbose_name_plural': 'HelpText',
            },
        ),
        migrations.CreateModel(
            name='Selector',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=25, choices=[(b'slug', b'Slug'), (b'css_selector', b'CSS Selector')])),
                ('selector', models.CharField(unique=True, max_length=255)),
            ],
            options={
                'verbose_name': 'Selector',
                'verbose_name_plural': 'Selectors',
            },
        ),
        migrations.AlterUniqueTogether(
            name='selector',
            unique_together=set([('type', 'selector')]),
        ),
        migrations.AddField(
            model_name='helptext',
            name='selector',
            field=models.ForeignKey(to='helptext.Selector'),
        ),
    ]
