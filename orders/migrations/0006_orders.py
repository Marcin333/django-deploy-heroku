# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0013_cart_tax_percentage'),
        ('orders', '0005_auto_20151004_1950'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('shipping_total_price', models.DecimalField(default=5.99, max_digits=30, decimal_places=2)),
                ('order_total', models.DecimalField(max_digits=30, decimal_places=2)),
                ('billing_address', models.ForeignKey(related_name='billing_address', to='orders.UserAddress')),
                ('cart', models.ForeignKey(to='carts.Cart')),
                ('shipping_address', models.ForeignKey(related_name='shipping_address', to='orders.UserAddress')),
                ('user', models.ForeignKey(to='orders.UserCheckout')),
            ],
        ),
    ]
