{% extends 'Incidencias_Almacen/base.html' %}
{% load static %}

{% block h1_titulo %} Registrar Material {% endblock %}
{% block p_texto %} <a href="{% url 'DashBoard'%}"> DashBoard </a> {% endblock %}

{% block cod_css %}
    <link href="{% static 'Incidencias_Almacen/css/Registrar_Material.css'%}" rel="stylesheet"/>
{%endblock%}


{% block content %}

<main>
    <form method="post">
        {% csrf_token %}

        
        <section class="info">
            <h2> Información Principal </h2>
            <label for="nombre"> Nombre </label>
            <input type="text" maxlength="100" required name="nombre" id="nombre">

            <label for="cod"> Código </label>
            <input type="number" max="10000" name="cod" required id="cod">

            <label for="dscrp"> Descripción </label>
            <textarea name="dscrp" rows="10" cols="30" required id="dscrp"> Poner Descripción</textarea>
        

        </section>
        
        <section class="slcts">
            <h2> Información Adicional </h2>
            <label for="fam"> Familia </label>
            <select name="fam" required id="fam">
                <option> Familia 1</option>
                <option> Familia 2</option>
                <option> Familia 3</option>
                <option> Familia 4</option>
                <option> Familia 5</option>
                <option> Familia 6</option>
                <option> Familia 7</option>
                <option> Familia 8</option>
                <option> Familia 9</option>
            </select>

            <label for="ubi"> Ubicación </label>
            <select name="ubi" required id="ubi">
                <option> Zona 1</option>
                <option> Zona 2</option>
                <option> Zona 3</option>
                <option> Zona 4</option>
                <option> Zona 5</option>
                <option> Zona 6</option>
                <option> Zona 7</option>
                <option> Zona 8</option>
                <option> Zona 9</option>
                <option> Zona 10</option>
            </select>
            <label name = 'proveedor'> Proveedor </label>
            <select name="proveedor" required id="proveedor">
                <option> Proveedor 1</option>
                <option> Proveedor 2</option>
                <option> Proveedor 3</option>
                <option> Proveedor 4</option>
                <option> Proveedor 5</option>
                <option> Proveedor 6</option>
                <option> Proveedor 7</option>
                <option> Proveedor 8</option>
            </select>

            <input type="submit" name="sbmt" value="Registrar" id="btn">
        </section>

    </form>
</main>

{% endblock %}