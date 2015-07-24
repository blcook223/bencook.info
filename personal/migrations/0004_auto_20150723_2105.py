# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0003_auto_20150715_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='images',
            field=models.ManyToManyField(to='personal.Image'),
        ),
    ]
