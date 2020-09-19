from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login_usuario'),
    path('usuarios/logout', views.logout_view, name='logout_usuario'),
]