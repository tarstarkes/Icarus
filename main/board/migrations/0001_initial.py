# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-15 01:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventsBoardmeeting',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField()),
                ('agenda_id', models.IntegerField(blank=True, null=True)),
                ('minutes_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'events_boardmeeting',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='EventsDocument',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150)),
                ('url', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'events_document',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='EventsDocumenttype',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'events_documenttype',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='EventsMeetinglocation',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'events_meetinglocation',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='eventsdocument',
            name='type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.EventsDocumenttype'),
        ),
        migrations.AddField(
            model_name='eventsboardmeeting',
            name='location_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.EventsMeetinglocation'),
        ),
    ]
