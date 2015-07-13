# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('logapp', '0003_auto_20150713_1303'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('branch', models.CharField(max_length=200, choices=[(b'CSE', b'Computer Science and Engineering'), (b'ECE', b'ECE'), (b'CE', b'CE'), (b'ME', b'ME')])),
                ('enrollment', models.IntegerField()),
                ('gender', models.CharField(default=b'Male', max_length=6, choices=[(b'Male', b'Male'), (b'Female', b'Female')])),
                ('dob', models.DateField()),
                ('contact', models.IntegerField(max_length=10)),
                ('address', models.CharField(max_length=200)),
                ('about', models.CharField(max_length=300)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='profiledata',
            name='user',
        ),
        migrations.DeleteModel(
            name='ProfileData',
        ),
    ]
