# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-17 13:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hood',
            name='location',
            field=models.IntegerField(choices=[(1, 'Nairobi'), (2, 'Kajiado'), (3, 'Mombasa'), (4, 'Kilifi'), (5, 'Kiambu')]),
        ),
    ]
