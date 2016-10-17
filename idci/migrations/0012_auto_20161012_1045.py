# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idci', '0011_auto_20160923_1037'),
    ]

    operations = [
        migrations.CreateModel(
            name='MergingAuthor',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('judulpaper', models.TextField(db_column='judulPaper')),
                ('namapenulis', models.TextField(db_column='namaPenulis')),
                ('status', models.TextField()),
                ('penulisbasedata', models.TextField(db_column='penulisBasedata')),
            ],
            options={
                'managed': False,
                'db_table': 'merging_author',
            },
        ),
        migrations.AlterField(
            model_name='mergingaffiliasi',
            name='namaaffiliasi',
            field=models.CharField(db_column='namaAffiliasi', max_length=255),
        ),
        migrations.AlterField(
            model_name='mergingaffiliasi',
            name='namapenulis',
            field=models.CharField(db_column='namaPenulis', max_length=255),
        ),
        migrations.AlterField(
            model_name='papers',
            name='venue',
            field=models.ForeignKey(verbose_name='Source Title', to='idci.Venues', db_column='venue'),
        ),
    ]
