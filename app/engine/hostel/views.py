from .models import Student
from .models import Room
from .service.stat import Statistics
from .forms import StudentForm
from .forms import RoomForm
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import View
from django.shortcuts import redirect


def number_of(request):
    residents = Statistics.num_of_residents
    male_places = Statistics.male_places
    female_places = Statistics.female_places
    save_places = Statistics.save_places
    empty_places = Statistics.empty_places

    county = Statistics.citizenship_sort()
    faculty = Statistics.faculty_sort()
    form = Statistics.form_studies_sort()
    reg = Statistics.registration_sort()

    return render(request, 'hostel/index.html', context={'residents': residents,
                                                         'male_places': male_places,
                                                         'female_places': female_places,
                                                         'save_places': save_places,
                                                         'empty_places': empty_places,
                                                         'country': county,
                                                         'faculty': faculty,
                                                         'form': form,
                                                         'reg': reg, })


def cards(request):
    room_list = Room.objects.all()
    print(room_list)
    twin_rooms = []
    hostel_rooms = []

    for index, room in enumerate(room_list):
        if index % 2 == 0:
            twin_rooms.append(room)
        else:
            twin_rooms.append(room)
            hostel_rooms.append(twin_rooms)
            twin_rooms = []
    print(hostel_rooms)
    return render(request, 'hostel/cards.html', context={'hostel_rooms': hostel_rooms})


class Student_detail(View):
    def get(self, request, id):
        student = Student.objects.get(id=id)
        return render(request, 'hostel/student_detail.html', context={'room': id, 'student': student})


def student_delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect(reverse('rooms_url'))


class Room_detail(View):
    def get(self, request, room_det):
        return render(request, 'hostel/room_detail.html', context={'room': room_det})


class Сheck_in_student(View):
    def get(self, request):
        form_student = StudentForm()
        form_room = RoomForm()
        return render(request, 'hostel/check_in_list.html', context={'form_student': form_student, 'form_room': form_room})

    def post(self, request):
        bound_form_student = StudentForm(request.POST)
        bound_form_room = RoomForm(request.POST)
        if bound_form_student.is_valid() and bound_form_room.is_valid():
            new_student = bound_form_student.save()
            print(new_student)
            print('0000000000000000000000000000')
            return redirect(new_student)
        print('==================================')
        return render(request, 'hostel/check_in_list.html', context={'form': bound_form_student})


class Check_In_student_Update(View):
    def get(self, request, id):
        student = Student.objects.get(id=id)
        bound_form = CheckInForm(instance=student)
        return render(request, 'hostel/check_in_update_list.html',
                      context={'bound_form': bound_form, 'student': student})

    def post(self, request, id):
        student = Student.objects.get(id=id)
        bound_form = CheckInForm(request.POST, instance=student)
        if bound_form.is_valid():
            new_student = bound_form.save()
            return redirect(new_student)
        return render(request, 'hostel/check_in_update_list.html',
                      context={'bound_form': bound_form, 'student': student})
