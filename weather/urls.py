from django.contrib import admin
from django.urls import path
from .views import HomeView, weather_view, nasa_data


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('weather/', weather_view, name='weather_view'),
    path('weather/nasa_data/', nasa_data, name='nasa_data'),   
]