# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-05 01:10
from __future__ import unicode_literals

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20161229_1012'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='file',
            field=models.FileField(blank=True, upload_to=home.models.get_upload_path),
        ),
    ]
