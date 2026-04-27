from django.urls import path
from . import views

urlpatterns = [
    path('DashBoard/', views.dashboard, name='DashBoard'),
    
    # Incidencias
    path('Lista/', views.IncidenciaListView.as_view(), name='Listado'),
    path('Detalles/<int:pk>/', views.IncidenciaDetailView.as_view(), name='Detalles'),
    path('Registrar/', views.Registrar, name='Registrar'),
    path('Borrar/<int:pk>/', views.Borrar, name='Borrar'),
    
    # Materiales
    path('Lista_Material/', views.MaterialListView.as_view(), name='Lista_Material'),
    path('RegistrarM/', views.RegistrarM, name='RegistrarM'),
    path('DetallesM/<int:pk>/', views.MaterialDetailView.as_view(), name='DetalleM'),
    
    # Proveedores
    path('ListaP/', views.ProveedorListView.as_view(), name='Lista_Proveedor'),
    path('RegistrarP/', views.RegistrarP, name='RegistrarP'),
    path('DetallesP/<int:pk>/', views.ProveedorDetailView.as_view(), name='DetallesP'),
]