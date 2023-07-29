
from django.urls import path  #import the main projects url path
from . import views #import views from app views file


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('rooms/', views.homepage, name='rooms'),



]
