from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Establecimiento)
admin.site.register(Localizacion)
admin.site.register(Domicilio)
admin.site.register(Oferta)
admin.site.register(Orientacion)
