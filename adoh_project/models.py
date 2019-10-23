# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AppStudent(models.Model):
    sb1 = models.IntegerField()
    sb2 = models.IntegerField()
    total = models.CharField(max_length=20)
    sb3 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_student'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class BlogComment(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    body = models.TextField()
    created = models.DateTimeField()
    updated = models.DateTimeField()
    active = models.IntegerField()
    post = models.ForeignKey('BlogPost', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'blog_comment'


class BlogPost(models.Model):
    tittle = models.CharField(max_length=256)
    slug = models.CharField(max_length=256)
    body = models.TextField()
    publish = models.DateTimeField()
    created = models.DateTimeField()
    updated = models.DateTimeField()
    status = models.CharField(max_length=20)
    author = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'blog_post'


class Dj(models.Model):
    name = models.CharField(max_length=10, blank=True, null=True)
    job = models.CharField(max_length=20, blank=True, null=True)
    sal = models.FloatField(blank=True, null=True)
    phno = models.IntegerField(blank=True, null=True)
    id = models.IntegerField()
    sb1 = models.IntegerField()
    sb2 = models.IntegerField()
    total = models.CharField(max_length=20)
    sb3 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dj'


class Dj1(models.Model):
    name = models.CharField(max_length=10, blank=True, null=True)
    job = models.CharField(max_length=20, blank=True, null=True)
    sal = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dj1'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class T1(models.Model):
    name = models.TextField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    sal = models.FloatField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    deptname = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't1'


class T2(models.Model):
    name = models.TextField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    sal = models.FloatField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't2'


class T3(models.Model):
    id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=10, blank=True, null=True)
    deptname = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't3'


class TestappChild(models.Model):
    parent_ptr = models.ForeignKey('TestappParent', models.DO_NOTHING, primary_key=True)
    fd3 = models.CharField(max_length=120)
    fd4 = models.CharField(max_length=120)

    class Meta:
        managed = False
        db_table = 'testapp_child'


class TestappContactinfo(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=254)
    address = models.CharField(max_length=120)

    class Meta:
        managed = False
        db_table = 'testapp_contactinfo'


class TestappParent(models.Model):
    fd1 = models.CharField(max_length=120)
    fs2 = models.CharField(max_length=120)

    class Meta:
        managed = False
        db_table = 'testapp_parent'


class TestappStudent(models.Model):
    contactinfo_ptr = models.ForeignKey(TestappContactinfo, models.DO_NOTHING, primary_key=True)
    rollno = models.IntegerField()
    marks = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'testapp_student'


class TestappStudent2(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=254)
    address = models.CharField(max_length=120)
    rollno = models.IntegerField()
    marks = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'testapp_student2'


class TestappSubchild(models.Model):
    child_ptr = models.ForeignKey(TestappChild, models.DO_NOTHING, primary_key=True)
    fd5 = models.CharField(max_length=120)

    class Meta:
        managed = False
        db_table = 'testapp_subchild'


class TestappTeacher(models.Model):
    contactinfo_ptr = models.ForeignKey(TestappContactinfo, models.DO_NOTHING, primary_key=True)
    subject = models.CharField(max_length=100)
    sal = models.FloatField()

    class Meta:
        managed = False
        db_table = 'testapp_teacher'


class TestappTeacher2(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=254)
    address = models.CharField(max_length=120)
    subject = models.CharField(max_length=100)
    sal = models.FloatField()

    class Meta:
        managed = False
        db_table = 'testapp_teacher2'
