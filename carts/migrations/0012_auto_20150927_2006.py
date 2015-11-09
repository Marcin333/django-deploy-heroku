# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0011_auto_20150927_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='subtotal',
            field=models.DecimalField(default=0.0, max_digits=40, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='cart',
            name='tax_total',
            field=models.DecimalField(default=0.0, max_digits=40, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='cart',
            name='total',
            field=models.DecimalField(default=0.0, max_digits=40, decimal_places=2),
        ),
    ]
