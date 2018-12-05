from django.db import models

# Create your models here.

class Usuario(models.Model):
    nomUsuario = models.CharField(max_length=50, primary_key=True)
    contrasenia = models.CharField(max_length=30)

class Lista(models.Model):
    nombreLista = models.CharField(max_length=50)
    total =  models.IntegerField()
    nombreUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Producto(models.Model):
    nombreProducto = models.CharField(max_length=50)

class Tienda(models.Model):
    nombreTienda = models.CharField(max_length=50, primary_key=True)
    nombreSucursal = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)

class DetalleLista(models.Model):
    idLista = models.ForeignKey(Lista, on_delete=models.CASCADE)
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)

class DetalleTienda(models.Model):
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    nombreTienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)
    precio = models.IntegerField()
