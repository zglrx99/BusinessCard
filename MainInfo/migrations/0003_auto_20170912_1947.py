# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-12 16:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('MainInfo', '0002_auto_20170911_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='author',
            field=models.CharField(max_length=254, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 12, 16, 47, 9, 529578, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='phone_number',
            field=models.CharField(max_length=254, verbose_name='Контактный телефон'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='text',
            field=models.TextField(max_length=2048, verbose_name='Сообщение'),
        ),
    ]
