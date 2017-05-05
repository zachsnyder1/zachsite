# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20160104_2006'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModuleConstant',
            fields=[
                ('symbolentity_ptr', models.OneToOneField(parent_link=True, primary_key=True,
                                                          to='projects.SymbolEntity', serialize=False, auto_created=True)),
                ('module', models.ForeignKey(to='projects.ProjModule')),
            ],
            bases=('projects.symbolentity',),
        ),
        migrations.RemoveField(
            model_name='classconstant',
            name='pclass',
        ),
        migrations.RemoveField(
            model_name='classconstant',
            name='symbolentity_ptr',
        ),
        migrations.DeleteModel(
            name='ClassConstant',
        ),
    ]
