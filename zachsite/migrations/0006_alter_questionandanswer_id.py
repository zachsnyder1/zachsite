# Generated by Django 3.2.4 on 2021-06-20 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zachsite', '0005_delete_blurb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionandanswer',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]