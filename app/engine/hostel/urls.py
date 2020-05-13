from django.urls import path
from .views import *

urlpatterns = [
	path('', number_of, name='home_url'),
	path('add-room/', AddRoom.as_view(), name='add_a_room_url'),
	path('rooms/', Cards.as_view(), name='rooms_url'),
	path('rooms/<str:id>/', Student_detail.as_view(), name='student_detail_url'),
	path('room/<str:room_det>/', Room_detail.as_view(), name='room_detail_url'),
	path('check-in/', Сheck_in_student.as_view(), name='check_in_url'),
	path('rooms/<str:id>/update/', Check_In_student_Update.as_view(), name='check_in_update_url'),
	path('rooms/delete/<str:id>', student_check_out, name='student_check_out_url'),

]