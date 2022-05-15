from . import views
from django.urls import path


urlpatterns = [
    path('FullBody', views.FullBody,name='FullBody'),
    path('Legs', views.Legs,name='Legs'),
    path('strength', views.strength,name='strength')
]