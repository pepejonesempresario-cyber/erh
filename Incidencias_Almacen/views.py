from django.shortcuts import render

def dashboard(request):
    return render(request, 'Incidencias_Almacen/DashBoard.html')

def lista(request):
    return render(request , 'Incidencias_Almacen/lista_incidencia.html')

def Detalles(request):
    return render(request, 'Incidencias_Almacen/Detalle_Incidencia.html')

def Registrar(request):
    return render (request, 'Incidencias_Almacen/Registrar_Incidencia.html')

def Lista_Material(request):
    return render(request, 'Incidencias_Almacen/Lista_Materiales.html')

def DetallesM(request):
    return render(request, 'Incidencias_Almacen/Detalles_Material.html')

def RegistrarM(request):
    return render(request, 'Incidencias_Almacen/Registrar_Material.html')

def Borrar(request):
    return render(request, 'Incidencias_Almacen/confirmar_borrado.html')

def Lista_Proveedores(request):
    return render(request, 'Incidencias_Almacen/Lista_Proveedores.html')

def DetallesP(request):
    return render(request, 'Incidencias_Almacen/Detalles_Proveedor.html')

def RegistrarP(request):
    return render(request, 'Incidencias_Almacen/Registrar_Proveedor.html')