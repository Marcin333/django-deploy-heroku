# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0003_conditions'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Conditions',
            new_name='Condition',
        ),
    ]
