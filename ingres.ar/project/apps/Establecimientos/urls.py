
from django.urls import path
from . import views

urlpatterns = [
    path('', views.establecimientos, name='establecimientos'),
    path('buscar_colegios', views.filtro, name='buscar_colegios'),
    #path('info_establecimientos', views.listing, name='info_establecimientos'),
    path('info/<int:pk>/', views.info_e, name='info_e'),
    #path('info_e', views.info_e, name='info_e'),
    #path("<int:id>/", views.info_e, name="info_e"),
]