# Generated by Django 2.2 on 2020-04-19 02:19

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Donacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donante', models.CharField(default='', max_length=150)),
                ('fecha', models.DateField(default=datetime.datetime(2020, 4, 19, 2, 19, 39, 28386, tzinfo=utc))),
                ('imagen', models.ImageField(default='images/none.jpg', upload_to='images')),
                ('observaciones', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('simbolo', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Donacionxarticulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('idarticulo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='NatanApp.Articulo')),
                ('iddonacion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='NatanApp.Donacion')),
            ],
        ),
        migrations.AddField(
            model_name='articulo',
            name='idmedida',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='NatanApp.Medida'),
        ),
    ]