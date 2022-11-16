from django.db import models

# Create your models here.
class Usuario(models.Model):
    username = models.CharField(max_length=20, unique=True, null=False)
    nombre = models.CharField(max_length=40, null=False)
    apellido = models.CharField(max_length=40,null=False)
    edad = models.IntegerField(null=False)

class Publicacion(models.Model):
    titulo = models.CharField(max_length=100,null=False)
    autorNombre = models.CharField(max_length=40,null=False)
    autorApellido = models.CharField(max_length=40,null=False)

class Producto(models.Model):
    nombre = models.CharField(max_length=50,null=False)
    descripcion = models.CharField(max_length=250,null=False)