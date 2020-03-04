from django.urls import path
from .views import *


urlpatterns = [
	path('', number_of, name='home_url'),
	path('rooms/', cards, name='rooms_url'),
	path('rooms/<str:student_det>/', student_detail, name='student_detail_url'),
	path('room/<str:room_det>/', room_detail, name='room_detail_url'),
	path('check-in/', check_in_student, name='check_in_url'),
]

