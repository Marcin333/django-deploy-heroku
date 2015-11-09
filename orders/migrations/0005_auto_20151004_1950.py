# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_useraddress'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useraddress',
            old_name='address_type',
            new_name='type',
        ),
    ]
