# Generated by Django 2.2 on 2019-08-21 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='sb3',
            field=models.IntegerField(default=0),
        ),
    ]
