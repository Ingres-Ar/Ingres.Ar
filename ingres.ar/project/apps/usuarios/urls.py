<<<<<<< HEAD
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login_usuario'),
    path('logout', views.logout_view, name='logout_usuario'),
    path('registro_usuario', views.register_view, name='registro_usuario'),

=======
from django.urls import path, include
from apps.usuarios import views

app_name='users'

urlpatterns=[
    path('',views.index,name='index'),
    path('special/',views.special,name='special'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('login/', views.login, name='login'),
    path('login/', views.login, name='login'),
    path('user_login', views.user_login, name='user_login'),
>>>>>>> 3a3db568bc364d097d4b79eee899a79c6afff60a
]