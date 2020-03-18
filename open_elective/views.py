from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse
from registration.models import *
from student.models import *
from results.models import *
from .models import *
from . import forms
from decimal import *
import json


# Create your views here.
def home(request):
    return render(request, 'open_elective/home.html')


def course_list(request):
    courses = ElectiveForm.objects.filter(class_code = 1)
    dept = Departments.objects.filter()

    if request.method == 'POST':
        d = {}
        d['dep_code'] = ""
        d['seats'] = []
        d['course_code'] = []

        for key, value in request.POST.items():
            try:
                d['dep_code'] = int(key)
            except ValueError:
                continue
        d['seats'] = request.POST.getlist('seats')
        d['course_code'] = request.POST.getlist('course_code')
        dep_code = int(d['dep_code'])
        if dep_code == 14:  # There isn't any department with code = 13. This is done to avoid indexing errors
            dep_code = dep_code - 1
        course_code = d['course_code'][dep_code]
        seats = d['seats'][dep_code - 1]
        elective = ElectiveForm.objects.get(course_code=course_code)
        elective.no_of_seats = int(seats)
        elective.save()
    return render(request, 'open_elective/course_list.html', {'courses': courses, 'department': dept})


def students(request):
    data = []
    student_details = StudentElectives.objects.filter(allotted = 1)
    c = 0
    for stu in student_details:
        d = {}
        d['id'] = stu.id
        d['cgpa'] = stu.cgpa
        d['roll_no'] = stu.roll

        info = StudentData.objects.using('wsdc_student').filter(roll_number = int(stu.roll))
        d['name'] = info[0].name
        d['department'] = info[0].branch
        d['class'] = info[0].course
        data.append(d)
        c = c + 1

    return render(request,'open_elective/students.html',{'data':data})


def allotted_elective(request):
    if request.method == 'POST':
        allot(request)
    data = []
    student_details = StudentElectives.objects.filter(allotted=1)
    for stu in student_details:
        d = {}
        d['cgpa'] = stu.cgpa
        d['roll_no'] = stu.roll
        d['allotted_elective'] = stu.allotted_elective
        d['priority'] = stu.priority
        info = StudentData.objects.using('wsdc_student').filter(roll_number = int(stu.roll))
        d['name'] = info[0].name
        d['department'] = info[0].branch
        d['class'] = info[0].course
        data.append(d)

    return render(request,'open_elective/allotted_elective.html',{'data':data})


def put_default(request):
    # student_details = StudentElectives.objects.filter(allotted=1)  # using it because already allotted
    students_detail = EligibleStudents.objects.filter()
    for stu in students_detail:
        index = 1
        priority = 1
        while index <= 14:
            if index == 13:
                pass
            elif stu.department_id != index:
                elective = ElectiveForm.objects.get(department_code=index)
                c = StudentElectiveChoices(student_id=stu.roll_number, course_id=elective.course_code, priority=priority)
                c.save(using='wsdc_electives')
                priority = priority + 1
            index = index + 1
    return redirect('/open_elective')


def search(request):
    if request.method == 'POST':
        formobj = forms.RollForm(request.POST)
        if formobj.is_valid():
            reqroll = formobj.cleaned_data['roll']
            try:
                studentobj = StudentElectives.objects.get(roll=reqroll)
            except:
                messages.warning(request, 'We have no record of this student (Roll number: %s), either this student has not submitted the elective application form or there was a problem uploading it.' % reqroll)
                return render(request, 'open_elective/search.html')
            schoices = StudentElectiveChoices.objects.filter(student_id=reqroll)
            info = StudentData.objects.using('wsdc_student').get(roll_number=int(reqroll))
            courselist = Courses.objects.filter()
            search_dict = {
                'skey': studentobj,
                'skey2': schoices,
                'skey3': info,
                'skey4': courselist,
            }
            return render(request, 'open_elective/search.html', search_dict)
    else:
        return render(request, 'open_elective/search.html')


def admin_allot_view(request):
    if request.method == 'POST':
        message = 'Allotted successfully!'
        try:
            roll = request.POST.get('roll')
            int(roll)
            cgpa = Decimal(request.POST.get('cgpa'))
        except ValueError:
            return render(request, 'open_elective/adminAllot.html',
                          {'message': 'Please check the correct format of the Roll number!'})
        except ArithmeticError:
            return render(request, 'open_elective/adminAllot.html',
                          {'message': 'Please check the correct format of the CGPA!'})
        cid = request.POST.get('cid')
        try:
            elective = ElectiveForm.objects.get(course_code=cid)
        except ElectiveForm.DoesNotExist:
            return render(request, 'open_elective/adminAllot.html',
                          {'message': 'Please check your Course ID!'})
        if elective.allotted_seats < elective.no_of_seats:
            try:
                student_elective = StudentElectives.objects.get(roll=roll)
                elective_existing = ElectiveForm.objects.get(course_code=student_elective.allotted_elective)
                elective_existing.allotted_seats = elective_existing.allotted_seats - 1
                elective_existing.save()
                student_elective.delete()
            except:
                pass
            finally:
                student_elective_new = StudentElectives(roll=roll, cgpa=cgpa, allotted_elective=cid, allotted=1, ipaddress=get_client_ip(request))
                student_elective_new.save(using='wsdc_electives')
                elective.allotted_seats = elective.allotted_seats + 1
                elective.save()
        else:
            message = 'The no of seats in the course '+cid+' are already full!'
        return render(request, 'open_elective/adminAllot.html', {'message': message})
    else:
        return render(request, 'open_elective/adminAllot.html')


def allot(request):
    StudentElectives.objects.all().delete()
    elective_form = ElectiveForm.objects.filter()
    for course in elective_form:
        course.allotted_seats = 0
        course.save(using='wsdc_electives')

    student_elective_choices = StudentElectiveChoices.objects.filter()
    for sec in student_elective_choices:
        courses = Courses.objects.filter()
        dep = int(str(sec.student_id)[2])
        for c in courses:
            if sec.course_id == c.cid:
                if dep == c.department:
                    sec.priority = 0
                    sec.save(using='wsdc_electives')

    eligible_students = EligibleStudents.objects.filter()
    for stud in eligible_students:
        cg = getCGPA(stud.roll_number)
        if cg is None:
            continue
        student_elective_new = StudentElectives(roll=stud.roll_number, cgpa=cg, allotted=0)
        student_elective_new.save(using='wsdc_electives')

    student_elective = StudentElectives.objects.filter().order_by('-cgpa')
    for studelect in student_elective:
        preferences = StudentElectiveChoices.objects.filter(student_id=studelect.roll, priority__gt=0).order_by('priority')
        for pref in preferences:
            courses = ElectiveForm.objects.get(course_code=pref.course_id)
            if courses.allotted_seats < courses.no_of_seats:
                courses.allotted_seats = courses.allotted_seats + 1
                courses.save(using='wsdc_electives')
                studelect.allotted = 1
                studelect.allotted_elective = pref.course_id
                studelect.priority = pref.priority
                studelect.ipaddress = get_client_ip(request)
                studelect.save(using='wsdc_electives')
                break

    return redirect(allotted_elective)


def getCGPA(rollnumber):
    cgpa = Cgupdate.objects.filter(rollno=rollnumber)
    if cgpa.count() == 0:
        cgpa = Results.objects.filter(regno=rollnumber).order_by('-reference_id')
    if cgpa.count() == 0:
        cgpa = -1
    else:
        cgpa = cgpa[0].cgpa
    return cgpa


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
