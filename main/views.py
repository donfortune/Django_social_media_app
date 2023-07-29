from django.shortcuts import render


def homepage(request):
    return render(request, 'home.html')

def rooms(request):
    return render(request, 'rooms.html')
