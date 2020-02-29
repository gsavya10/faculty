from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


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
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class Departments(models.Model):
    department_code = models.IntegerField(primary_key=True)
    department_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'departments'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()

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


class Factemp(models.Model):
    name = models.CharField(max_length=28, blank=True, null=True)
    department = models.CharField(max_length=40, blank=True, null=True)
    designation = models.CharField(max_length=20, blank=True, null=True)
    facid = models.CharField(max_length=5, blank=True, null=True)
    specialization = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'factemp'


class FacultyCurrentData(models.Model):
    facultyid = models.AutoField(primary_key=True)
    drupal_id = models.IntegerField()
    name = models.CharField(max_length=30)
    designation = models.CharField(max_length=20)
    interest = models.TextField(blank=True, null=True)
    department = models.CharField(max_length=100)
    email = models.CharField(max_length=5000, blank=True, null=True)
    phone = models.CharField(max_length=256, blank=True, null=True)
    office = models.CharField(max_length=20, blank=True, null=True)
    officeaddress = models.CharField(max_length=5000, blank=True, null=True)
    extlinks = models.CharField(max_length=5000, blank=True, null=True)
    profile = models.TextField(blank=True, null=True)
    edit = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField()
    approve_ipaddress = models.CharField(max_length=50)
    approve_by = models.CharField(max_length=50)
    courses = models.TextField(blank=True, null=True)
    phds = models.TextField(blank=True, null=True)
    workshops = models.TextField(blank=True, null=True)
    projects = models.TextField(blank=True, null=True)
    awards = models.TextField(blank=True, null=True)
    responsibility = models.TextField(blank=True, null=True)
    publications = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'faculty_current_data'


class FacultyCurrentData33(models.Model):
    facultyid = models.AutoField(primary_key=True)
    drupal_id = models.IntegerField()
    name = models.CharField(max_length=30)
    designation = models.CharField(max_length=20)
    interest = models.TextField()
    department = models.CharField(max_length=100)
    email = models.CharField(max_length=5000, blank=True, null=True)
    phone = models.CharField(max_length=256, blank=True, null=True)
    office = models.CharField(max_length=20)
    officeaddress = models.CharField(max_length=5000)
    extlinks = models.CharField(max_length=5000)
    profile = models.TextField(blank=True, null=True)
    edit = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField()
    approve_ipaddress = models.CharField(max_length=50)
    approve_by = models.CharField(max_length=50)
    courses = models.TextField(blank=True, null=True)
    phds = models.TextField(blank=True, null=True)
    workshops = models.TextField(blank=True, null=True)
    projects = models.TextField(blank=True, null=True)
    awards = models.TextField(blank=True, null=True)
    responsibility = models.TextField(blank=True, null=True)
    publications = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'faculty_current_data33'


class FacultyDesignation(models.Model):
    designation_code = models.IntegerField()
    designation_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'faculty_designation'


class FacultyDetails(models.Model):
    name = models.CharField(max_length=30)
    designation_name = models.CharField(max_length=100)
    department_name = models.CharField(max_length=100)
    email = models.CharField(max_length=5000, blank=True, null=True)
    phone = models.CharField(max_length=256, blank=True, null=True)
    office = models.CharField(max_length=20, blank=True, null=True)
    officeaddress = models.CharField(max_length=5000, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'faculty_details'


class FacultyPendingData(models.Model):
    facultyid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    interest = models.TextField()
    phone = models.CharField(max_length=256)
    office = models.CharField(max_length=100)
    officeaddress = models.CharField(max_length=5000)
    extlinks = models.CharField(max_length=5000)
    email = models.CharField(max_length=100)
    profile = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    review = models.IntegerField(blank=True, null=True)
    saved = models.IntegerField()
    ipaddress = models.CharField(max_length=50)
    timestamp = models.DateTimeField()
    courses = models.TextField(blank=True, null=True)
    phds = models.TextField(blank=True, null=True)
    workshops = models.TextField(blank=True, null=True)
    projects = models.TextField(blank=True, null=True)
    awards = models.TextField(blank=True, null=True)
    responsibility = models.TextField(blank=True, null=True)
    publications = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'faculty_pending_data'


class Groups(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'groups'


class LoginAttempts(models.Model):
    ip_address = models.CharField(max_length=16)
    login = models.CharField(max_length=100)
    time = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'login_attempts'


class Users(models.Model):
    ip_address = models.CharField(max_length=16)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=80)    
    salt = models.CharField(max_length=40, blank=True, null=True)
    email = models.CharField(max_length=100)
    activation_code = models.CharField(max_length=40, blank=True, null=True)
    forgotten_password_code = models.CharField(max_length=40, blank=True, null=True)
    forgotten_password_time = models.PositiveIntegerField(blank=True, null=True)
    remember_code = models.CharField(max_length=40, blank=True, null=True)
    created_on = models.PositiveIntegerField()
    last_login = models.PositiveIntegerField(blank=True, null=True)
    active = models.PositiveIntegerField(blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    department_code = models.IntegerField()
    phone = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class UsersGroups(models.Model):
    user = models.ForeignKey(Users, models.DO_NOTHING)
    group = models.ForeignKey(Groups, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_groups'
        unique_together = (('user', 'group'),)