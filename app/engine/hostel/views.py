from django.shortcuts import render


def hostel_home(request):
	rooms = ['520','523','524','525']
	return 	render(request, 'hostel/index.html', context={'rooms': rooms})