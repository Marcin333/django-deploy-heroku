# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_usercheckout_braintree_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraddress',
            name='country',
            field=models.CharField(default=datetime.datetime(2015, 10, 12, 13, 52, 14, 750512, tzinfo=utc), max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='useraddress',
            name='phone',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
    ]
