# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import products.models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20150918_1239'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductFeatured',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=products.models.image_upload_featured)),
                ('title', models.CharField(max_length=120, null=True, blank=True)),
                ('text', models.CharField(max_length=120, null=True, blank=True)),
                ('text_right', models.BooleanField(default=False)),
                ('show_price', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='default',
            field=models.ForeignKey(related_name='default_category', blank=True, to='products.Category', null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(default=datetime.datetime(2015, 9, 19, 19, 23, 15, 486527, tzinfo=utc), max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productfeatured',
            name='product',
            field=models.ForeignKey(to='products.Product'),
        ),
    ]
