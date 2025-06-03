from django.contrib import admin
from .models import NivelEscolar, PerfilUsuario, Alumno, Docente

# Register your models here.
admin.site.register(NivelEscolar)
admin.site.register(PerfilUsuario)
admin.site.register(Alumno)
admin.site.register(Docente) 