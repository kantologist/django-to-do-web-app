# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0008_auto_20160910_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='list',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
    ]
