# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_auto_20160114_2044'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='has_docs',
            field=models.BooleanField(default=True),
        ),
    ]
