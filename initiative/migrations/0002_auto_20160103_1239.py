# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-03 12:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('initiative', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Effet',
            fields=[
                ('slug', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='Nom')),
                ('temps_restant', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ('-temps_restant', 'slug'),
            },
        ),
        migrations.AlterModelOptions(
            name='initiative',
            options={'ordering': ('-initiative', 'slug')},
        ),
    ]