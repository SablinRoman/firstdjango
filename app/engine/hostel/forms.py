from django import  forms
from .models import Student
from django.core.exceptions import ValidationError



class CheckInForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['room', 'name', 'faculty', 'place_status', 'form_studies',
                  'group', 'sex', 'mobile_number', 'fluorography', 'pediculosis',
                  'contract_number', 'agreement_date', 'registration', 'citizenship',
                  'date_of_birthday', 'place_of_birthday', 'document_number', 'authority',
                  'date_of_issue', 'notation'
                  ]

        widgets = { 'room' : forms.TextInput(attrs={'class' : 'form-control'}),
                    'name' : forms.TextInput(attrs={'class' : 'form-control'}),
                    'faculty' : forms.TextInput(attrs={'class' : 'form-control'}),
                    'place_status': forms.TextInput(attrs={'class': 'form-control'}),
                    'form_studies': forms.TextInput(attrs={'class': 'form-control'}),
                    'group': forms.TextInput(attrs={'class': 'form-control'}),
                    'sex': forms.TextInput(attrs={'class': 'form-control'}),
                    'mobile_number': forms.TextInput(attrs={'class': 'form-control'}),
                    'fluorography': forms.TextInput(attrs={'class': 'form-control'}),
                    'pediculosis' : forms.TextInput(attrs={'class' : 'form-control'}),
                    'contract_number' : forms.TextInput(attrs={'class' : 'form-control'}),
                    'agreement_date': forms.TextInput(attrs={'class': 'form-control'}),
                    'registration': forms.TextInput(attrs={'class': 'form-control'}),
                    'citizenship': forms.TextInput(attrs={'class': 'form-control'}),
                    'date_of_birthday': forms.TextInput(attrs={'class': 'form-control'}),
                    'place_of_birthday': forms.TextInput(attrs={'class': 'form-control'}),
                    'document_number': forms.TextInput(attrs={'class': 'form-control'}),
                    'authority': forms.TextInput(attrs={'class': 'form-control'}),
                    'date_of_issue': forms.TextInput(attrs={'class': 'form-control'}),
                    'notation': forms.TextInput(attrs={'class': 'form-control'}),
                  }

    def clean_room(self):
        new_room = self.cleaned_data['room']
        if new_room == '':
            raise ValidationError('Поле комнаты не может быть пустым')

        return new_room




