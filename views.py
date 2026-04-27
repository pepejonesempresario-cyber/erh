{% extends 'Incidencias_Almacen/base.html' %}
{% load static %}

{%block cod_css%} 
    <link href="{% static 'Incidencias_Almacen/css/Lista_Materiales.css'%}" rel="stylesheet"> 
{%endblock%}
{% block h1_titulo%} Lista Materiales  {% endblock %}
{% block p_texto%} <a href="{% url 'DashBoard'%}">  Dashboard  </a> {% endblock%}

{%block content%}
<main>
    <table>
        <thead> 
            <tr> 
                <th> Código </th> <th> Nombre </th> <th> Familia </th> <th> Ubicacion </th> <th> Proveedor</th> <th> Acciones</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td> -- </td> <td> -- </td>  <td> -- </td> <td> -- </td> <td> -- </td> <td> <span class="ac">  Detalles </span> <span class="acc" > quitar </span> </td>
            </tr>
            <tr>
                <td> -- </td> <td> -- </td> <td> -- </td> <td> -- </td> <td> -- </td> <td>  <span class="ac">  Detalles </span> <span class="acc" > quitar </span>  </td>
            </tr>
        </tbody>
    </table>
</main>

{%endblock%}