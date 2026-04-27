from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Incidencia, Material, Proveedor
from .forms import IncidenciaForm, MaterialForm, ProveedorForm

# La vista dashboard la mantenemos como función 
def dashboard(request):
    ultimas_incidencias = Incidencia.objects.order_by('-fecha_alta')[:5]
    return render(request, 'Incidencias_Almacen/DashBoard.html', {'ultimas_incidencias': ultimas_incidencias})

# =======================
# INCIDENCIAS
# =======================
class IncidenciaListView(ListView):
    model = Incidencia
    template_name = 'Incidencias_Almacen/lista_incidencia.html'
    context_object_name = 'incidencias'
    queryset = Incidencia.objects.order_by('titulo')

class IncidenciaDetailView(DetailView):
    model = Incidencia
    template_name = 'Incidencias_Almacen/Detalle_Incidencia.html'
    context_object_name = 'incidencia'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalles de la Incidencia'
        return context

def Registrar(request):
    if request.method == 'POST':
        form = IncidenciaForm(request.POST)
        if form.is_valid():
            Incidencia.objects.create(
                codigo=form.cleaned_data['codigo'],
                titulo=form.cleaned_data['titulo'],
                descripcion_detallada=form.cleaned_data['descripcion_detallada'],
                estado=form.cleaned_data['estado'],
                nivel_prioridad=form.cleaned_data['nivel_prioridad'],
                zona_almacen=form.cleaned_data['zona_almacen'],
                operario_asignado=form.cleaned_data['operario_asignado'],
                material_afectado=form.cleaned_data['material_afectado']
            )
            return redirect('Listado')
    else:
        form = IncidenciaForm()
    return render(request, 'Incidencias_Almacen/Registrar_Incidencia.html', {'form': form})

def Borrar(request, pk):
    incidencia = get_object_or_404(Incidencia, pk=pk)
    if request.method == 'POST':
        incidencia.delete()
        return redirect('Listado')
    return render(request, 'Incidencias_Almacen/confirmar_borrado.html', {'incidencia': incidencia})

# =======================
# MATERIALES
# =======================
class MaterialListView(ListView):
    model = Material
    template_name = 'Incidencias_Almacen/Lista_Materiales.html'
    context_object_name = 'materiales'
    queryset = Material.objects.order_by('nombre')

class MaterialDetailView(DetailView):
    model = Material
    template_name = 'Incidencias_Almacen/Detalles_Material.html'
    context_object_name = 'material'

def RegistrarM(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            Material.objects.create(
                codigo_interno=form.cleaned_data['codigo_interno'],
                nombre=form.cleaned_data['nombre'],
                descripcion=form.cleaned_data['descripcion'],
                familia=form.cleaned_data['familia'],
                ubicacion_habitual=form.cleaned_data['ubicacion_habitual'],
                proveedor_principal=form.cleaned_data['proveedor_principal']
            )
            return redirect('Lista_Material')
    else:
        form = MaterialForm()
    return render(request, 'Incidencias_Almacen/Registrar_Material.html', {'form': form})

# =======================
# PROVEEDORES
# =======================
class ProveedorListView(ListView):
    model = Proveedor
    template_name = 'Incidencias_Almacen/Lista_Proveedores.html'
    context_object_name = 'proveedores'
    queryset = Proveedor.objects.order_by('nombre_comercial')

class ProveedorDetailView(DetailView):
    model = Proveedor
    template_name = 'Incidencias_Almacen/Detalles_Proveedor.html'
    context_object_name = 'proveedor'

def RegistrarP(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            Proveedor.objects.create(
                cif=form.cleaned_data['cif'],
                nombre_comercial=form.cleaned_data['nombre_comercial'],
                email=form.cleaned_data['email'],
                telefono=form.cleaned_data['telefono'],
                direccion=form.cleaned_data['direccion']
            )
            return redirect('Lista_Proveedor')
    else:
        form = ProveedorForm()
    return render(request, 'Incidencias_Almacen/Registrar_Proveedor.html', {'form': form})