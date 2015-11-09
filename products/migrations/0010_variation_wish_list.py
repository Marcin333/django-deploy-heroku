# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_productfeatured_text_css_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='variation',
            name='wish_list',
            field=models.BooleanField(default=False),
        ),
    ]
