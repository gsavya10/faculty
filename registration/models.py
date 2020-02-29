from django.db import models

class RegistrationDbManager(models.Manager):
    using = 'registration'

    def get_queryset(self):
        return super(RegistrationDbManager, self).get_queryset().using(self.using)

class AllowedstudentsregDayscholars(models.Model):
    regno = models.CharField(db_column='RegNo', max_length=11)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'allowedstudentsreg_dayscholars'


class AttendanceDates(models.Model):
    structure_id = models.IntegerField()
    course_id = models.CharField(max_length=10)
    section = models.CharField(max_length=2)
    lab_batch = models.IntegerField()
    date = models.DateField()
    no_hours = models.DecimalField(max_digits=11, decimal_places=2)
    start = models.TimeField()
    end = models.TimeField()

    class Meta:
        managed = False
        db_table = 'attendance_dates'


class AttendanceRecord(models.Model):
    count = models.AutoField(primary_key=True)
    id = models.IntegerField()
    rollno = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'attendance_record'


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


class AutoReg(models.Model):
    regno = models.CharField(primary_key=True, max_length=16)
    section = models.CharField(max_length=7, blank=True, null=True)
    course_list = models.CharField(max_length=62, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auto_reg'


class BlockStudent(models.Model):
    reg_no = models.CharField(max_length=25)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'block_student'


class CompData(models.Model):
    registered_id = models.IntegerField(blank=True, null=True)
    reg_structure_id = models.IntegerField(blank=True, null=True)
    reg_session_id = models.IntegerField(blank=True, null=True)
    reg_session_name = models.CharField(max_length=128, blank=True, null=True)
    reg_department_id = models.IntegerField(blank=True, null=True)
    reg_department_name = models.CharField(max_length=100, blank=True, null=True)
    reg_specialization_id = models.IntegerField(blank=True, null=True)
    reg_specialization_name = models.CharField(max_length=256, blank=True, null=True)
    reg_semester = models.IntegerField(blank=True, null=True)
    reg_section = models.CharField(max_length=2, blank=True, null=True)
    registration_number = models.CharField(max_length=10, blank=True, null=True)
    structure_id = models.IntegerField(blank=True, null=True)
    section = models.CharField(max_length=2, blank=True, null=True)
    course_id = models.CharField(max_length=9, blank=True, null=True)
    course_name = models.CharField(max_length=67, blank=True, null=True)
    credit = models.IntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    course_type_name = models.CharField(max_length=100, blank=True, null=True)
    batch = models.IntegerField(blank=True, null=True)
    mode = models.IntegerField(blank=True, null=True)
    backlog = models.IntegerField(blank=True, null=True)
    registered_on = models.DateTimeField(blank=True, null=True)
    last_modified_on = models.DateTimeField()
    pre_registered = models.IntegerField(blank=True, null=True)
    approved = models.IntegerField(blank=True, null=True)
    academic_fee_status = models.IntegerField(blank=True, null=True)
    hostel_fee_status = models.IntegerField(blank=True, null=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comp_data'


class CourseAllottedMode(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'course_allotted_mode'


class CourseFacultyAllotted(models.Model):
    regular_course_id = models.IntegerField()
    section = models.CharField(max_length=2)
    batch_index = models.IntegerField()
    faculty_id = models.IntegerField(blank=True, null=True)
    last_modified_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'course_faculty_allotted'
        unique_together = (('regular_course_id', 'section', 'batch_index'),)


class Courses(models.Model):
    id = models.CharField(primary_key=True, max_length=9)
    name = models.CharField(max_length=67)
    credit = models.IntegerField()
    type = models.IntegerField()
    last_modified_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'courses'


class CoursesType(models.Model):
    name = models.CharField(max_length=100)
    last_modified_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'courses_type'


class Department(models.Model):
    name = models.CharField(max_length=100)
    last_modified_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'department'


class DepartmentSpecialization(models.Model):
    department_id = models.IntegerField()
    specialization_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'department_specialization'
        unique_together = (('department_id', 'specialization_id'),)


class DetailedDepartmentSpecialization(models.Model):
    department_id = models.IntegerField()
    department_name = models.CharField(max_length=100, blank=True, null=True)
    specialization_id = models.IntegerField()
    specialization_name = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'detailed_department_specialization'


class DetailedDumRegistration(models.Model):
    registered_id = models.IntegerField(blank=True, null=True)
    reg_structure_id = models.IntegerField(blank=True, null=True)
    registration_number = models.CharField(max_length=10, blank=True, null=True)
    reg_section = models.CharField(max_length=2, blank=True, null=True)
    pre_registered = models.IntegerField(blank=True, null=True)
    approved = models.IntegerField(blank=True, null=True)
    academic_fee_status = models.IntegerField(blank=True, null=True)
    hostel_fee_status = models.IntegerField(blank=True, null=True)
    reg_session_id = models.IntegerField(blank=True, null=True)
    reg_session_name = models.CharField(max_length=128, blank=True, null=True)
    reg_department_id = models.IntegerField(blank=True, null=True)
    reg_department_name = models.CharField(max_length=100, blank=True, null=True)
    reg_specialization_id = models.IntegerField(blank=True, null=True)
    reg_specialization_name = models.CharField(max_length=256, blank=True, null=True)
    reg_semester = models.IntegerField(blank=True, null=True)
    course_id = models.CharField(max_length=9)
    batch = models.IntegerField()
    mode = models.IntegerField()
    registered_on = models.DateTimeField()
    last_modified_on = models.DateTimeField()
    backlog = models.IntegerField()
    course_name = models.CharField(max_length=67, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    credit = models.IntegerField(blank=True, null=True)
    course_type_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'detailed_dum_registration' 
        unique_together = ("registered_id", "reg_structure_id","registration_number")       

    objects = RegistrationDbManager()


class DetailedRegistration(models.Model):
    registered_id = models.IntegerField(blank=True, null=True)
    reg_structure_id = models.IntegerField(blank=True, null=True)
    registration_number = models.CharField(max_length=10, blank=True, null=True)
    reg_section = models.CharField(max_length=2)
    pre_registered = models.IntegerField(blank=True, null=True)
    approved = models.IntegerField(blank=True, null=True)
    academic_fee_status = models.IntegerField(blank=True, null=True)
    hostel_fee_status = models.IntegerField(blank=True, null=True)
    reg_session_id = models.IntegerField(blank=True, null=True)
    reg_session_name = models.CharField(max_length=128, blank=True, null=True)
    reg_department_id = models.IntegerField(blank=True, null=True)
    reg_department_name = models.CharField(max_length=100, blank=True, null=True)
    reg_specialization_id = models.IntegerField(blank=True, null=True)
    reg_specialization_name = models.CharField(max_length=256, blank=True, null=True)
    reg_semester = models.IntegerField(blank=True, null=True)
    course_id = models.CharField(max_length=9)
    batch = models.IntegerField()
    mode = models.IntegerField()
    registered_on = models.DateTimeField()
    last_modified_on = models.DateTimeField()
    backlog = models.IntegerField()
    course_name = models.CharField(max_length=67, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    credit = models.IntegerField(blank=True, null=True)
    course_type_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'detailed_registration'


class DetailedStructure(models.Model):
    structure_id = models.IntegerField(primary_key=True)
    faculty_id = models.IntegerField(blank=True, null=True)
    semester = models.IntegerField()
    department_id = models.IntegerField()
    department_name = models.CharField(max_length=100)
    specialization_id = models.IntegerField()
    specialization_name = models.CharField(max_length=256)
    session_id = models.IntegerField()
    session_name = models.CharField(max_length=128)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'detailed_structure'


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


class ExamOnly(models.Model):
    sno = models.AutoField(primary_key=True)
    regno2 = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'exam_only'


class FeesPayment(models.Model):
    reg_no = models.CharField(unique=True, max_length=100)
    hostel_fees_status = models.IntegerField()
    amount_to_be_paid = models.IntegerField()
    student_paid = models.IntegerField()
    faculty_advisor_approved = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fees_payment'


class NewRollList(models.Model):
    id = models.IntegerField(primary_key=True)
    roll_no = models.IntegerField()
    reg_no = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    section = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'new_roll_list'


class Registered(models.Model):
    registration_number = models.CharField(max_length=10)
    reg_structure = models.ForeignKey('Structure', models.DO_NOTHING)
    reg_section = models.ForeignKey('Section', models.DO_NOTHING, db_column='reg_section')
    pre_registered = models.IntegerField()
    approved = models.IntegerField()
    academic_fee_status = models.IntegerField()
    hostel_fee_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'registered'
        unique_together = (('registration_number', 'reg_structure'),)


class RegisteredCourses(models.Model):
    registered = models.ForeignKey(Registered, models.DO_NOTHING)
    structure = models.ForeignKey('Structure', models.DO_NOTHING)
    section = models.ForeignKey('Section', models.DO_NOTHING, db_column='section')
    course = models.ForeignKey(Courses, models.DO_NOTHING)
    batch = models.IntegerField()
    mode = models.ForeignKey('RegisteredMode', models.DO_NOTHING, db_column='mode')
    backlog = models.IntegerField()
    registered_on = models.DateTimeField()
    last_modified_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'registered_courses'
        unique_together = (('registered', 'structure', 'course', 'backlog'),)


class RegisteredCoursesOld(models.Model):
    id = models.IntegerField(primary_key=True)
    registered_id = models.IntegerField()
    structure_id = models.IntegerField()
    section = models.CharField(max_length=2)
    course_id = models.CharField(max_length=9)
    batch = models.IntegerField()
    mode = models.IntegerField()
    backlog = models.IntegerField()
    registered_on = models.DateTimeField()
    last_modified_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'registered_courses_old'


class RegisteredCoursesOops(models.Model):
    registered_id = models.IntegerField()
    structure_id = models.IntegerField()
    section = models.CharField(max_length=2)
    course_id = models.CharField(max_length=9)
    batch = models.IntegerField()
    mode = models.IntegerField()
    backlog = models.IntegerField()
    registered_on = models.DateTimeField()
    last_modified_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'registered_courses_oops'
        unique_together = (('registered_id', 'structure_id', 'course_id', 'backlog'),)


class RegisteredMode(models.Model):
    name = models.CharField(max_length=20)
    last_modified_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'registered_mode'


class RegisteredOld(models.Model):
    id = models.IntegerField(primary_key=True)
    registration_number = models.CharField(max_length=10)
    reg_structure_id = models.IntegerField()
    reg_section = models.CharField(max_length=2)
    pre_registered = models.IntegerField()
    approved = models.IntegerField()
    academic_fee_status = models.IntegerField()
    hostel_fee_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'registered_old'


class RegistrationAllottedCourses(models.Model):
    regular_course_id = models.IntegerField()
    structure_id = models.IntegerField()
    course_id = models.CharField(max_length=9)
    course_mode = models.IntegerField()
    course_type = models.IntegerField(blank=True, null=True)
    course_type_name = models.CharField(max_length=100, blank=True, null=True)
    course_mode_name = models.CharField(max_length=50, blank=True, null=True)
    credit = models.IntegerField(blank=True, null=True)
    course_name = models.CharField(max_length=67, blank=True, null=True)
    section = models.CharField(max_length=2, blank=True, null=True)
    batch_index = models.IntegerField(blank=True, null=True)
    faculty_id = models.IntegerField(blank=True, null=True)
    cfid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'registration_allotted_courses'


class RegularCourses(models.Model):
    structure_id = models.IntegerField()
    course_id = models.CharField(max_length=9)
    course_mode = models.IntegerField()
    last_modified_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'regular_courses'
        unique_together = (('structure_id', 'course_id'),)


class Requested(models.Model):
    registration_number = models.CharField(max_length=10)
    reg_structure_id = models.IntegerField()
    reg_section = models.CharField(max_length=2)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'requested'
        unique_together = (('registration_number', 'reg_structure_id'),)


class RequestedCourses(models.Model):
    registered_id = models.IntegerField()
    structure_id = models.IntegerField()
    section = models.CharField(max_length=2)
    course_id = models.CharField(max_length=9)
    batch = models.IntegerField()
    mode = models.IntegerField()
    backlog = models.IntegerField()
    dropped = models.IntegerField()
    registered_on = models.DateTimeField()
    last_modified_on = models.DateTimeField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'requested_courses'
        unique_together = (('registered_id', 'structure_id', 'course_id', 'backlog'),)


class Section(models.Model):
    id = models.CharField(primary_key=True, max_length=2)

    class Meta:
        managed = False
        db_table = 'section'


class Session(models.Model):
    name = models.CharField(max_length=128)
    last_modified_on = models.DateTimeField()
    results_publish = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'session'


class Specialization(models.Model):
    abbr = models.CharField(max_length=16)
    name = models.CharField(max_length=256)
    last_modified_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'specialization'


class Structure(models.Model):
    faculty_id = models.IntegerField(blank=True, null=True)
    session_id = models.IntegerField()
    department_id = models.IntegerField()
    specialization_id = models.IntegerField()
    semester = models.IntegerField()
    last_modified_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'structure'
        unique_together = (('session_id', 'department_id', 'specialization_id', 'semester'),)


class StructureOverride(models.Model):
    regno = models.CharField(primary_key=True, max_length=10)
    structure_id = models.CharField(max_length=10)
    section = models.CharField(max_length=5)
    session_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'structure_override'


class StructureSection(models.Model):
    structure_id = models.IntegerField()
    section = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'structure_section'
        unique_together = (('structure_id', 'section'),)


class StudCurrRegStatus(models.Model):
    registration_number = models.CharField(max_length=10)
    specialization = models.CharField(max_length=256)
    department = models.CharField(max_length=100)
    section = models.CharField(max_length=2)
    current_year = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'stud_curr_reg_status'


class StudentData(models.Model):
    userid = models.PositiveIntegerField()
    name = models.CharField(max_length=64)
    roll_number = models.CharField(max_length=10, blank=True, null=True)
    registration_number = models.CharField(max_length=10, blank=True, null=True)
    current_section = models.CharField(max_length=40, blank=True, null=True)
    current_year = models.CharField(max_length=4)
    joining_year = models.CharField(max_length=40)
    course = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    gender = models.CharField(max_length=1)
    birthday = models.DateField(blank=True, null=True)
    country = models.CharField(max_length=32)
    mobile = models.CharField(max_length=16)
    emergency_contact = models.CharField(max_length=16)
    sbh_account = models.CharField(max_length=32, blank=True, null=True)
    passport = models.CharField(max_length=20, blank=True, null=True)
    hostel_room = models.CharField(max_length=10)
    hostel = models.CharField(max_length=10)
    mess = models.CharField(max_length=10)
    created_location = models.CharField(max_length=32)
    created_time = models.DateTimeField()
    guardian1 = models.CharField(max_length=64, blank=True, null=True)
    relationship1 = models.CharField(max_length=64, blank=True, null=True)
    email1 = models.CharField(max_length=64, blank=True, null=True)
    mobile1 = models.CharField(max_length=16, blank=True, null=True)
    guardian2 = models.CharField(max_length=64, blank=True, null=True)
    relationship2 = models.CharField(max_length=64, blank=True, null=True)
    email2 = models.CharField(max_length=64, blank=True, null=True)
    mobile2 = models.CharField(max_length=16, blank=True, null=True)
    homenumber = models.CharField(max_length=16, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    bloodgroup = models.CharField(max_length=50, blank=True, null=True)
    adhaar = models.CharField(max_length=20, blank=True, null=True)
    linkedin = models.CharField(max_length=100, blank=True, null=True)
    mac = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'student_data'


class Temp(models.Model):
    col_1 = models.CharField(db_column='COL 1', max_length=37, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    col_2 = models.CharField(db_column='COL 2', max_length=7, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    col_3 = models.CharField(db_column='COL 3', max_length=7, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    col_4 = models.CharField(db_column='COL 4', max_length=39, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    col_5 = models.CharField(db_column='COL 5', max_length=14, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    col_6 = models.CharField(db_column='COL 6', max_length=8, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cid = models.CharField(max_length=6, blank=True, null=True)
    cname = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'temp'


class Timestamp(models.Model):
    regno = models.CharField(max_length=10)
    time = models.DateTimeField()
    ip = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'timestamp'


class TimestampRequested(models.Model):
    regno = models.CharField(max_length=10)
    time = models.DateTimeField()
    ip = models.CharField(max_length=20)
    status = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'timestamp_requested'


class TimestampSession10(models.Model):
    regno = models.CharField(max_length=10)
    time = models.DateTimeField()
    ip = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'timestamp_session_10'


class TimestampSession9(models.Model):
    regno = models.CharField(max_length=10)
    time = models.DateTimeField()
    ip = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'timestamp_session_9'