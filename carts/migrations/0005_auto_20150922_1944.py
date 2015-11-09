# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0004_cartitem_line_total'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='line_total',
            new_name='line_item_total',
        ),
    ]
