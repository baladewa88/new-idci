# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idci', '0006_auto_20160919_1110'),
    ]

    operations = [
        migrations.AddField(
            model_name='authorbasedata',
            name='jumlahdokumen',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
