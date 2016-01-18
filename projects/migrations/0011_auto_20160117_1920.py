# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_auto_20160117_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='logo',
            field=models.CharField(max_length=30),
        ),
    ]
