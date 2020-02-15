from django.urls import path
from .views import number_of, cards


urlpatterns = [
	path('', number_of, name='home_url'),
	path('/rooms/', cards, name='rooms_url'),
]