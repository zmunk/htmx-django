# Generated by Django 3.2.12 on 2023-08-21 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
