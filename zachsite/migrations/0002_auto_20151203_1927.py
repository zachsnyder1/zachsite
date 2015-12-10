# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zachsite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blurb',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=80)),
                ('text', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='project',
            old_name='project_title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='questionandanswer',
            old_name='answer_text',
            new_name='answer',
        ),
        migrations.RenameField(
            model_name='questionandanswer',
            old_name='question_text',
            new_name='question',
        ),
        migrations.AddField(
            model_name='project',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
