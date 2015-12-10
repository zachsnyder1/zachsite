# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zachsite', '0003_project_slug'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Project',
        ),
    ]
