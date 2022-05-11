from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('frontTest', views.frontTest, name='frontTest'),
    path('backTest', views.backTest, name='backTest'),
    path('leftTest', views.leftTest, name='leftTest'),
    path('rightTest', views.rightTest, name='rightTest')
]

