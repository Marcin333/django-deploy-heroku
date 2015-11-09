# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0015_auto_20151025_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='type',
            field=models.CharField(default=b'billing', max_length=120, choices=[(b'billing', b'Billing'), (b'shipping', b'Shipping')]),
        ),
    ]
