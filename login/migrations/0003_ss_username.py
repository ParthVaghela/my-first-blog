# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-03 05:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_ss'),
    ]

    operations = [
        migrations.AddField(
            model_name='ss',
            name='username',
            field=models.CharField(default=4, max_length=50),
            preserve_default=False,
        ),
    ]
