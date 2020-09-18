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
]