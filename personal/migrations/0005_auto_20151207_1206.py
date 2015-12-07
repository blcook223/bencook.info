# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0004_auto_20151206_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='category',
            field=models.CharField(max_length=1, default='L', choices=[('T', 'Technical'), ('P', 'Professional'), ('L', 'Language'), ('D', 'Database'), ('V', 'Development Tool')]),
        ),
    ]
