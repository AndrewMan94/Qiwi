# Generated by Django 4.0 on 2021-12-15 14:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.utcnow),
        ),
    ]