from django.urls import path

from desafio import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('publicaciones/', views.publicaciones, name="publicaciones"),
    path('productos/', views.productos, name="productos"),
    path('usuario/', views.usuario, name="usuario"),
    path('usuario/registro/', views.formUsuario, name="form.registro.usuario"),
    path('usuario/busqueda/', views.busquedaUsuario, name='form.busqueda.usuario'),
]