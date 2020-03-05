from django import  forms
from .models import Student
from django.core.exceptions import ValidationError



class CheckInForm(forms.Form):
    room = forms.CharField(max_length=8, help_text="ФИО")
    name = forms.CharField(max_length=50, help_text="Комната")
    faculty = forms.CharField(max_length=10, help_text="Факультет")

    room.widget.attrs.update({'class' : 'form-control'})
    name.widget.attrs.update({'class': 'form-control'})
    faculty.widget.attrs.update({'class': 'form-control'})

    def clean_room(self):
        print('i am clean room')
        new_room = self.cleaned_data['room']
        if new_room == '':
            raise ValidationError('Поле комнаты не может быть пустым')

        return new_room

    def save(self):
        new_student = Student.objects.create(room=self.cleaned_data['room'],
                                            name=self.cleaned_data['name'],
                                            faculty=self.cleaned_data['faculty'])
        return new_student




