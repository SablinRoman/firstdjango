from django.shortcuts import render

from .models import Student



def hostel_home(request):
	students = Student.objects.all()
	return 	render(request, 'hostel/index.html', context={'students': students})