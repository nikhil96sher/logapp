# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logapp', '0009_auto_20150724_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiledata',
            name='contact',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='profiledata',
            name='enrollment',
            field=models.IntegerField(),
        ),
    ]
