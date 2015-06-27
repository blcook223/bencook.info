# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('category', models.CharField(max_length=1, default='T', choices=[('T', 'Technical'), ('P', 'Professional')])),
                ('level', models.CharField(max_length=1, default='1', choices=[('1', 'Beginner (1)'), ('2', 'Intermediate (2)'), ('3', 'Competent (3)'), ('4', 'Proficient (4)'), ('5', 'Expert (5)')])),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]
