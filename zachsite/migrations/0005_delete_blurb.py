# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zachsite', '0004_delete_project'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Blurb',
        ),
    ]
