# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0002_remove_link_element_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='opensourcecontribution',
            options={'ordering': ('name',), 'verbose_name': 'open-source contribution'},
        ),
        migrations.AlterModelOptions(
            name='technology',
            options={'ordering': ('category', 'name'), 'verbose_name_plural': 'technologies'},
        ),
        migrations.AlterField(
            model_name='event',
            name='html',
            field=models.TextField(verbose_name='HTML content'),
        ),
        migrations.AlterField(
            model_name='image',
            name='alt',
            field=models.CharField(verbose_name='alt text', max_length=500),
        ),
        migrations.AlterField(
            model_name='link',
            name='href',
            field=models.CharField(verbose_name='URL', null=True, blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='link',
            name='target',
            field=models.BooleanField(verbose_name='Open in new tab', default=False),
        ),
    ]
