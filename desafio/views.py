from django.shortcuts import render
from .models import Publicacion, Producto, Usuario
from .forms import FormRegistroUsuario, FormRegistroProducto, FormNuevaPublicacion

# Create your views here.
def inicio(request):
    return render(request, "desafio/index.html")

def publicaciones(request):
    formVacio = FormNuevaPublicacion
    if request.method == "POST":
        form = FormNuevaPublicacion(request.POST)
        if form.is_valid():
            formCleaned = form.cleaned_data
            newProd = Publicacion(titulo = formCleaned['titulo'], autorNombre = formCleaned['autorNombre'], autorApellido = formCleaned['autorApellido'])
            newProd.save()
            return render(request, "desafio/publicaciones.html", {"form": formVacio})
    else:
        return render(request, "desafio/publicaciones.html", {"form": formVacio})

def productos(request):
    formVacio = FormRegistroProducto
    if request.method == "POST":
        form = FormRegistroProducto(request.POST)
        if form.is_valid():
            formCleaned = form.cleaned_data
            newPost = Producto(nombre = formCleaned['nombre'], descripcion = formCleaned['descripcion'])
            newPost.save()
            return render(request, "desafio/productos.html", {"form": formVacio})
    else:
        return render(request, "desafio/productos.html", {"form": formVacio})

def usuario(request):
    return render(request, "desafio/usuario.html")

def formUsuario(request):
    if request.method == "POST":
        form = FormRegistroUsuario(request.POST)
        if form.is_valid():
            formCleaned = form.cleaned_data
            newUser = Usuario(username = formCleaned['username'], nombre = formCleaned['nombre'], apellido = formCleaned['apellido'], edad = formCleaned['edad'])
            newUser.save()
            return render(request, "desafio/usuario.html")
    else:
        form = FormRegistroUsuario
        return render(request, "desafio/form.registro.usuario.html", {"form": form})

def busquedaUsuario(request):
    if request.GET.get('nombre', False):
        nombre = request.GET['nombre']
        usuarios = Usuario.objects.filter(nombre__icontains=nombre)
        for usuario in usuarios:
            print(f"{usuario.nombre} se registró como {usuario.username}")
        return render(request, "desafio/form.busqueda.usuario.html", {"usuarios": usuarios})
    else:
        respuesta = "No hay datos registrados"
    return render(request,"desafio/form.busqueda.usuario.html", {"respuesta": respuesta})
