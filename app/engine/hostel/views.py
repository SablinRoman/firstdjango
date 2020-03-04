from django.shortcuts import render
from .models import Student
from .service.stat import Statistics
from .forms import CheckInForm


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
	rooms = Student.objects.all()
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

def student_detail(request, student_det):
	return render(request, 'hostel/student_detail.html', context={'room' : student_det})

def room_detail(request, room_det):
	return render(request, 'hostel/room_detail.html', context={'room' : room_det})

def check_in_student(request):
	def get(self, request):
		form = CheckInForm()
		return render(request, 'hostel/check_in_list.html', context={'form' : form})
