from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from django.db import connection

class StoredProcedureAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            with connection.cursor() as cursor:
                # Llamar al procedimiento almacenado
                cursor.callproc('sp_autenticar_usuario', [username, password])
                result = cursor.fetchone()
            
            if result and result[0]:  # Si el procedimiento retorna un ID de usuario válido
                # Obtener o crear el usuario en Django
                user, created = User.objects.get_or_create(
                    username=username,
                    defaults={
                        'is_active': True,
                        'is_staff': False,
                        'is_superuser': False
                    }
                )
                return user
        except Exception as e:
            print(f"Error en autenticación: {e}")
        return None
 
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None