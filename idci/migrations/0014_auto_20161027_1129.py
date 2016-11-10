# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idci', '0013_auto_20161027_1105'),
    ]

    operations = [
        migrations.AddField(
            model_name='mergingauthor',
            name='email',
            field=models.TextField(default='', db_column='email_author'),
        ),
        migrations.AlterField(
            model_name='affiliasirelasi',
            name='idpaper',
            field=models.ForeignKey(to='idci.Papers', db_column='idPaper'),
        ),
    ]
