from django.urls import path
from .views import number_of, cards, student_detail, room_detail
print('==========================================')

urlpatterns = [
	path('', number_of, name='home_url'),
	path('rooms/', cards, name='rooms_url'),
	path('rooms/<str:student_det>/', student_detail, name='student_detail_url'),
	path('room/<str:room_det>/', room_detail, name='room_detail_url'),


]

