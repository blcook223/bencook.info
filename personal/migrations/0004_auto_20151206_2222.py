# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0003_auto_20150726_0028'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ('-priority',)},
        ),
        migrations.AddField(
            model_name='project',
            name='priority',
            field=models.IntegerField(default=500),
        ),
    ]
