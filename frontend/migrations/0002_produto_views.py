# Generated by Django 3.2.9 on 2021-11-15 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
