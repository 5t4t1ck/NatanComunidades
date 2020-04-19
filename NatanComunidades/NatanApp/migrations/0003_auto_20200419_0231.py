# Generated by Django 2.2 on 2020-04-19 02:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('NatanApp', '0002_auto_20200419_0229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donacion',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2020, 4, 19, 2, 31, 12, 507541, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='donacion',
            name='observaciones',
            field=models.TextField(blank=True, default=''),
        ),
    ]