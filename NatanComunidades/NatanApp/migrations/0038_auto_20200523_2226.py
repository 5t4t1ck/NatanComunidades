# Generated by Django 2.2.10 on 2020-05-23 22:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('NatanApp', '0037_auto_20200523_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donacion',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2020, 5, 23, 22, 26, 28, 436064, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='donacion',
            name='imagen',
            field=models.ImageField(default='noimage.png', null=True, upload_to=''),
        ),
    ]
