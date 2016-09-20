# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Papers(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    version = models.IntegerField(default=1)
    cluster = models.BigIntegerField(blank=True, null=True, default=0)
    title = models.CharField(max_length=255, blank=True, null=True)
    abstract = models.TextField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    venue = models.ForeignKey('Venues', db_column='venue', verbose_name="Source Title", default="")
    pages = models.CharField(max_length=20, blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    publisher = models.CharField(max_length=100, blank=True, null=True)
    pubaddress = models.CharField(db_column='pubAddress', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tech = models.CharField(max_length=100, blank=True, null=True, default="")
    public = models.IntegerField(default=1)
    ncites = models.IntegerField(default=0)
    versionname = models.CharField(db_column='versionName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    crawldate = models.DateTimeField(db_column='crawlDate', default=timezone.now)  # Field name made lowercase.
    repositoryid = models.CharField(db_column='repositoryID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    conversiontrace = models.CharField(db_column='conversionTrace', max_length=255, blank=True, null=True)  # Field name made lowercase.
    selfcites = models.IntegerField(db_column='selfCites', default=0)  # Field name made lowercase.
    versiontime = models.DateTimeField(db_column='versionTime', default=timezone.now)  # Field name made lowercase.
    #kodebuku = models.CharField(db_column='kodeBuku', max_length=10, verbose_name="ISSN / ISBN")  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'papers'

    def __str__(self):
        return self.title

class Citations(models.Model):
    #id = models.BigAutoField(primary_key=True)
    cluster = models.BigIntegerField(blank=True, null=True)
    authors = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    #venue = models.ForeignKey('Venues', db_column='venue', verbose_name="Source Title", default="")
    #venuetype = models.CharField(db_column='venueType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    venue = models.ForeignKey('Venues', db_column='venue', verbose_name="Source Title", default="")
    year = models.IntegerField(blank=True, null=True)
    pages = models.CharField(max_length=20, blank=True, null=True)
    editors = models.TextField(blank=True, null=True)
    publisher = models.CharField(max_length=100, blank=True, null=True)
    pubaddress = models.CharField(db_column='pubAddress', max_length=100, blank=True, null=True)  # Field name made lowercase.
    volume = models.IntegerField(blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    tech = models.CharField(max_length=100, blank=True, null=True)
    raw = models.TextField(blank=True, null=True)
    paperid = models.ForeignKey('Papers', db_column='paperid')
    self = models.IntegerField(default=0)

    class Meta:
        #managed = False
        db_table = 'citations'

    def __str__(self):
        return self.authors

class Affiliations(models.Model):
    #id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=1000, blank=True, null=True)
    address = models.CharField(max_length=1000, blank=True, null=True)
    url = models.CharField(max_length=500, blank=True, null=True)
    ncites = models.IntegerField(blank=True, null=True)
    nauthors = models.IntegerField(blank=True, null=True)
    ndocs = models.IntegerField(blank=True, null=True)

    class Meta:
       # managed = False
        db_table = 'affiliations'

    def __str__(self):
        return self.name
    
class AffiliasiRelasi(models.Model):
    #id = models.BigAutoField(primary_key=True)
    idaffiliasi = models.ForeignKey('Affiliations', db_column='idAffiliasi')  # Field name made lowercase.
    idpaper = models.ForeignKey('Papers', db_column='idpaper')

    class Meta:
        #managed = False
        db_table = 'affiliasi_relasi'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        #managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        #managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        #managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        #managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        #managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        #managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthorBasedata(models.Model):
    #id = models.BigAutoField(primary_key=True)
    namalengkap = models.CharField(max_length=55)
    affiliasi = models.TextField()
    alamat_affiliasi = models.TextField()
    jumlahdokumen = models.IntegerField(blank=True, null=True, default=0)
    
    class Meta:
        #managed = False
        db_table = 'author_basedata'
        
    def __str__(self):
        return self.namalengkap

class Authors(models.Model):
    #id = models.BigAutoField(primary_key=True)
    cluster = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=100)
    affil = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    ord = models.IntegerField(verbose_name="Author's Order")
    paperid = models.ForeignKey('Papers', db_column='paperid')

    class Meta:
        #managed = False
        db_table = 'authors'

    def __str__(self):
        return self.name
    
class Authorsaffil(models.Model):
    #id = models.BigAutoField(primary_key=True)
    authors_id = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=500, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'authorsaffil'

        
class AuthorsRelasi(models.Model):
    #id = models.BigAutoField(primary_key=True)
    idbasedata = models.ForeignKey('AuthorBasedata', db_column='idBasedata')
    idauthors = models.ForeignKey('Authors', db_column='idAuthors')

    class Meta:
        #managed = False
        db_table = 'authors_relasi'

class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        #managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        #managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        #managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        #managed = False
        db_table = 'django_session'


class Keywords(models.Model):
    #id = models.BigAutoField(primary_key=True)
    keyword = models.CharField(max_length=100)
    paperid = models.ForeignKey('Papers', db_column='paperid')

    class Meta:
        #managed = False
        db_table = 'keywords'

    def __str__(self):
        return self.keyword

class Urls(models.Model):
    #id = models.BigAutoField(primary_key=True)
    url = models.CharField(max_length=255)
    paperid = models.ForeignKey(Papers, db_column='paperid')

    class Meta:
        #managed = False
        db_table = 'urls'

    def __str__(self):
        return self.url
    
class Venues(models.Model):
    #id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=500, blank=True, null=True)
    url = models.CharField(max_length=500, blank=True, null=True)
    editor = models.CharField(max_length=500, blank=True, null=True)
    issn = models.CharField(max_length=50, blank=True, null=True)
    publisher = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    contact_info = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    language = models.CharField(max_length=20, blank=True, null=True)
    halflife_cited = models.FloatField(blank=True, null=True)
    halflife_citing = models.FloatField(blank=True, null=True)
    impact_factor = models.FloatField(blank=True, null=True)
    immediciacy = models.FloatField(blank=True, null=True)
    hindex = models.FloatField(blank=True, null=True)
    selfcites = models.IntegerField(blank=True, null=True)
    ndocs = models.IntegerField(blank=True, null=True)
    ncites = models.IntegerField(blank=True, null=True)
    nauthors = models.IntegerField(blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'venues'

    def __str__(self):
        return self.name

class MergingAffiliasi(models.Model):
    #id = models.BigIntegerField(primary_key=True)
    judulpaper = models.TextField(db_column='judulPaper')  # Field name made lowercase.
    namapenulis = models.TextField(db_column='namaPenulis')  # Field name made lowercase.
    namaaffiliasi = models.TextField(db_column='namaAffiliasi')  # Field name made lowercase.
    status = models.TextField()

    class Meta:
        #managed = False
        db_table = 'merging_affiliasi'
