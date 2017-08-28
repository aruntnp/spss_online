# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-27 22:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_purchase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='license_type',
            field=models.CharField(choices=[('1 year', '12'), ('2 years', '24'), ('perpetual', '999999')], default='1 year', max_length=50),
        ),
    ]
