# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_classconstants'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ClassConstants',
            new_name='ClassConstant',
        ),
    ]
