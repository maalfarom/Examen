from django.shortcuts import render
from django.contrib.auth import authenticate,login
from .forms import regUsuario, UsuarioModelForm
from .models import Usuario

# Create your views here.

def index(request):
    form = UsuarioModelForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        # form_data = form.cleaned_data
        # abc = form_data.get("usuario")
        # abc2 = form_data.get("contraseña")
        # obj = Usuario.objects.create(nomUsuario=abc, contrasenia=abc2)
    context = {
        "el_form": form,
    }
    return render(request, 'aplicacion/index.html',context)

def loginn(request):
    return render(request, 'aplicacion/login.html')

def registro(request):
    
    return render(request, 'aplicacion/registro.html')