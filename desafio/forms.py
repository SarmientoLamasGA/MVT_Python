from django import forms

class FormRegistroUsuario(forms.Form):
    username = forms.CharField(max_length=20, required=True)
    nombre = forms.CharField(max_length=40, required=True)
    apellido = forms.CharField(max_length=40, required=True)
    edad = forms.IntegerField(required=True)

class FormRegistroProducto(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    descripcion = forms.CharField(max_length=250)

class FormNuevaPublicacion(forms.Form):
    titulo = forms.CharField(max_length=100, required=True)
    autorNombre = forms.CharField(max_length=40,required=True)
    autorApellido = forms.CharField(max_length=40, required=True)
