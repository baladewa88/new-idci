# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idci', '0008_auto_20160921_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='papers',
            name='publisher',
            field=models.CharField(null=True, blank=True, max_length=255),
        ),
    ]
