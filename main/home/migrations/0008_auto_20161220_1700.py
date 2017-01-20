# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-21 01:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20161220_1649'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='contact',
            table='db_contact',
        ),
        migrations.AlterModelTable(
            name='contactrole',
            table='db_contactrole',
        ),
        migrations.AlterModelTable(
            name='contacttype',
            table='db_contacttype',
        ),
        migrations.AlterModelTable(
            name='contract',
            table='db_contract',
        ),
        migrations.AlterModelTable(
            name='date',
            table='db_date',
        ),
        migrations.AlterModelTable(
            name='datetype',
            table='db_datetype',
        ),
        migrations.AlterModelTable(
            name='document',
            table='db_document',
        ),
        migrations.AlterModelTable(
            name='documenttype',
            table='db_documenttype',
        ),
        migrations.AlterModelTable(
            name='gps',
            table='db_gps',
        ),
        migrations.AlterModelTable(
            name='list',
            table='db_list',
        ),
        migrations.AlterModelTable(
            name='organization',
            table='db_organization',
        ),
        migrations.AlterModelTable(
            name='organizationrole',
            table='db_organizationrole',
        ),
        migrations.AlterModelTable(
            name='organizationtype',
            table='db_organizationtype',
        ),
        migrations.AlterModelTable(
            name='project',
            table='db_project',
        ),
        migrations.AlterModelTable(
            name='projectboundary',
            table='db_projectboundary',
        ),
        migrations.AlterModelTable(
            name='projectlist',
            table='db_projectlist',
        ),
        migrations.AlterModelTable(
            name='site',
            table='db_site',
        ),
        migrations.AlterModelTable(
            name='species',
            table='db_species',
        ),
        migrations.AlterModelTable(
            name='speciesrel',
            table='db_speciesrel',
        ),
        migrations.AlterModelTable(
            name='statustype',
            table='db_statustype',
        ),
        migrations.AlterModelTable(
            name='task',
            table='db_task',
        ),
        migrations.AlterModelTable(
            name='tasksubtype',
            table='db_tasksubtype',
        ),
        migrations.AlterModelTable(
            name='tasktype',
            table='db_tasktype',
        ),
    ]
