from django.urls import path
from .views import number_of, cards, student_detail


urlpatterns = [
	path('', number_of, name='home_url'),
	path('rooms/', cards, name='rooms_url'),
	path('student/<name>/', student_detail, name='student_detail_url'),
]