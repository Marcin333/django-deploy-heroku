# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0005_auto_20151013_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='condition',
            name='text_field',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
