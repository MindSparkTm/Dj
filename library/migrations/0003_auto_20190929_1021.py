# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-09-29 10:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20190921_1225'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'Author', 'verbose_name_plural': 'Authors'},
        ),
    ]
