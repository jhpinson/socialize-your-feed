# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-06 16:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0003_auto_20160306_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='url',
            field=models.URLField(default='', verbose_name='Entry URL'),
            preserve_default=False,
        ),
    ]
