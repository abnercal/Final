from django.shortcuts import render
from django.contrib import messages
from .forms import CompraForm
from .models import Compra, Producto, Usuario
# Create your views here.
def compra_nueva(request):
    if request.method == "POST":
        formulario = CompraForm(request.POST)
        if formulario.is_valid():
            pelicula = Pelicula.objects.create(nombre=formulario.cleaned_data['nombre'], anio = formulario.cleaned_data['anio'])
            for actor_id in request.POST.getlist('actores'):
                actuacion = Actuacion(actor_id=actor_id, pelicula_id = pelicula.id)
                actuacion.save()
            messages.add_message(request, messages.SUCCESS, 'Pelicula Guardada Exitosamente')
    else:
        formulario = CompraForm()
    return render(request, 'blog/lista.html', {'formulario': formulario})
