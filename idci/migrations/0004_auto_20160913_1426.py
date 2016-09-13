# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('idci', '0003_auto_20160907_1347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='citations',
            name='venuetype',
        ),
        migrations.RemoveField(
            model_name='papers',
            name='kodebuku',
        ),
        migrations.AlterField(
            model_name='citations',
            name='self',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='citations',
            name='venue',
            field=models.ForeignKey(default='', to='idci.Venues', db_column='venue', verbose_name='Source Title'),
        ),
        migrations.AlterField(
            model_name='papers',
            name='cluster',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='papers',
            name='crawldate',
            field=models.DateTimeField(db_column='crawlDate', default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='papers',
            name='ncites',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='papers',
            name='public',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='papers',
            name='selfcites',
            field=models.IntegerField(db_column='selfCites', default=0),
        ),
        migrations.AlterField(
            model_name='papers',
            name='tech',
            field=models.CharField(default='', blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='papers',
            name='version',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='papers',
            name='versiontime',
            field=models.DateTimeField(db_column='versionTime', default=django.utils.timezone.now),
        ),
    ]
