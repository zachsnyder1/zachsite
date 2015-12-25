# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConstructorParam',
            fields=[
                ('symbolentity_ptr', models.OneToOneField(serialize=False, primary_key=True, to='projects.SymbolEntity', auto_created=True, parent_link=True)),
                ('default', models.CharField(max_length=120, blank=True)),
                ('pclass', models.ForeignKey(to='projects.ProjClass')),
            ],
            bases=('projects.symbolentity',),
        ),
        migrations.CreateModel(
            name='MethodParam',
            fields=[
                ('symbolentity_ptr', models.OneToOneField(serialize=False, primary_key=True, to='projects.SymbolEntity', auto_created=True, parent_link=True)),
                ('default', models.CharField(max_length=120, blank=True)),
                ('method', models.ForeignKey(to='projects.ClassMethod')),
            ],
            bases=('projects.symbolentity',),
        ),
        migrations.RemoveField(
            model_name='constructorarg',
            name='pclass',
        ),
        migrations.RemoveField(
            model_name='constructorarg',
            name='symbolentity_ptr',
        ),
        migrations.RemoveField(
            model_name='methodarg',
            name='method',
        ),
        migrations.RemoveField(
            model_name='methodarg',
            name='symbolentity_ptr',
        ),
        migrations.DeleteModel(
            name='ConstructorArg',
        ),
        migrations.DeleteModel(
            name='MethodArg',
        ),
    ]
