from django.urls import path
from apps.Home import views
from . import views

urlpatterns = [
    path('', views.login_view, name='login_usuario'),
    #path('', views.login_view, name='login_usuario'),
    path('logout_usuario', views.logout_view, name='logout_usuario'),
    path('registro_usuario', views.register_view, name='registro_usuario'),

]