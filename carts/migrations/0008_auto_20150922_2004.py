# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0007_cartitem_line_item_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='line_item_total',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=2),
        ),
    ]
