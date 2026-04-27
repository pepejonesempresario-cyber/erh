from django import forms
from .models import Incidencia, Material, Proveedor, Operario

class IncidenciaForm(forms.Form):
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

    codigo = forms.CharField(label="Código", max_length=50)
    titulo = forms.CharField(label="Título", max_length=200)
    descripcion_detallada = forms.CharField(label="Descripción detallada", widget=forms.Textarea)
    estado = forms.ChoiceField(label="Estado", choices=ESTADOS)
    nivel_prioridad = forms.ChoiceField(label="Nivel de prioridad", choices=PRIORIDADES)
    zona_almacen = forms.CharField(label="Zona almacén", max_length=100)
    
    operario_asignado = forms.ModelChoiceField(label="Operario Asignado", queryset=Operario.objects.all(), required=False)
    material_afectado = forms.ModelChoiceField(label="Material Afectado", queryset=Material.objects.all(), required=False)


class MaterialForm(forms.Form):
    codigo_interno = forms.CharField(label="Código Interno", max_length=50)
    nombre = forms.CharField(label="Nombre", max_length=150)
    descripcion = forms.CharField(label="Descripción", widget=forms.Textarea)
    familia = forms.CharField(label="Familia", max_length=100)
    ubicacion_habitual = forms.CharField(label="Ubicación habitual", max_length=100)
    
    proveedor_principal = forms.ModelChoiceField(label="Proveedor", queryset=Proveedor.objects.all(), required=False)


class ProveedorForm(forms.Form):
    cif = forms.CharField(label="CIF", max_length=20)
    nombre_comercial = forms.CharField(label="Nombre Comercial", max_length=150)
    email = forms.EmailField(label="Email")
    telefono = forms.CharField(label="Teléfono", max_length=20)
    direccion = forms.CharField(label="Dirección", widget=forms.Textarea)

