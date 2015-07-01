# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('end_date', models.DateField(default=django.utils.timezone.now, blank=True, null=True)),
                ('description', models.TextField()),
                ('html', models.TextField()),
            ],
            options={
                'ordering': ('-start_date', '-end_date'),
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('image_file', models.ImageField(upload_to='')),
                ('alt', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('end_date', models.DateField(default=django.utils.timezone.now, blank=True, null=True)),
                ('title', models.CharField(max_length=200)),
                ('employer', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ('-end_date', 'start_date'),
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('href', models.CharField(blank=True, max_length=200, null=True)),
                ('element_id', models.CharField(blank=True, max_length=200, null=True)),
                ('text', models.CharField(blank=True, max_length=200, null=True)),
                ('target', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('text',),
            },
        ),
        migrations.CreateModel(
            name='OpenSourceContribution',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('link', models.ForeignKey(to='personal.Link')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('end_date', models.DateField(default=django.utils.timezone.now, blank=True, null=True)),
                ('name', models.CharField(max_length=200)),
                ('contribution', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ('-end_date', 'start_date'),
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('category', models.CharField(default='L', max_length=1, choices=[('T', 'Technical'), ('P', 'Professional'), ('L', 'Language')])),
                ('level', models.CharField(default='1', max_length=1, choices=[('1', 'Beginner (1)'), ('2', 'Intermediate (2)'), ('3', 'Competent (3)'), ('4', 'Proficient (4)'), ('5', 'Expert (5)')])),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ('category', 'level', 'name'),
            },
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(default='A', max_length=1, choices=[('A', 'Language'), ('B', 'Framework'), ('C', 'Database'), ('D', 'Editor'), ('E', 'Other')])),
            ],
            options={
                'ordering': ('category', 'name'),
            },
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('quote', models.TextField()),
                ('source', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='technologies',
            field=models.ManyToManyField(to='personal.Technology'),
        ),
        migrations.AddField(
            model_name='image',
            name='link',
            field=models.ForeignKey(to='personal.Link', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='images',
            field=models.ManyToManyField(to='personal.Image'),
        ),
    ]
