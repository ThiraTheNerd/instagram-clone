# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2021-07-10 23:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='caption',
            field=models.CharField(max_length=300),
        ),
    ]
