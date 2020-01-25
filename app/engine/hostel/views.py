from django.shortcuts import render

from .models import Student

from .service.stat import Statistics


def number_of(request):
	a = Statistics.places()
	b = Statistics.stat_group()

	a= Statistics.qwe
	print(a)



	return render(request, 'hostel/index.html', context=a)


