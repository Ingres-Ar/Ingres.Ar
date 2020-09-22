from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login_usuario'),
    path('logout', views.logout_view, name='logout_usuario'),
    path('registro_usuario', views.register_view, name='registro_usuario'),

]