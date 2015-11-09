# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_auto_20150910_1339'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conditions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, null=True, blank=True)),
                ('text_field', models.CharField(max_length=50, null=True, blank=True)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
    ]
