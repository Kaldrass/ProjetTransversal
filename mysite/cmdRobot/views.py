from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')
    #  return HttpResponse("Hello, world. You're at the cmdRobot index.")
