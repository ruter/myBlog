# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_bloginfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('userName', models.CharField(max_length=20, verbose_name='Username')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('subject', models.CharField(max_length=100, verbose_name='Subject')),
                ('message', models.TextField(verbose_name='Message')),
                ('submitDate', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
            ],
            options={
                'ordering': ['-submitDate'],
            },
        ),
    ]
