from django.db import models
from django.shortcuts import reverse


class Student(models.Model):
    FORM_STUDIES_CHOICES = (
        ('БЮДЖЕТ', 'Бюджет'),
        ('ПВЗ', 'ПВЗ')
    )

    SEX_CHOICES = (
        ('М', 'Мужской'),
        ('Ж', 'Женский')
    )
    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=50,
                            db_index=True)

    place_status = models.CharField(max_length=25,
                                    db_index=True,
                                    default='пусто')

    room = models.IntegerField(db_index=True,
                               blank=True)

    faculty = models.CharField(max_length=10,
                               db_index=True,
                               blank=True,
                               null=True)

    form_studies = models.CharField(max_length=10,
                                    db_index=True,
                                    choices=FORM_STUDIES_CHOICES,
                                    blank=True,
                                    null=True)

    group = models.CharField(max_length=10,
                             db_index=True,
                             blank=True,
                             null=True)

    sex = models.CharField(max_length=2,
                           db_index=True,
                           choices=SEX_CHOICES,
                           blank=True,
                           null=True)

    mobile_number = models.BigIntegerField(db_index=True,
                                           blank=True,
                                           null=True)

    fluorography = models.BooleanField(db_index=True,
                                       default=False)

    pediculosis = models.BooleanField(db_index=True,
                                      default=False)

    contract_number = models.CharField(max_length=15,
                                       db_index=True,
                                       blank=True,
                                       null=True)

    agreement_date = models.DateField(blank=True,
                                      null=True)

    registration = models.DateField(blank=True,
                                    null=True)

    citizenship = models.CharField(max_length=20,
                                   db_index=True,
                                   blank=True,
                                   null=True)

    date_of_birthday = models.DateField(blank=True,
                                        null=True)

    place_of_birthday = models.CharField(max_length=70,
                                         db_index=True,
                                         blank=True,
                                         null=True)

    document_number = models.CharField(max_length=20,
                                       db_index=True,
                                       blank=True,
                                       null=True)

    authority = models.CharField(max_length=100,
                                 blank=True,
                                 null=True)

    date_of_issue = models.DateField(blank=True,
                                     null=True)

    notation = models.TextField(db_index=True,
                                blank=True,
                                null=True)

    def get_absolute_url(self):
        id = self.id
        return reverse('student_detail_url', kwargs={'id': id})

    def room_url(self):
        url = self.room
        return reverse('room_detail_url', kwargs={'room_det': url})

    def __str__(self):
        return self.name
