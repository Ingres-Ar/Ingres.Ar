from django.urls import path
from . import views

urlpatterns = [
    path('', views.autoevaluacion, name='autoevaluacion'),
]