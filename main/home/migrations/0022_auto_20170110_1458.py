# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-10 22:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_video_extension'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='dropboxURL',
            new_name='youtubeURL',
        ),
    ]
