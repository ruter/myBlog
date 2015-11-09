# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_auto_20151107_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloginfo',
            name='domain',
            field=models.CharField(max_length=20, null=True, verbose_name='Domain', blank=True),
        ),
    ]
