# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-03 11:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180102_2228'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=60, verbose_name='slug'),
        ),
    ]
