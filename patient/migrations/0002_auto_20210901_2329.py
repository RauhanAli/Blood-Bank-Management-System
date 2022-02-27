# Generated by Django 3.0.5 on 2021-09-01 18:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='city',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='patient',
            name='gender',
            field=models.CharField(blank=True, max_length=1),
        ),
        migrations.AddField(
            model_name='patient',
            name='nic',
            field=models.PositiveIntegerField(blank=True, default=123),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='reg_date',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
    ]
