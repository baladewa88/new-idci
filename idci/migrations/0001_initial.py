# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AffiliasiRelasi',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('idaffiliasi', models.BigIntegerField(db_column='idAffiliasi')),
                ('idpaper', models.CharField(db_column='idPaper', max_length=100)),
            ],
            options={
                'db_table': 'affiliasi_relasi',
            },
        ),
        migrations.CreateModel(
            name='Affiliations',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(blank=True, null=True, max_length=1000)),
                ('address', models.CharField(blank=True, null=True, max_length=1000)),
                ('url', models.CharField(blank=True, null=True, max_length=500)),
                ('ncites', models.IntegerField(blank=True, null=True)),
                ('nauthors', models.IntegerField(blank=True, null=True)),
                ('ndocs', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'affiliations',
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(unique=True, max_length=80)),
            ],
            options={
                'db_table': 'auth_group',
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('group', models.ForeignKey(to='idci.AuthGroup', to_field=django.db.models.deletion.DO_NOTHING)),
            ],
            options={
                'db_table': 'auth_group_permissions',
            },
        ),
        migrations.CreateModel(
            name='AuthorBasedata',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('namalengkap', models.CharField(max_length=55)),
                ('affiliasi', models.TextField()),
                ('alamat_affiliasi', models.TextField()),
            ],
            options={
                'db_table': 'author_basedata',
            },
        ),
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('cluster', models.BigIntegerField(blank=True, null=True)),
                ('name', models.CharField(max_length=100)),
                ('affil', models.CharField(blank=True, null=True, max_length=255)),
                ('address', models.CharField(blank=True, null=True, max_length=255)),
                ('email', models.CharField(blank=True, null=True, max_length=100)),
                ('ord', models.IntegerField()),
            ],
            options={
                'db_table': 'authors',
            },
        ),
        migrations.CreateModel(
            name='Authorsaffil',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('authors_id', models.BigIntegerField(blank=True, null=True)),
                ('name', models.CharField(blank=True, null=True, max_length=500)),
                ('address', models.CharField(blank=True, null=True, max_length=500)),
            ],
            options={
                'db_table': 'authorsaffil',
            },
        ),
        migrations.CreateModel(
            name='AuthorsRelasi',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('idbasedata', models.BigIntegerField(db_column='idBasedata')),
                ('idauthors', models.BigIntegerField(db_column='idAuthors')),
            ],
            options={
                'db_table': 'authors_relasi',
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(unique=True, max_length=150)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('group', models.ForeignKey(to='idci.AuthGroup', to_field=django.db.models.deletion.DO_NOTHING)),
                ('user', models.ForeignKey(to='idci.AuthUser', to_field=django.db.models.deletion.DO_NOTHING)),
            ],
            options={
                'db_table': 'auth_user_groups',
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('permission', models.ForeignKey(to='idci.AuthPermission', to_field=django.db.models.deletion.DO_NOTHING)),
                ('user', models.ForeignKey(to='idci.AuthUser', to_field=django.db.models.deletion.DO_NOTHING)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
            },
        ),
        migrations.CreateModel(
            name='Citations',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('cluster', models.BigIntegerField(blank=True, null=True)),
                ('authors', models.TextField(blank=True, null=True)),
                ('title', models.CharField(blank=True, null=True, max_length=255)),
                ('venue', models.CharField(blank=True, null=True, max_length=255)),
                ('venuetype', models.CharField(blank=True, db_column='venueType', null=True, max_length=20)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('pages', models.CharField(blank=True, null=True, max_length=20)),
                ('editors', models.TextField(blank=True, null=True)),
                ('publisher', models.CharField(blank=True, null=True, max_length=100)),
                ('pubaddress', models.CharField(blank=True, db_column='pubAddress', null=True, max_length=100)),
                ('volume', models.IntegerField(blank=True, null=True)),
                ('number', models.IntegerField(blank=True, null=True)),
                ('tech', models.CharField(blank=True, null=True, max_length=100)),
                ('raw', models.TextField(blank=True, null=True)),
                ('self', models.IntegerField()),
            ],
            options={
                'db_table': 'citations',
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(serialize=False, primary_key=True, max_length=40)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
            },
        ),
        migrations.CreateModel(
            name='Keywords',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('keyword', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'keywords',
            },
        ),
        migrations.CreateModel(
            name='Papers',
            fields=[
                ('id', models.CharField(serialize=False, primary_key=True, max_length=100)),
                ('version', models.IntegerField()),
                ('cluster', models.BigIntegerField(blank=True, null=True)),
                ('title', models.CharField(blank=True, null=True, max_length=255)),
                ('abstract', models.TextField(blank=True, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('venue', models.CharField(blank=True, null=True, max_length=100)),
                ('pages', models.CharField(blank=True, null=True, max_length=20)),
                ('volume', models.IntegerField(blank=True, null=True)),
                ('number', models.IntegerField(blank=True, null=True)),
                ('publisher', models.CharField(blank=True, null=True, max_length=100)),
                ('pubaddress', models.CharField(blank=True, db_column='pubAddress', null=True, max_length=100)),
                ('tech', models.CharField(blank=True, null=True, max_length=100)),
                ('public', models.IntegerField()),
                ('ncites', models.IntegerField()),
                ('versionname', models.CharField(blank=True, db_column='versionName', null=True, max_length=20)),
                ('crawldate', models.DateTimeField(db_column='crawlDate')),
                ('repositoryid', models.CharField(blank=True, db_column='repositoryID', null=True, max_length=15)),
                ('conversiontrace', models.CharField(blank=True, db_column='conversionTrace', null=True, max_length=255)),
                ('selfcites', models.IntegerField(db_column='selfCites')),
                ('versiontime', models.DateTimeField(db_column='versionTime')),
                ('kodebuku', models.CharField(db_column='kodeBuku', max_length=10)),
            ],
            options={
                'db_table': 'papers',
            },
        ),
        migrations.CreateModel(
            name='Urls',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('url', models.CharField(max_length=255)),
                ('paperid', models.ForeignKey(to='idci.Papers', to_field=django.db.models.deletion.DO_NOTHING, db_column='paperid')),
            ],
            options={
                'db_table': 'urls',
            },
        ),
        migrations.CreateModel(
            name='Venues',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(blank=True, null=True, max_length=500)),
                ('url', models.CharField(blank=True, null=True, max_length=500)),
                ('editor', models.CharField(blank=True, null=True, max_length=500)),
                ('issn', models.CharField(blank=True, null=True, max_length=50)),
                ('publisher', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('contact_info', models.TextField(blank=True, null=True)),
                ('type', models.CharField(blank=True, null=True, max_length=20)),
                ('language', models.CharField(blank=True, null=True, max_length=20)),
                ('halflife_cited', models.FloatField(blank=True, null=True)),
                ('halflife_citing', models.FloatField(blank=True, null=True)),
                ('impact_factor', models.FloatField(blank=True, null=True)),
                ('immediciacy', models.FloatField(blank=True, null=True)),
                ('hindex', models.FloatField(blank=True, null=True)),
                ('selfcites', models.IntegerField(blank=True, null=True)),
                ('ndocs', models.IntegerField(blank=True, null=True)),
                ('ncites', models.IntegerField(blank=True, null=True)),
                ('nauthors', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'venues',
            },
        ),
        migrations.AddField(
            model_name='keywords',
            name='paperid',
            field=models.ForeignKey(to='idci.Papers', to_field=django.db.models.deletion.DO_NOTHING, db_column='paperid'),
        ),
        migrations.AlterUniqueTogether(
            name='djangocontenttype',
            unique_together=set([('app_label', 'model')]),
        ),
        migrations.AddField(
            model_name='djangoadminlog',
            name='content_type',
            field=models.ForeignKey(to_field=django.db.models.deletion.DO_NOTHING, to='idci.DjangoContentType', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='djangoadminlog',
            name='user',
            field=models.ForeignKey(to='idci.AuthUser', to_field=django.db.models.deletion.DO_NOTHING),
        ),
        migrations.AddField(
            model_name='citations',
            name='paperid',
            field=models.ForeignKey(to='idci.Papers', to_field=django.db.models.deletion.DO_NOTHING, db_column='paperid'),
        ),
        migrations.AddField(
            model_name='authpermission',
            name='content_type',
            field=models.ForeignKey(to='idci.DjangoContentType', to_field=django.db.models.deletion.DO_NOTHING),
        ),
        migrations.AddField(
            model_name='authors',
            name='paperid',
            field=models.ForeignKey(to='idci.Papers', to_field=django.db.models.deletion.DO_NOTHING, db_column='paperid'),
        ),
        migrations.AddField(
            model_name='authgrouppermissions',
            name='permission',
            field=models.ForeignKey(to='idci.AuthPermission', to_field=django.db.models.deletion.DO_NOTHING),
        ),
        migrations.AlterUniqueTogether(
            name='authuseruserpermissions',
            unique_together=set([('user', 'permission')]),
        ),
        migrations.AlterUniqueTogether(
            name='authusergroups',
            unique_together=set([('user', 'group')]),
        ),
        migrations.AlterUniqueTogether(
            name='authpermission',
            unique_together=set([('content_type', 'codename')]),
        ),
        migrations.AlterUniqueTogether(
            name='authgrouppermissions',
            unique_together=set([('group', 'permission')]),
        ),
    ]
