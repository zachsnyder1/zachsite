# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True,
                                        verbose_name='ID', serialize=False, auto_created=True)),
                ('project_title', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionAndAnswer',
            fields=[
                ('id', models.AutoField(primary_key=True,
                                        verbose_name='ID', serialize=False, auto_created=True)),
                ('question_text', models.CharField(max_length=120)),
                ('answer_text', models.CharField(max_length=120)),
            ],
        ),
    ]
