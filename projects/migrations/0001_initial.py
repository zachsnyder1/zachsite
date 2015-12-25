# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CodeExample',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('codetext', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=30)),
                ('slug', models.SlugField(max_length=30)),
                ('active', models.BooleanField(default=True)),
                ('summary', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SymbolEntity',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('symbol', models.CharField(max_length=120)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ClassMethod',
            fields=[
                ('symbolentity_ptr', models.OneToOneField(serialize=False, primary_key=True, parent_link=True, to='projects.SymbolEntity', auto_created=True)),
            ],
            bases=('projects.symbolentity',),
        ),
        migrations.CreateModel(
            name='ClassVariable',
            fields=[
                ('symbolentity_ptr', models.OneToOneField(serialize=False, primary_key=True, parent_link=True, to='projects.SymbolEntity', auto_created=True)),
            ],
            bases=('projects.symbolentity',),
        ),
        migrations.CreateModel(
            name='ConstructorArg',
            fields=[
                ('symbolentity_ptr', models.OneToOneField(serialize=False, primary_key=True, parent_link=True, to='projects.SymbolEntity', auto_created=True)),
                ('default', models.CharField(max_length=120, blank=True)),
            ],
            bases=('projects.symbolentity',),
        ),
        migrations.CreateModel(
            name='InstanceVariable',
            fields=[
                ('symbolentity_ptr', models.OneToOneField(serialize=False, primary_key=True, parent_link=True, to='projects.SymbolEntity', auto_created=True)),
            ],
            bases=('projects.symbolentity',),
        ),
        migrations.CreateModel(
            name='MethodArg',
            fields=[
                ('symbolentity_ptr', models.OneToOneField(serialize=False, primary_key=True, parent_link=True, to='projects.SymbolEntity', auto_created=True)),
                ('default', models.CharField(max_length=120, blank=True)),
                ('method', models.ForeignKey(to='projects.ClassMethod')),
            ],
            bases=('projects.symbolentity',),
        ),
        migrations.CreateModel(
            name='MethodReturn',
            fields=[
                ('symbolentity_ptr', models.OneToOneField(serialize=False, primary_key=True, parent_link=True, to='projects.SymbolEntity', auto_created=True)),
                ('method', models.ForeignKey(to='projects.ClassMethod')),
            ],
            bases=('projects.symbolentity',),
        ),
        migrations.CreateModel(
            name='ProjClass',
            fields=[
                ('symbolentity_ptr', models.OneToOneField(serialize=False, primary_key=True, parent_link=True, to='projects.SymbolEntity', auto_created=True)),
            ],
            bases=('projects.symbolentity',),
        ),
        migrations.CreateModel(
            name='ProjModule',
            fields=[
                ('symbolentity_ptr', models.OneToOneField(serialize=False, primary_key=True, parent_link=True, to='projects.SymbolEntity', auto_created=True)),
                ('path', models.CharField(max_length=300)),
                ('project', models.ForeignKey(to='projects.Project')),
            ],
            bases=('projects.symbolentity',),
        ),
        migrations.AddField(
            model_name='codeexample',
            name='project',
            field=models.ForeignKey(to='projects.Project'),
        ),
        migrations.AddField(
            model_name='projclass',
            name='module',
            field=models.ForeignKey(to='projects.ProjModule'),
        ),
        migrations.AddField(
            model_name='instancevariable',
            name='pclass',
            field=models.ForeignKey(to='projects.ProjClass'),
        ),
        migrations.AddField(
            model_name='constructorarg',
            name='pclass',
            field=models.ForeignKey(to='projects.ProjClass'),
        ),
        migrations.AddField(
            model_name='classvariable',
            name='pclass',
            field=models.ForeignKey(to='projects.ProjClass'),
        ),
        migrations.AddField(
            model_name='classmethod',
            name='pclass',
            field=models.ForeignKey(to='projects.ProjClass'),
        ),
    ]
