from .models import Student
from .service.stat import Statistics
from .forms import CheckInForm
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import View
from django.shortcuts import redirect

def number_of(request):
	residents = Statistics.num_of_residents
	male_places = Statistics.male_places
	female_places  = Statistics.female_places
	save_places = Statistics.save_places
	empty_places= Statistics.empty_places

	county = Statistics.citizenship_sort()
	faculty = Statistics.faculty_sort()
	form = Statistics.form_studies_sort()
	reg = Statistics.registration_sort()

	return render(request, 'hostel/index.html', context={'residents' : residents,
														'male_places' : male_places,
														'female_places' : female_places,
														'save_places' : save_places,
														'empty_places' : empty_places,
														'country': county, 
														'faculty': faculty,
														'form' : form,
														'reg': reg,})

def cards(request):
	rooms = Student.objects.all().order_by('room')
	last_room = None
	names_list = []
	rooms_list = []

	for i in rooms:
		if last_room == None:
			last_room = i.room
		if i.room == last_room:
			names_list.append(i)
		else:
			rooms_list.append(names_list)
			last_room = i.room
			names_list = []
			names_list.append(i)
	rooms_list.append(names_list)
	return render(request, 'hostel/cards.html', context={'rooms_list' : rooms_list})

class Student_detail(View):
	def get(self, request, id):
		student = Student.objects.get(id= id)
		return render(request, 'hostel/student_detail.html', context={'room': id, 'student': student})

class Room_detail(View):
	def get(self, request, room_det):
		return render(request, 'hostel/room_detail.html', context={'room': room_det})

class Сheck_in_student(View):
	def get(self, request):
		form = CheckInForm()
		return render(request, 'hostel/check_in_list.html', context={'form' : form})

	def post(self, request):
		bound_form = CheckInForm(request.POST)
		if bound_form.is_valid():
			new_student = bound_form.save()
			return redirect(new_student)
		return render(request, 'hostel/check_in_list.html', context={'form' : bound_form})

class Check_In_student_Update(View):
	def get(self, request, id):
		student = Student.objects.get(id= id)
		bound_form = CheckInForm(instance=student)
		return render(request, 'hostel/check_in_update_list.html', context={'bound_form' : bound_form, 'student' : student})

	def post(self, request, id):
		student = Student.objects.get(id= id)
		bound_form = CheckInForm(request.POST, instance=student)
		if bound_form.is_valid():
			new_student = bound_form.save()
			return redirect(new_student)
		return render(request, 'hostel/check_in_update_list.html', context={'bound_form' : bound_form, 'student' : student})

class StudentDelete(View):
	def get(self, request, id):
		student = Student.objects.get(id= id)

	def post(self, request, id):
		student = Student.objects.get(id=id)
		student.delete()
		return redirect(reverse('rooms_url'))

