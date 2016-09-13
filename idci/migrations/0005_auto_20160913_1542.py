# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idci', '0004_auto_20160913_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authors',
            name='ord',
            field=models.IntegerField(verbose_name="Author's Order"),
        ),
    ]
