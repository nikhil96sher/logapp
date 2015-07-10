# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('logapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('branch', models.CharField(max_length=200)),
                ('enrollment', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=6)),
                ('dob', models.DateField()),
                ('email', models.EmailField(max_length=75)),
                ('contact', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=200)),
                ('about', models.CharField(max_length=300)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
