# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20151030_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='wish_list',
            field=models.ForeignKey(blank=True, to='products.Variation', null=True),
        ),
    ]
