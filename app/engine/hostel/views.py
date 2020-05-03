from .models import Student
from .models import Room
from .models import CardsFilter
from .service.stat import Statistics
from .forms import StudentForm
from .forms import RoomForm
from .forms import FiltersForm
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


class AddRoom(View):
    def get(self, request):
        form = RoomForm
        return render(request, 'hostel/add_a_room.html', context={'form': form})

    def post(self, request):
        bound_form = RoomForm(request.POST)
        if bound_form.is_valid():
            new_room = bound_form.save()
            print(new_room)
            return redirect(reverse('rooms_url'))
        return render(request, 'hostel/add_a_room.html', context={'form': bound_form})


class Cards(View):
    def get(self, request):
        filter = CardsFilter.objects.get(id=1)
        bound_form = FiltersForm(instance=filter)
        room_list = []

        if filter.all is True:
            room_list = Room.objects.all().order_by('room_numb')

        else:
            status_list = []

            if filter.men is True:
                status_list.append('мужское')
            if filter.women is True:
                status_list.append('женское')
            if filter.free is True:
                status_list.append('пусто')
            if filter.busy is True:
                status_list.append('занято')

            rooms = Student.objects.filter(bed_status__in=status_list).values_list('room', flat=True).order_by('room')

            for room in rooms:
                room_list.append(Room.objects.get(room_numb=room))

        twin_rooms = []
        hostel_rooms = []

        for index, room in enumerate(room_list):
            if index % 2 == 0:
                twin_rooms.append(room)
            else:
                twin_rooms.append(room)
                hostel_rooms.append(twin_rooms)
                twin_rooms = []
        hostel_rooms.append(twin_rooms)
        return render(request, 'hostel/cards.html', context={'form': bound_form,
                                                             'hostel_rooms': hostel_rooms})

    def post(self, request):
        bound_form = FiltersForm(request.POST)
        if bound_form.is_valid():
            return redirect(reverse('rooms_url'))
        return render(request, 'hostel.cards.html', context={'form': bound_form})


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
        form = StudentForm()
        return render(request, 'hostel/check_in_list.html', context={'form': form})

    def post(self, request):
        bound_form = StudentForm(request.POST)
        if bound_form.is_valid():
            new_student = bound_form.save()
            print(new_student)
            return redirect(new_student)
        return render(request, 'hostel/check_in_list.html', context={'form': bound_form})


class Check_In_student_Update(View):
    def get(self, request, id):
        student = Student.objects.get(id=id)
        bound_form = StudentForm(instance=student)
        return render(request, 'hostel/check_in_update_list.html',
                      context={'bound_form': bound_form, 'student': student})

    def post(self, request, id):
        student = Student.objects.get(id=id)
        bound_form = StudentForm(request.POST, instance=student)
        if bound_form.is_valid():
            new_student = bound_form.save()
            return redirect(new_student)
        return render(request, 'hostel/check_in_update_list.html',
                      context={'bound_form': bound_form, 'student': student})
