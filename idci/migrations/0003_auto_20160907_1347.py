# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idci', '0002_mergingaffiliasi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authors',
            name='paperid',
            field=models.ForeignKey(db_column='paperid', to='idci.Papers'),
        ),
        migrations.AlterField(
            model_name='citations',
            name='paperid',
            field=models.ForeignKey(db_column='paperid', to='idci.Papers'),
        ),
        migrations.AlterField(
            model_name='keywords',
            name='paperid',
            field=models.ForeignKey(db_column='paperid', to='idci.Papers'),
        ),
        migrations.AlterField(
            model_name='papers',
            name='kodebuku',
            field=models.CharField(max_length=10, db_column='kodeBuku', verbose_name='ISSN / ISBN'),
        ),
        migrations.AlterField(
            model_name='papers',
            name='venue',
            field=models.ForeignKey(db_column='venue', verbose_name='Source Title', default='', to='idci.Venues'),
        ),
        migrations.AlterField(
            model_name='urls',
            name='paperid',
            field=models.ForeignKey(db_column='paperid', to='idci.Papers'),
        ),
    ]
