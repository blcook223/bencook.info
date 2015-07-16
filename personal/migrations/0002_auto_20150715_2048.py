# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ('order_date',)},
        ),
        migrations.RemoveField(
            model_name='event',
            name='description',
        ),
        migrations.RemoveField(
            model_name='event',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='event',
            name='start_date',
        ),
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.CharField(default=datetime.datetime(2015, 7, 16, 1, 48, 34, 241259, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='order_date',
            field=models.DateField(null=True, blank=True, default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='event',
            name='title',
            field=models.CharField(default='title', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='credit',
            field=models.CharField(null=True, blank=True, max_length=200),
        ),
    ]
