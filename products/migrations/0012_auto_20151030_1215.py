# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20151029_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='wish_list',
            field=models.ForeignKey(to='products.Variation'),
        ),
    ]
