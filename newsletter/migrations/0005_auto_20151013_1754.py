# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0004_auto_20151013_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='condition',
            name='text_field',
            field=models.TextField(max_length=50, null=True, blank=True),
        ),
    ]
