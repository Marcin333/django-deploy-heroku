# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_orders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='billing_address',
            field=models.ForeignKey(related_name='billing_address', to='orders.UserAddress', null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='shipping_address',
            field=models.ForeignKey(related_name='shipping_address', to='orders.UserAddress', null=True),
        ),
    ]
