# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idci', '0007_authorbasedata_jumlahdokumen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authorsrelasi',
            name='idauthors',
            field=models.ForeignKey(to='idci.Authors', db_column='idAuthors'),
        ),
        migrations.AlterField(
            model_name='authorsrelasi',
            name='idbasedata',
            field=models.ForeignKey(to='idci.AuthorBasedata', db_column='idBasedata'),
        ),
        migrations.AlterField(
            model_name='citations',
            name='number',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='citations',
            name='volume',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
    ]
