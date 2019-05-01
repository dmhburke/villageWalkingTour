from django.urls import path
from . import views

urlpatterns = [
    path('', views.agenda, name='agenda'),
    path('hotelchelsea', views.hotelchelsea, name='hotelchelsea'),
    path('washingtonsqpark', views.washingtonsqpark, name='washingtonsqpark'),
    path('gerdes', views.gerdes, name='gerdes'),
    path('bleecker', views.bleecker, name='bleecker'),
    path('macdougal', views.macdougal, name='macdougal'),
    path('cafewha', views.cafewha, name='cafewha'),
    path('jones', views.jones, name='jones'),
]
