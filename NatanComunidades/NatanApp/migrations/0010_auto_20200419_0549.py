# Generated by Django 2.2 on 2020-04-19 05:49

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('NatanApp', '0009_auto_20200419_0516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donacion',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2020, 4, 19, 5, 49, 23, 320615, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='donacionxarticulo',
            name='donacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NatanApp.Donacion'),
        ),
    ]
