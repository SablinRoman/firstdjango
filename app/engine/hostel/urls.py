from django.urls import path
from .views import hostel_home


urlpatterns = [
	path('', hostel_home),
]