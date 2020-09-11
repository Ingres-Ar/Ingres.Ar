from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Registro el modelo customizado de de usuario (Perfil)

from apps.usuarios.models import Perfil

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('usuario','fecha_nacimiento','foto')

'''
Para no cambiar de url al asignar perfil (revisar)


class PerfilDeSeguido(admin.StackedInline):
    model = Perfil
    can_delete = False
    verbose_name = 'Perfiles'

class UsuarioAdmin(UserAdmin):
    inlines = (PerfilDeSeguido,)


admin.site.unregister(Perfil)
admin.site.register(Perfil,PerfilDeSeguido)

se puede agregar list_filter, list_editable, list_link, etc.

'''


