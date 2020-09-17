from django.urls import path
from . import views

urlpatterns = [
    path('', views.establecimientos, name='establecimientos'),
]