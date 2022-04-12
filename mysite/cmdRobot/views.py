from django.shortcuts import render
from django.http import HttpResponse
from .interface import func


def index(request):
    return render(request, 'index.html')
    #  return HttpResponse("Hello, world. You're at the cmdRobot index.")


def premierTest(request):
    success = func()
    # success = interface.forward()
    return render(request, 'index.html', {'output': success})

