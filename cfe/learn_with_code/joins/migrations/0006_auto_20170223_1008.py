# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-23 18:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0005_auto_20170223_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='join',
            name='ip_address',
            field=models.CharField(default='ABC', max_length=120, unique=True),
        ),
    ]