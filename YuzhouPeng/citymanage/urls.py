from django.urls import path

from . import views

app_name = 'citymanages'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('station/', views.station, name='station'),
    path('emission/', views.emission, name='emission'),
]