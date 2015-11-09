# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0016_auto_20151030_1847'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wish',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='WishItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('item', models.ForeignKey(to='products.Variation')),
                ('wish', models.ForeignKey(to='products.Wish')),
            ],
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='user',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='wish_list',
        ),
        migrations.DeleteModel(
            name='WishList',
        ),
        migrations.AddField(
            model_name='wish',
            name='items',
            field=models.ManyToManyField(to='products.Variation', through='products.WishItem'),
        ),
        migrations.AddField(
            model_name='wish',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
