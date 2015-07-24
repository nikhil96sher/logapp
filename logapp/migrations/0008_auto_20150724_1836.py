# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logapp', '0007_uploads'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiledata',
            name='contact',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='uploads',
            name='cover',
            field=models.ImageField(default=b'/cover/default_cover.jpg', upload_to=b'./cover/'),
        ),
        migrations.AlterField(
            model_name='uploads',
            name='profile',
            field=models.ImageField(default=b'/profile/default_profile.jpg', upload_to=b'./profile/'),
        ),
    ]
