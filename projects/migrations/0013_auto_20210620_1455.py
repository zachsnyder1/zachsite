# Generated by Django 3.2.4 on 2021-06-20 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_auto_20160220_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codeexample',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='symbolentity',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
