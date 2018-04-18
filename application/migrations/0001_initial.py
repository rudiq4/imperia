# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-30 09:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Назва продукту')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Ціна')),
                ('image', models.ImageField(upload_to='production_image/', verbose_name='Фото')),
                ('description', models.TextField(verbose_name='Опис')),
                ('flag', models.BooleanField(default=True, verbose_name='акт/деакт')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Створено')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Оновлено')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товари',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Тип товару')),
            ],
            options={
                'verbose_name': 'Тип товару',
                'verbose_name_plural': 'Типи товарів',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.Type', verbose_name='Тип'),
        ),
    ]
