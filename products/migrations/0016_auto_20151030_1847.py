# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_auto_20151030_1302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='wish_list',
        ),
        migrations.AddField(
            model_name='wishlist',
            name='wish_list',
            field=models.ManyToManyField(to='products.Variation'),
        ),
    ]
