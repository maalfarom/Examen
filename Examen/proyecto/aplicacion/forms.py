from django import forms
from .models import Usuario

class UsuarioModelForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ["nomUsuario","contrasenia"]

    def clean_nomUsuario(self):
        nombre = self.cleaned_data.get("nomUsuario")
        #validaciones
        return nombre

    def clean_contrasenia(self):
        contrasenia = self.cleaned_data.get("contrasenia")
        #validaciones
        return contrasenia

class regUsuario(forms.Form):
    usuario = forms.CharField(max_length=50)
    contraseña = forms.CharField(max_length=50)