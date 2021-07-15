# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2021-07-15 07:59
from __future__ import unicode_literals

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20210714_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='profile_pic'),
        ),
    ]
