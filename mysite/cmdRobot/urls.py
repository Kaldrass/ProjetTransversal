from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('premierTest', views.premierTest, name='premierTest')
]

