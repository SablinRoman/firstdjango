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
	

	return render(request, 'hostel/index.html', context={'residents' : residents,
														'male_places' : male_places,
														'female_places' : female_places,
														'save_places' : save_places,
														'empty_places' : empty_places,
														'country': county, 'faculty': faculty})




def cards(request):
	rooms = Student.objects.all()

	last_room = None
	cards_dict = {}
	place_list = []
	name_list = []


	for i in rooms:

		if i.place_status == 'мужское' or i.place_status == 'женское' or i.place_status == 'занято':
			place_list.append(i.place_status)


		if last_room == None:
			last_room = i.room
			name_list.append(i.name)


		elif i.room == last_room:
			name_list.append(i.name)
		else:
			cards_dict[last_room] = name_list
			print(place_list)
			name_list = place_list = []
			name_list.append(i.name)
			last_room = i.room


	return  render(request, 'hostel/cards.html', context={'cards' : cards_dict})