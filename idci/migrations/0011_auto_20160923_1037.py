# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idci', '0010_auto_20160923_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='papers',
            name='venue',
            field=models.ForeignKey(verbose_name='Source Title', to='idci.Venues', db_column='venues'),
        ),
    ]
