from django.urls import path
from .views import number_of


urlpatterns = [
	path('', number_of),
]