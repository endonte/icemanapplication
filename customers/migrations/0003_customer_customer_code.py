# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-16 08:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_auto_20170901_0157'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='customer_code',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Customer Code'),
        ),
    ]
