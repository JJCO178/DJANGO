from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

# Tabla niveles escolares
class NivelEscolar(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

# Tabla perfil_usuario
class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')  # Relación uno a uno con User
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    biografia = models.TextField(blank=True, null=True)
    nivel_escolar = models.ForeignKey(NivelEscolar, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'Perfil de {self.user.username}'
    
    
    
class Alumno(models.Model):
    # Relación con el usuario principal (en la base de datos default)
    user_id = models.IntegerField()  # Obligatorio
    nivel_escolar_id = models.IntegerField()  # Nuevo campo
    dni = models.CharField(
        _('DNI'),
        max_length=8,
        unique=True
    )
    
    enfermedades = models.TextField(
        _('Enfermedades o condiciones crónicas'),
        blank=True,
        null=True
    )
    
    alergias = models.TextField(
        _('Alergias conocidas'),
        blank=True,
        null=True
    )
    
    tipo_sangre = models.CharField(
        _('Tipo de sangre'),
        max_length=5,
        blank=True,
        null=True
    )
    
    tutor_legal = models.CharField(
        _('Tutor legal del menor'),
        max_length=255
    )
    
    telefono_emergencias = models.CharField(
        _('Teléfono para emergencias'),
        max_length=20
    )
    
    medico_cabecera = models.CharField(
        _('Médico/Pediatra de cabecera'),
        max_length=255,
        blank=True,
        null=True
    )
    
    centro_medico = models.CharField(
        _('Centro médico afiliado'),
        max_length=255,
        blank=True,
        null=True
    )
    
    numero_hermanos = models.PositiveIntegerField(
        _('Hermanos en el colegio'),
        default=0
    )
    
    @property
    def user(self):
        try:
            from django.contrib.auth.models import User
            return User.objects.using('default').get(pk=self.user_id)
        except User.DoesNotExist:
            return None

    @property
    def nivel_escolar(self):
        try:
            from bibliotech.models import NivelEscolar
            return NivelEscolar.objects.using('default').get(pk=self.nivel_escolar_id)
        except NivelEscolar.DoesNotExist:
            return None
    class Meta:
        verbose_name = _('Alumno')
        verbose_name_plural = _('Alumnos')
        db_table = 'alumnos'  # Nombre personalizado para la tabla

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.dni}"


class Docente(models.Model):
    TIPO_CONTRATO_CHOICES = [
        ('PLANTA', _('Planta')),
        ('CONTRATADO', _('Contratado')),
        ('SUPLENTE', _('Suplente')),
    ]

    user_id = models.IntegerField()  # ID del User en BD principal
    
    dni = models.CharField(
        _('DNI'),
        max_length=8,
        unique=True
    )
    
    fecha_contratacion = models.DateField(
        _('Fecha de contratación')
    )
    
    codigo_modular = models.CharField(
        _('Código Modular'),
        max_length=20,
        unique=True
    )
    
    codigo_colegio_profesores = models.CharField(
        _('Código Colegio de Profesores'),
        max_length=20,
        unique=True
    )
    
    cursos_dictados = models.TextField(
        _('Cursos a dictar'),
        help_text=_("Separar cursos por comas")
    )
    
    telefono_emergencias = models.CharField(
        _('Teléfono para emergencias'),
        max_length=20
    )
    
    tipo_contrato = models.CharField(
        _('Tipo de contrato'),
        max_length=20,
        choices=TIPO_CONTRATO_CHOICES
    )
    
    def user(self):
        try:
            from django.contrib.auth.models import User
            return User.objects.using('default').get(pk=self.user_id)
        except User.DoesNotExist:
            return None


    class Meta:
        verbose_name = _('Docente')
        verbose_name_plural = _('Docentes')
        db_table = 'docentes'  # Nombre personalizado para la tabla

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.codigo_modular}"