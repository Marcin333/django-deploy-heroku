# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0012_auto_20150927_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='tax_percentage',
            field=models.DecimalField(default=0.2, max_digits=10, decimal_places=5),
        ),
    ]
