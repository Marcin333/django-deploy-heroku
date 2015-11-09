# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0007_newsletter'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsletter',
            options={'ordering': ['-timestamp']},
        ),
    ]
