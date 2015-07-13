# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logapp', '0002_auto_20150710_1911'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profiledata',
            name='email',
        ),
        migrations.AlterField(
            model_name='profiledata',
            name='branch',
            field=models.CharField(max_length=200, choices=[(b'CSE', b'Computer Science and Engineering'), (b'ECE', b'ECE'), (b'CE', b'CE'), (b'ME', b'ME')]),
        ),
        migrations.AlterField(
            model_name='profiledata',
            name='contact',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='profiledata',
            name='enrollment',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='profiledata',
            name='gender',
            field=models.CharField(default=b'Male', max_length=6, choices=[(b'Male', b'Male'), (b'Female', b'Female')]),
        ),
    ]
