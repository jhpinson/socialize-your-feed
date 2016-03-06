# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-06 16:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='last_fetch_date',
            field=models.DateTimeField(default=None, editable=None, null=True, verbose_name='Last fetched at'),
        ),
    ]