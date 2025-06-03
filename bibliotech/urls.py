
from django.urls import path, include
from django.conf import settings
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.custom_login,  name='custom_login'),
    path('pagina_principal/', views.pagina_principal, name='pagina_principal'),
    path('perfil/', views.perfil_usuario, name='perfil'),
    path('libros/', views.libros, name='libros'),
    path('comentarios/', views.comentarios, name='comentarios'),
    path('listar_libros/', views.listar_libros, name='listar_libros'),
]

