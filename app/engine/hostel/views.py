from django.shortcuts import render

from .models import Student

from .service.stat import Statistics


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
	status_list = ['мужское', 'женское', 'занято', 'пусто']

	last_room = None
	cards_dict = {}
	content_list = []

	for i in rooms:
		if last_room == None:
			last_room = i.room 

		if i.room == last_room:
			if i.place_status in status_list:
				content_list.append(i.place_status)
			else:
				content_list.append(i.name)

		else:
			cards_dict[last_room] = content_list
			last_room = i.room 
			content_list = []
			if i.place_status in status_list:
				content_list.append(i.place_status)
			else:
				content_list.append(i.name)
	cards_dict[last_room] = content_list

	return  render(request, 'hostel/cards.html', context={'cards' : cards_dict})


def student_detail(request, name):
	print('I am student_detail in view!')
	student = Student.objects.all(name__iexact=name)
	return render(request, 'hostel/student_detail.html', context={'student' : student})