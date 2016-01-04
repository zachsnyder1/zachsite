# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20151224_2345'),
    ]

    operations = [
        migrations.AddField(
            model_name='symbolentity',
            name='orderingIndex',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
