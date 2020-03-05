from django import  forms
from .models import Student
from django.core.exceptions import ValidationError



class CheckInForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['room', 'name', 'faculty']

        widgets = {'room' : forms.TextInput(attrs={'class' : 'form-control'}),
                  'name' : forms.TextInput(attrs={'class' : 'form-control'}),
                  'faculty' : forms.TextInput(attrs={'class' : 'form-control'}),
                  }

    def clean_room(self):
        print('i am clean room')
        new_room = self.cleaned_data['room']
        if new_room == '':
            raise ValidationError('Поле комнаты не может быть пустым')

        return new_room




