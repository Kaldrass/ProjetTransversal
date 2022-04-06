from django.shortcuts import render
from django.http import HttpResponse


# import interface


def index(request):
    return render(request, 'index.html')
    #  return HttpResponse("Hello, world. You're at the cmdRobot index.")


def premierTest(request):
    success = ":)"
    # success = interface.forward()
    return render(request, 'index.html', {'output': success})
