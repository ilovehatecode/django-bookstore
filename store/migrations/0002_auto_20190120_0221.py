# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2019-01-20 02:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='stock',
            field=models.IntegerField(default=0),
        ),
    ]
