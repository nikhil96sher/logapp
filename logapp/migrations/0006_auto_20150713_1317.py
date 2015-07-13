# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logapp', '0005_auto_20150713_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiledata',
            name='contact',
            field=models.CharField(max_length=15),
        ),
    ]
