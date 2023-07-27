
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def homepage(request):
    return HttpResponse('This is your home page')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
]
