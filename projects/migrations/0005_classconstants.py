# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20160103_2117'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassConstants',
            fields=[
                ('symbolentity_ptr', models.OneToOneField(serialize=False, auto_created=True,
                                                          to='projects.SymbolEntity', parent_link=True,
                                                          primary_key=True, on_delete=models.CASCADE)),
                ('pclass', models.ForeignKey(to='projects.ProjClass', on_delete=models.CASCADE)),
            ],
            bases=('projects.symbolentity',),
        ),
    ]
