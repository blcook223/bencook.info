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
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=200)),
                ('order_date', models.DateField(null=True, default=django.utils.timezone.now, blank=True)),
                ('html', models.TextField(verbose_name='HTML content')),
            ],
            options={
                'ordering': ('order_date',),
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, null=True, blank=True)),
                ('image_file', models.ImageField(upload_to='uploaded/personal')),
                ('alt', models.CharField(max_length=500, verbose_name='alt text')),
                ('credit', models.CharField(max_length=200, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('end_date', models.DateField(null=True, default=django.utils.timezone.now, blank=True)),
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
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, null=True, blank=True)),
                ('href', models.CharField(max_length=200, verbose_name='URL', null=True, blank=True)),
                ('text', models.CharField(max_length=200, null=True, blank=True)),
                ('target', models.BooleanField(verbose_name='Open in new tab', default=False)),
            ],
            options={
                'ordering': ('text',),
            },
        ),
        migrations.CreateModel(
            name='OpenSourceContribution',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('link', models.ForeignKey(to='personal.Link')),
            ],
            options={
                'verbose_name': 'open-source contribution',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('end_date', models.DateField(null=True, default=django.utils.timezone.now, blank=True)),
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
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=1, default='L', choices=[('T', 'Technical'), ('P', 'Professional'), ('L', 'Language')])),
                ('level', models.CharField(max_length=1, default='1', choices=[('1', 'Beginner (1)'), ('2', 'Intermediate (2)'), ('3', 'Competent (3)'), ('4', 'Proficient (4)'), ('5', 'Expert (5)')])),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ('category', 'level', 'name'),
            },
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=1, default='A', choices=[('A', 'Language'), ('B', 'Framework'), ('C', 'Database'), ('D', 'Editor'), ('E', 'Other')])),
            ],
            options={
                'verbose_name_plural': 'technologies',
                'ordering': ('category', 'name'),
            },
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
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
            field=models.ForeignKey(to='personal.Link', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='event',
            name='images',
            field=models.ManyToManyField(to='personal.Image'),
        ),
    ]
