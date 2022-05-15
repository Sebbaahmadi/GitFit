from . import views
from django.urls import path


urlpatterns = [
    path('', views.Home,name='Home'),
    path('about', views.about,name='about'),
    path('contact', views.contact,name='contact')
]
