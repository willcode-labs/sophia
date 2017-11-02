# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-02 18:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20171017_1016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='merchant',
            name='login',
        ),
        migrations.RemoveField(
            model_name='exceptionlog',
            name='description',
        ),
        migrations.RemoveField(
            model_name='exceptionlog',
            name='login_client_id',
        ),
        migrations.AlterField(
            model_name='login',
            name='profile_id',
            field=models.IntegerField(choices=[(1, 'root'), (2, 'director'), (3, 'client')]),
        ),
        migrations.DeleteModel(
            name='Merchant',
        ),
    ]