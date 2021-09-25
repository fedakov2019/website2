# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Books(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    author = models.TextField(db_column='Author', blank=True, null=True)  # Field name made lowercase.
    price = models.IntegerField(db_column='Price')  # Field name made lowercase.
    opis = models.TextField(db_column='Opis', blank=True, null=True)  # Field name made lowercase.
    discriminator = models.CharField(db_column='Discriminator', max_length=128)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Books'


class Menuitems(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    header = models.TextField(db_column='Header', blank=True, null=True)  # Field name made lowercase.
    url = models.TextField(db_column='Url', blank=True, null=True)  # Field name made lowercase.
    order = models.IntegerField(db_column='Order', blank=True, null=True)  # Field name made lowercase.
    parentid = models.ForeignKey('self', models.DO_NOTHING, db_column='ParentId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MenuItems'


class Players(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    position = models.TextField(db_column='Position', blank=True, null=True)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age')  # Field name made lowercase.
    teamid = models.ForeignKey('Teams', models.DO_NOTHING, db_column='TeamId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Players'


class Table(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    id1 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Table'


class Table1(models.Model):
    id1 = models.AutoField(primary_key=True)
    opis = models.CharField(db_column='Opis', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Table_1'


class Table2(models.Model):
    name = models.CharField(db_column='Name', max_length=10, blank=True, null=True)  # Field name made lowercase.
    name1 = models.CharField(db_column='Name1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    zn = models.IntegerField(db_column='Zn', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Table_2'


class Teams(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    coach = models.TextField(db_column='Coach', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Teams'


class User(models.Model):
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    age = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table ationhistory(models.Model):
    migrationid = models.CharField(db_column='MigrationId', primary_key=True, max_length=150)  # Field name made lowercase.
    contextkey = models.CharField(db_column='ContextKey', max_length=300)  # Field name made lowercase.
    model = models.BinaryField(db_column='Model')  # Field name made lowercase.
    productversion = models.CharField(db_column='ProductVersion', max_length=32)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '__MigrationHistory'
        unique_together = (('migrationid', 'contextkey'),)


class Outcome(models.Model):
    code = models.IntegerField()
    point = models.SmallIntegerField()
    out = models.DecimalField(max_digits=10, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'outcome'


class Utb(models.Model):
    b_datetime = models.DateTimeField()
    b_q_id = models.IntegerField(db_column='B_Q_ID')  # Field name made lowercase.
    b_v_id = models.IntegerField(db_column='B_V_ID')  # Field name made lowercase.
    b_vol = models.IntegerField(db_column='B_VOL')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'utb'
