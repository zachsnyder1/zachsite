# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(primary_key=True,
                                        auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=120)),
                ('slug', models.SlugField(max_length=120)),
                ('tagline', models.CharField(max_length=80)),
                ('text', models.TextField()),
                ('pub_date', models.DateField()),
            ],
        ),
    ]
