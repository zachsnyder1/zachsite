# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20151204_2245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='entry',
            name='last_modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 12, 5, 6, 13, 58, 441168, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entry',
            name='pub_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 5, 6, 14, 12, 607488, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
