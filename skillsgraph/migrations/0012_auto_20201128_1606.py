# Generated by Django 3.1.3 on 2020-11-28 16:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('skillsgraph', '0011_auto_20201128_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='last_update',
            field=models.DateField(default=datetime.datetime(2020, 11, 28, 16, 6, 59, 166978, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='overtime_job',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2020, 11, 28, 16, 6, 59, 168070, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='overtime_skill',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2020, 11, 28, 16, 6, 59, 168468, tzinfo=utc)),
        ),
    ]
