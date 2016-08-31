# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idci', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MergingAffiliasi',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('judulpaper', models.TextField(db_column='judulPaper')),
                ('namapenulis', models.TextField(db_column='namaPenulis')),
                ('namaaffiliasi', models.TextField(db_column='namaAffiliasi')),
                ('status', models.TextField()),
            ],
            options={
                'db_table': 'merging_affiliasi',
            },
        ),
    ]
