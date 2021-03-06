# Generated by Django 3.1.3 on 2020-11-28 16:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('skillsgraph', '0009_auto_20201128_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='count',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='language',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='language',
            name='last_update',
            field=models.DateField(default=datetime.datetime(2020, 11, 28, 16, 4, 43, 397497, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='overtime_job',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2020, 11, 28, 16, 4, 43, 398534, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='overtime_job',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='overtime_skill',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2020, 11, 28, 16, 4, 43, 398892, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='overtime_skill',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='skill',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
