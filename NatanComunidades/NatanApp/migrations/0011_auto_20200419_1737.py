# Generated by Django 2.2 on 2020-04-19 17:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('NatanApp', '0010_auto_20200419_0549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='nombre',
            field=models.CharField(max_length=45, unique=True),
        ),
        migrations.AlterField(
            model_name='donacion',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2020, 4, 19, 17, 37, 22, 314399, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='medida',
            name='simbolo',
            field=models.CharField(max_length=45, unique=True),
        ),
    ]