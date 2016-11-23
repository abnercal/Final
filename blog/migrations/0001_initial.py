# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('codigo', models.CharField(max_length=7)),
                ('nombre', models.CharField(max_length=30)),
                ('imagen', models.ImageField(upload_to='imagen/', blank='True')),
                ('marca', models.CharField(default='Ro', choices=[('Ro', 'Ropa'), ('Ca', 'Calzado'), ('Be', 'Bebidas')], max_length=2)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('existencia', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('dpi', models.CharField(max_length=15)),
                ('nombre', models.CharField(max_length=60)),
                ('productos', models.ManyToManyField(to='blog.Producto', through='blog.Compra')),
            ],
        ),
        migrations.AddField(
            model_name='compra',
            name='producto',
            field=models.ForeignKey(to='blog.Producto'),
        ),
        migrations.AddField(
            model_name='compra',
            name='usuario',
            field=models.ForeignKey(to='blog.Usuario'),
        ),
    ]
