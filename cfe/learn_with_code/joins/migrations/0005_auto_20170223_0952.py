# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-23 17:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0004_join_ref_id'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='join',
            unique_together=set([('email', 'ref_id')]),
        ),
    ]
