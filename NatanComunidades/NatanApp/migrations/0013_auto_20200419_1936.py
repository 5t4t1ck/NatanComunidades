# Generated by Django 2.2 on 2020-04-19 23:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('NatanApp', '0012_auto_20200419_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donacion',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2020, 4, 19, 23, 36, 3, 444317, tzinfo=utc)),
        ),
    ]
