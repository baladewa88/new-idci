# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idci', '0009_auto_20160923_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='papers',
            name='venue',
            field=models.ForeignKey(db_column='venue', to='idci.Venues', verbose_name='Source Title'),
        ),
    ]
