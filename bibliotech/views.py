from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import PerfilUsuario
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .backends import StoredProcedureAuthBackend  

def home(request):
    return render(request, 'pages/home.html')

def login(request):
    return render(request, 'pages/login.html')

#def perfil(request):
    #return render(request, 'pages/perfil.html')

def libros(request):
    return render(request, 'pages/libros.html')

def comentarios(request):
    return render(request, 'pages/comentarios.html')


def custom_login(request):
    error = None
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        next_url = request.POST.get('next', 'pagina_principal')  # URL a redirigir después del login
        
        # Autenticar usando el backend personalizado con procedimiento almacenado
        auth_backend = StoredProcedureAuthBackend()
        user = auth_backend.authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect(next_url)
        else:
            error = "Credenciales inválidas. Por favor intente nuevamente."
    
    return render(request, 'login.html', {
        'error': error,
        'next': request.GET.get('next', '')
    })



@login_required(login_url='custom_login')
def pagina_principal(request):
    return render(request, 'pages/pagina_principal.html')


@login_required(login_url='custom_login')
def perfil_usuario(request):
    try:
        perfil = request.user.perfil  # Acceso directo vía relación OneToOne
    except PerfilUsuario.DoesNotExist:
        perfil = None
    context = {
        'user': request.user,  # datos del usuario autenticado
        'perfil': perfil,
    }
    return render(request, 'pages/perfil.html', context)

@login_required(login_url='custom_login')
def listar_libros(request):
    return render(request, 'pages/listar_libros.html')