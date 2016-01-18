# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_project_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='logo',
            field=models.ImageField(upload_to=''),
        ),
    ]
