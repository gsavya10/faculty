from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse
from registration.models import *
from student.models import *
from .models import *
from . import forms
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
        # print(stu.roll)
        info = StudentData.objects.using('wsdc_student').filter(roll_number = int(stu.roll))
        # print("f   :   ",info)

        # info = info.first()
        d['name'] = info[0].name
        d['department'] = info[0].branch
        d['class'] = info[0].course
        data.append(d)
        c = c + 1
        # print(c)

    return render(request,'open_elective/students.html',{'data':data})


def allotted_elective(request):
    data = []
    student_details = StudentElectives.objects.filter(allotted = 1)
    #c = 0
    for stu in student_details:
        d = {}
        d['id'] = stu.id
        d['cgpa'] = stu.cgpa
        d['roll_no'] = stu.roll
        d['allotted_elective'] = stu.allotted_elective
        d['priority'] = stu.priority
        # print(stu.roll)
        info = StudentData.objects.using('wsdc_student').filter(roll_number = int(stu.roll))
        # print("f   :   ",info)

        # info = info.first()
        d['name'] = info[0].name
        d['department'] = info[0].branch
        d['class'] = info[0].course
        data.append(d)
        # c = c + 1
        # print(c)
    return render(request,'open_elective/allotted_elective.html',{'data':data})


def put_default(request):
    student_details = StudentElectives.objects.filter(allotted = 1)

    for stu in student_details:
        print(stu.roll)
        dept = EligibleStudents.objects.filter(roll_number = stu.roll).first()
        # dept_details = Department.objects.using('registration').filter(name = department_name).first()
        dept_id = dept.department_id
        index = 1
        priority = 1
        # courses = ['Civil Engineering','Electrical Engineering','Mechanical Engineering','Electronics & communication Engineering','Metallurgical & Materials Engineering','Chemical Engineering','Computer Science & Engineering','Biotechnology','Physics','Chemistry','Mathematics','Humanities & Social Science','School of Management']
        while(index<=12):
            if index == 13:
                pass
            elif dept_id != index:
                elective = ElectiveForm.objects.filter(department_code = index).first()
                c = StudentElectiveChoices(student_id= stu.roll,course_id = elective.course_code ,priority = priority)
                c.save()
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

