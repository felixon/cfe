# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-23 21:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0009_auto_20170223_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='join',
            name='friends',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='referral', to='joins.Join'),
        ),
    ]