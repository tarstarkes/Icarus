# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-31 00:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stepwise', '0007_auto_20170127_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prospectus',
            name='opp_lead_email',
            field=models.EmailField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='prospectus',
            name='tech_contact_email',
            field=models.EmailField(blank=True, max_length=50),
        ),
    ]
