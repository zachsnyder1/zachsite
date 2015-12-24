# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project_summary'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodeExample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('codetext', models.TextField()),
                ('project', models.ForeignKey(to='projects.Project')),
            ],
        ),
    ]
