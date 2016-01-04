# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_symbolentity_orderingindex'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='symbolentity',
            options={'ordering': ['orderingIndex']},
        ),
    ]
