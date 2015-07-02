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
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('end_date', models.DateField(default=django.utils.timezone.now, blank=True, null=True)),
                ('description', models.TextField()),
                ('html', models.TextField(verbose_name='HTML content')),
            ],
            options={
                'ordering': ('-start_date', '-end_date'),
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('image_file', models.ImageField(upload_to='uploaded/personal')),
                ('alt', models.CharField(max_length=500, verbose_name='alt text')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
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
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('href', models.CharField(blank=True, max_length=200, null=True, verbose_name='URL')),
                ('text', models.CharField(blank=True, max_length=200, null=True)),
                ('target', models.BooleanField(default=False, verbose_name='Open in new tab')),
            ],
            options={
                'ordering': ('text',),
            },
        ),
        migrations.CreateModel(
            name='OpenSourceContribution',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('link', models.ForeignKey(to='personal.Link')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'open-source contribution',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('end_date', models.DateField(default=django.utils.timezone.now, blank=True, null=True)),
                ('name', models.CharField(max_length=200)),
                ('contribution', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('first_image', models.ForeignKey(related_name='first_project_image', to='personal.Image', null=True)),
                ('links', models.ManyToManyField(to='personal.Link', blank=True)),
                ('second_image', models.ForeignKey(related_name='second_project_image', to='personal.Image', null=True)),
            ],
            options={
                'ordering': ('-end_date', 'start_date'),
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('category', models.CharField(default='L', choices=[('T', 'Technical'), ('P', 'Professional'), ('L', 'Language')], max_length=1)),
                ('level', models.CharField(default='1', choices=[('1', 'Beginner (1)'), ('2', 'Intermediate (2)'), ('3', 'Competent (3)'), ('4', 'Proficient (4)'), ('5', 'Expert (5)')], max_length=1)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ('category', 'level', 'name'),
            },
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(default='A', choices=[('A', 'Language'), ('B', 'Framework'), ('C', 'Database'), ('D', 'Editor'), ('E', 'Other')], max_length=1)),
            ],
            options={
                'ordering': ('category', 'name'),
                'verbose_name_plural': 'technologies',
            },
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('quote', models.TextField()),
                ('source', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='technology',
            unique_together=set([('name', 'category')]),
        ),
        migrations.AddField(
            model_name='project',
            name='technologies',
            field=models.ManyToManyField(to='personal.Technology'),
        ),
        migrations.AddField(
            model_name='image',
            name='link',
            field=models.ForeignKey(blank=True, to='personal.Link', null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='images',
            field=models.ManyToManyField(to='personal.Image'),
        ),
    ]
