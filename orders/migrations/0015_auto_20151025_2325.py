# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_auto_20151013_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
