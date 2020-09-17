from django.contrib import admin

# Registro el modelo customizado de de usuario (Perfil)

from apps.usuarios.models import Perfil

admin.site.register(Perfil)
