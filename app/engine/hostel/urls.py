from django.urls import path
from .views import number_of, cards, room_detail
print('==========================================')

urlpatterns = [
	path('', number_of, name='home_url'),
	path('rooms/', cards, name='rooms_url'),
	path('rooms/<str:room>/', room_detail, name='room_detail_url'),

]

