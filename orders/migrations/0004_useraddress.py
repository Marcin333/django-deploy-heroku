# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20151004_0952'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address_type', models.CharField(max_length=120, choices=[(b'billing', b'Billing'), (b'shipping', b'Shipping')])),
                ('street', models.CharField(max_length=120)),
                ('city', models.CharField(max_length=120)),
                ('state', models.CharField(max_length=120, null=True, blank=True)),
                ('post_code', models.CharField(max_length=120)),
                ('user', models.ForeignKey(to='orders.UserCheckout')),
            ],
        ),
    ]
