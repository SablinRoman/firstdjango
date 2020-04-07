import re
from django import forms
from .models import Student
from .models import Room
from django.core.exceptions import ValidationError


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'faculty', 'form_studies',
                  'group', 'sex', 'mobile_number', 'fluorography', 'pediculosis',
                  'contract_number', 'agreement_date', 'registration', 'citizenship',
                  'date_of_birthday', 'place_of_birthday', 'document_number', 'authority',
                  'date_of_issue', 'notation', 'id'
                  ]
        widgets = {'room': forms.NumberInput(attrs={'class': 'form-control'}),
                   'name': forms.TextInput(attrs={'class': 'form-control'}),
                   'faculty': forms.TextInput(attrs={'class': 'form-control'}),
                   # 'place_status': forms.TextInput(attrs={'class': 'form-control'}),
                   'form_studies': forms.Select(attrs={'class': 'form-control'}),
                   'group': forms.TextInput(attrs={'class': 'form-control'}),
                   'sex': forms.Select(attrs={'class': 'form-control'}),
                   'mobile_number': forms.TextInput(attrs={'class': 'form-control'}),
                   'fluorography': forms.CheckboxInput(attrs={'class': 'form-control'}, ),
                   'pediculosis': forms.CheckboxInput(attrs={'class': 'form-control'}),
                   'contract_number': forms.TextInput(attrs={'class': 'form-control'}),
                   'agreement_date': forms.DateInput(attrs={'class': 'form-control'}),
                   'registration': forms.DateInput(attrs={'class': 'form-control'}),
                   'citizenship': forms.TextInput(attrs={'class': 'form-control'}),
                   'date_of_birthday': forms.DateInput(attrs={'class': 'form-control'}),
                   'place_of_birthday': forms.TextInput(attrs={'class': 'form-control'}),
                   'document_number': forms.TextInput(attrs={'class': 'form-control'}),
                   'authority': forms.TextInput(attrs={'class': 'form-control'}),
                   'date_of_issue': forms.DateInput(attrs={'class': 'form-control'}),
                   'notation': forms.TextInput(attrs={'class': 'form-control'}),
                   'id': forms.TextInput(attrs={'class': 'form-control'}),
                   }

    def clean(self):
        cleaned_data = super(CheckInForm, self).clean()
        new_room = cleaned_data.get('room')

        if Student.objects.filter(room=new_room).count() > 3:
            if self.instance.pk is not None:  # if edit then filter with id
                if not Student.objects.filter(room=new_room, id=self.instance.pk):
                    raise ValidationError('Комната уже заполнена!')
            else:
                raise ValidationError('Комната уже заполнена!')

    def clean_room(self):
        # Добавить защиту от ввода буквенных значений
        new_room = self.cleaned_data['room']
        if new_room == '':
            raise ValidationError('Поле комнаты не может быть пустым!')

        return new_room

    # def clean_name(self):
    #     new_name = self.cleaned_data['name']
    #     frmt = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя- '
    #     for i in new_name:
    #         if i.lower() not in frmt:
    #             raise ValidationError('ФИО может содеражать только буквенные символы!')
    #     return new_name

    def clean_faculty(self):
        new_faculty = self.cleaned_data['faculty']
        if new_faculty:
            new_faculty = new_faculty.upper()
            if new_faculty in ['РТФ', 'РКФ', 'ФВС', 'ФСУ', 'ФЭТ', 'ЭФ',
                               'ГФ', 'ЮФ', 'ФИТ', 'ФБ', 'ЦОИГ', 'ЗАОЧНИК']:
                return new_faculty
            raise ValidationError('Введен несуществующий факультет!')

    def clean_mobile_number(self):
        new_number = self.cleaned_data['mobile_number']
        #  Проверна на наличие буквенных символов не отрабатывает
        if new_number is not None:
            if not str(new_number).isdigit():
                raise ValidationError('Номер телефона  может содеражать только цифры!')
            if len(str(new_number)) != 11:
                raise ValidationError('Количество цифр не равно 11!')
        return new_number

    def clean_contract_number(self):
        pass


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_numb']
        widgets = {'room_numb': forms.NumberInput(attrs={'class': 'form-control'})}
