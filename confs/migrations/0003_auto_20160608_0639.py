# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-08 06:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('confs', '0002_auto_20160607_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conference',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 18, 6, 39, 5, 606561)),
        ),
        migrations.AlterField(
            model_name='conference',
            name='event_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 28, 6, 39, 5, 606402)),
        ),
    ]
