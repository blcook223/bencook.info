# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0003_auto_20150630_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='links',
            field=models.ManyToManyField(to='personal.Link'),
        ),
        migrations.AlterUniqueTogether(
            name='technology',
            unique_together=set([('name', 'category')]),
        ),
    ]
