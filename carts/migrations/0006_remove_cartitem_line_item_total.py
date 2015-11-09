# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0005_auto_20150922_1944'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='line_item_total',
        ),
    ]
