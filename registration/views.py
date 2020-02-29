from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect, HttpResponseRedirect
from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from registration.models import *
from student.models import *
from faculty_profile.models import *
from django.http import JsonResponse
import json
from django.core import serializers
from datetime import datetime
# Create your views here.

def start(request):
	kar=Registered.objects.filter(registration_number='931643')
	for ka in kar:
		print (ka.reg_structure_id)  
	response={}
	response['kar']='karma is a bitch'
	data={'kar':'karma is a bitch'}
	#return render(request,'registration/dummy.djt',data)  
	return HttpResponse('karmadsdfgfhgdffs')

def Reg_slip(request):
	if request.method =='POST':		
		num=request.POST.get('number')		
		num_type=request.POST.get('num')
		if(num_type=='roll'):			
			reg_num=StudentData.objects.using('wsdc_student').get(roll_number=num).registration_number
		else:
			reg_num=num
		data2={'kar':'karma is a bitch'}
		data = {'registration_number':	str(reg_num)}
		registered = Registered.objects.filter(registration_number=data['registration_number'])
		student_data = StudentData.objects.using('wsdc_student').filter(registration_number=data['registration_number'])
		data['student_name'] = student_data[0].name
		data['roll_number']=student_data[0].roll_number			
		data['registered'] = []
		data['sems'] = []		
		for reg in registered:
			section = reg.reg_section
			structure_id = reg.reg_structure_id
			r = {}
			sum =0
			r['section'] = section
			r['courses'] = []
			r['credit'] = []	
			q = RegisteredCourses.objects.filter(registered_id=reg.id)
			f = q.first()
			struct = Structure.objects.filter(id = structure_id)
			s = struct.first()
			dept_id = s.department_id
			spec_id = s.specialization_id
			department = Department.objects.filter(id = dept_id)
			department = department.first()
			specialization = Specialization.objects.filter(id = spec_id)
			specialization = specialization.first()
			r['dept_id'] = department.name
			r['spec_id'] = specialization.name
			r['semester'] = s.semester
			summ = 0
			diff = 0
			for course in q:
				details = Courses.objects.filter(id=course.course_id)
				for detail in details:
					if(detail.type == 1):
						detail.type = 'THEORY'
					elif(detail.type == 2):
						detail.type = 'LABORATORY'
					elif(detail.type == 3):
						detail.type = 'SEMINAR'
					elif(detail.type == 4):
						detail.type = 'PROJECT'
					elif(detail.type == 5):
						detail.type = 'COMPREHENSIVE VIVA'
					elif(detail.type == 6):
						detail.type = 'THEORY AND LAB'
					summ = summ + detail.credit
					if (course.mode.id==2):
						diff = diff + detail.credit
						print('yes')
				r['study'] = summ - diff
				r['sum'] = summ
				r['courses'].append(details)
			data['registered'].append(r)			
			chosen = data['registered']
			data['chosen'] = data['registered'][len(chosen) - 1]['semester']
			print(data['chosen'])
			data['sems'].append(s.semester)				
		return render(request, 'registration/slip.djt', data)		
	else:
		response={}
		return render(request,'registration/slip.djt',response)

def PortData(request):
	session=Session.objects.all().order_by('-id').first()
	s=session.id	
	print(s)
	PrevStructures=Structure.objects.filter(session_id=s-2).order_by('id')
	print(PrevStructures.count())
	structcount=0
	sectioncount=0
	coursecount=0
	batchcount=0
	for PrevStruct in PrevStructures:
		PrevCourses=RegularCourses.objects.filter(structure_id=PrevStruct.id)
		PrevSections=StructureSection.objects.filter(structure_id=PrevStruct.id)
		CurrStructure=Structure()
		CurrStructure.faculty_id=None
		CurrStructure.session_id=s
		CurrStructure.department_id=PrevStruct.department_id
		CurrStructure.specialization_id=PrevStruct.specialization_id
		CurrStructure.semester=PrevStruct.semester
		CurrStructure.last_modified_on=datetime.now()
		CurrStructure.save()
		structcount+=1
		CurrStructure=Structure.objects.filter(session_id=s).order_by('-id')
		cs=CurrStructure.first()			
		for PrevSect in PrevSections:
			section=StructureSection()
			section.structure_id=cs.id
			section.section=PrevSect.section
			section.save()
			sectioncount+=1
		for PrevCourse in PrevCourses:
			Batches=CourseFacultyAllotted.objects.filter(regular_course_id=PrevCourse.id)
			regCourse=RegularCourses()
			regCourse.structure_id=cs.id
			regCourse.course_id=PrevCourse.course_id
			regCourse.course_mode=PrevCourse.course_mode
			regCourse.last_modified_on=datetime.now()
			regCourse.save()
			coursecount+=1
			CurrCourse=RegularCourses.objects.all().order_by('-id')
			cc=CurrCourse.first()
			for Batch in Batches:
				currBatch=CourseFacultyAllotted()
				currBatch.regular_course_id=cc.id
				currBatch.section=Batch.section
				currBatch.batch_index=Batch.batch_index
				currBatch.faculty_id=None
				currBatch.last_modified_on=datetime.now()
				currBatch.save()
				batchcount+=1	
	return HttpResponse('Data is ported:)')

def AllotFacAd(request):

	fac_users=Users.objects.using('faculty_profile').filter(active=1)
	print(fac_users.count())
	print('karma')
	facultys=[]
	for fac_user in fac_users:
		try:
			faculty=FacultyCurrentData.objects.using('faculty_profile').get(facultyid=fac_user.id)
			facultys.append(faculty)
		except:
			print('User data doesnot exist')			
	session=Session.objects.all().order_by('-id').first()
	s=session.id
	structures=[]
	structures=DetailedStructure.objects.filter(session_id=15)
	response={}
	response['facultys']=facultys
	response['structures']=structures	
	count=0
	for structure in structures:		
		count+=1
	print(count)
	return render(request,'registration/allotfacad.djt',response)
	return HttpResponse('faculty data printed in cmd')







