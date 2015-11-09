# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0008_auto_20151025_2325'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='message',
            field=models.TextField(default=datetime.datetime(2015, 11, 8, 17, 42, 15, 304859, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
