# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-17 10:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='compound',
            field=models.NullBooleanField(),
        ),
    ]
