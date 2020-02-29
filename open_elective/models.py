# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class OEDbManager(models.Manager):
    using = 'wsdc_electives'

    def get_queryset(self):
        return super(OEDbManager, self).get_queryset().using(self.using)

class Cgupdate(models.Model):
    rollno = models.IntegerField(unique=True, blank=True, null=True)
    cgpa = models.DecimalField(db_column='Cgpa', max_digits=3, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cgupdate'


class Courses(models.Model):
    uid = models.AutoField(primary_key=True)
    cid = models.CharField(max_length=6)
    department = models.CharField(max_length=16)
    name = models.CharField(max_length=67, blank=True, null=True)
    credit = models.IntegerField(blank=True, null=True)
    type = models.IntegerField()
    last_edited_by = models.CharField(max_length=100)
    last_modified_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'courses'


class Departments(models.Model):
    code = models.IntegerField(primary_key=True)
    department_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'departments'


class ElectiveForm(models.Model):
    session_code = models.IntegerField()
    class_code = models.IntegerField()
    department_code = models.IntegerField(blank=True, null=True)
    course_code = models.CharField(max_length=15)
    course_name = models.CharField(max_length=67, blank=True, null=True)
    credit = models.IntegerField(blank=True, null=True)
    type = models.IntegerField()
    no_of_seats = models.IntegerField()
    allotted_seats = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'elective_form'
        unique_together = (('session_code', 'class_code', 'department_code', 'course_code'),)


class EligibleStudents(models.Model):
    roll_number = models.CharField(max_length=10, blank=True, null=True)
    department_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'eligible_students'


class Sessions(models.Model):
    code = models.AutoField(primary_key=True)
    session_name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'sessions'


class StudentElectiveChoices(models.Model):
    student_id = models.IntegerField()
    course_id = models.CharField(max_length=16)
    priority = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'student_elective_choices'
        unique_together = (('student_id', 'course_id'),)


class StudentElectives(models.Model):
    roll = models.CharField(unique=True, max_length=11)
    cgpa = models.DecimalField(max_digits=10, decimal_places=2)
    allotted = models.IntegerField()
    allotted_elective = models.CharField(max_length=10, blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField()
    ipaddress = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student_electives'