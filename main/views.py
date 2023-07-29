from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return HttpResponse('This is your home page')

def rooms(request):
    return HttpResponse('This is your room page')
