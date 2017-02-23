# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-03 00:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stepwise', '0015_auto_20170202_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='landowner',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
