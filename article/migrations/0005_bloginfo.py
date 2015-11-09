# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_auto_20151105_2021'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('blogName', models.CharField(max_length=20, verbose_name='Blog Name')),
                ('logo', models.CharField(max_length=100, null=True, verbose_name='Logo', blank=True)),
                ('avatar', models.CharField(max_length=100, null=True, verbose_name='Avatar', blank=True)),
                ('oName', models.CharField(max_length=20, null=True, verbose_name='Name', blank=True)),
                ('intro', models.TextField(null=True, verbose_name='Intro', blank=True)),
            ],
        ),
    ]
