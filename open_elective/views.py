from django.shortcuts import render, get_object_or_404
from .models import *
from registration.models import *
from student.models import *
from . import forms

# Create your views here.
def course_list(request):

	MyForm = forms.MyForm()
	cources = ElectiveForm.objects.filter(class_code = 1)
	print('beforeform')
	if request.method == 'POST':
		print('aftersubmit')
		MyForm = forms.MyForm(request.POST)
		if MyForm.is_valid():
			print('formvalid')
			seats = MyForm.cleaned_data['seats']
			course_code = MyForm.cleaned_data['course_code']
			elective = ElectiveForm.objects.get(course_code = course_code)
			elective.no_of_seats = seats
			print(seats)
			elective.save()
	return render(request, 'open_elective/course_list.html',{'cources':cources})

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
	c = 0
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
    if(request.method=='POST'):
        formobj=forms.RollForm(request.POST)

        if(formobj.is_valid()):
            reqroll = formobj.cleaned_data['roll']
            print(reqroll)
            studentobj = get_object_or_404(StudentElectives, roll =reqroll)
            schoices= StudentElectiveChoices.objects.filter(student_id=reqroll)
            search_dict={'skey':studentobj,
                        'skey2':schoices}
            return render(request,'open_elective/searchResult.html',search_dict)
           
    else:
        return render(request,'open_elective/search.html')