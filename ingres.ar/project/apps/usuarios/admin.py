from django.contrib import admin

# Registro el modelo customizado de de usuario (Perfil)

from apps.usuarios.models import Perfil


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('usuario','fecha_nacimiento','foto')
