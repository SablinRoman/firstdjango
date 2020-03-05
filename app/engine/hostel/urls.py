from django.urls import path
from .views import *


urlpatterns = [
	path('', number_of, name='home_url'),
	path('rooms/', cards, name='rooms_url'),
	path('rooms/<str:student_det>/', Student_detail.as_view(), name='student_detail_url'),
	path('room/<str:room_det>/', Room_detail.as_view(), name='room_detail_url'),
	path('check-in/', Сheck_in_student.as_view(), name='check_in_url'),
]