from django.contrib import admin
from .models import Usuario,Tienda,Producto,Lista,DetalleTienda,DetalleLista
# Register your models here.

class AdminAuto(admin.ModelAdmin):
    list_display = [""]

admin.site.register(Usuario)
admin.site.register(Producto)
admin.site.register(Lista)
admin.site.register(DetalleLista)
admin.site.register(DetalleTienda)
admin.site.register(Tienda)