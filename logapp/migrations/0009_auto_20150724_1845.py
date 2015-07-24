# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import logapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('logapp', '0008_auto_20150724_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiledata',
            name='branch',
            field=models.CharField(max_length=200, choices=[(b'CSE', b'CSE'), (b'ECE', b'ECE'), (b'CE', b'CE'), (b'ME', b'ME')]),
        ),
        migrations.AlterField(
            model_name='profiledata',
            name='contact',
            field=models.BigIntegerField(validators=[logapp.models.contact_range]),
        ),
        migrations.AlterField(
            model_name='profiledata',
            name='enrollment',
            field=models.IntegerField(validators=[logapp.models.enroll_range]),
        ),
    ]
