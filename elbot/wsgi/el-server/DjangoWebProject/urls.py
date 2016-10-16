from datetime import datetime
from django.conf.urls import url
#from app.forms import BootstrapAuthenticationForm
from app import views
import django.contrib.auth.views

urlpatterns = [
    url(r'^elapp', views.elapp, name='elapp'),
    url(r'^test_weather/(?P<location>\w+)/', views.test_weather, name='test_weather'),
    url(r'^weather_picture/(?P<weather>\w+)/(?P<size>\d+).jpg/', views.weather_picture),
    url(r'^whattoeat_picture/(?P<choose>\w+)/(?P<random_num>\d+)/(?P<size>\d+).jpg/', views.whattoeat_picture),
    url(r'^button_picture/(?P<button>\w+)/(?P<size>\d+).jpg/', views.button_picture),
 #  url(r'^weather_picture/(?P<weather>\w+)/(?P<size>\d+).jpg/', views.weather_picture),
]
