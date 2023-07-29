from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return render(request, 'home.html')

def rooms(request):
    return render(request, 'rooms.html')
