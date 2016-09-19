# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idci', '0005_auto_20160913_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='affiliasirelasi',
            name='idaffiliasi',
            field=models.ForeignKey(to='idci.Affiliations', db_column='idAffiliasi'),
        ),
        migrations.AlterField(
            model_name='affiliasirelasi',
            name='idpaper',
            field=models.ForeignKey(to='idci.Papers', db_column='idpaper'),
        ),
    ]
