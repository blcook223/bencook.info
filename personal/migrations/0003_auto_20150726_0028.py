# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0002_auto_20150724_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='images',
            field=models.ManyToManyField(blank=True, to='personal.Image'),
        ),
    ]
