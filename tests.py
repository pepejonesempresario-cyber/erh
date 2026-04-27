{% extends 'Incidencias_Almacen/base.html' %}
{% load static %}

{%block h1_titulo%} Detalles Material {%endblock%}
{%block p_texto%} <a href="{% url 'DashBoard'%}"> DashBoard </a> {%endblock%}

{% block cod_css%} 
<link href="{%static 'Incidencias_Almacen/css/Detalles_Material.css'%}" rel="stylesheet"/> {%endblock%}
{% block content %}

<main>
    <div class="info">
        <section class="nom">
            <h2> Aqui va el nombre</h2> 
            <h2> Aqui va el codigo </h2>
        </section>
        <section class="dscrp">
            <p> Aqui va la descripcion extensa </p>
        </section>
    
    </div>
    <div class="extra">
     <h3> Aqui va la Familia</h3>
     <h3> Aqui va la Ubicacion</h3>
     <h3> Aqui va el Proveedor</h3>
    </div>
</main>
{%endblock%}

