from django.shortcuts import render
from django.http import HttpResponse
from .interface import func


def index(request):
    return render(request, 'index.html')
    #  return HttpResponse("Hello, world. You're at the cmdRobot index.")


def arrowMvt(request):
    # TODO : Vérifier code côté JS + Lire le JSON transmis + Checker la config Django
    inst = b'D+020F'
    print("front")
    success = func(inst)
    # success = interface.forward()
    return render(request, 'index.html', {'output': success})