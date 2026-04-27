from django.db import models

class Proveedor(models.Model):
    cif = models.CharField(max_length=20, unique=True)
    nombre_comercial = models.CharField(max_length=150)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    direccion = models.TextField()

    def __str__(self):
        return self.nombre_comercial

class Operario(models.Model):
    dni = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=150)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"

class Material(models.Model):
    codigo_interno = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    familia = models.CharField(max_length=100)
    ubicacion_habitual = models.CharField(max_length=100)
    
    proveedor_principal = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"[{self.codigo_interno}] {self.nombre}"

class Incidencia(models.Model):
    ESTADOS = [
        ('PENDIENTE', 'Pendiente'),
        ('EN_PROCESO', 'En Proceso'),
        ('RESUELTA', 'Resuelta'),
    ]
    PRIORIDADES = [
        ('BAJA', 'Baja'),
        ('MEDIA', 'Media'),
        ('ALTA', 'Alta'),
        ('URGENTE', 'Urgente'),
    ]

    codigo = models.CharField(max_length=50, unique=True)
    titulo = models.CharField(max_length=200)
    descripcion_detallada = models.TextField()
    fecha_alta = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='PENDIENTE')
    nivel_prioridad = models.CharField(max_length=20, choices=PRIORIDADES, default='MEDIA')
    zona_almacen = models.CharField(max_length=100)
    
    operario_asignado = models.ForeignKey(Operario, on_delete=models.SET_NULL, null=True, blank=True)
    material_afectado = models.ForeignKey(Material, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Incidencia {self.codigo} - {self.titulo}"
