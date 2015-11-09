# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0010_auto_20150922_2135'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='tax_total',
            field=models.DecimalField(default=1, max_digits=40, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cart',
            name='total',
            field=models.DecimalField(default=1, max_digits=40, decimal_places=2),
            preserve_default=False,
        ),
    ]
