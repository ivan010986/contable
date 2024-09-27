from django.contrib import admin
from .models import CentroCostos, Rubro, Presupuesto, SubRubro

# Register your models here.
class CentroCostosAdmin(admin.ModelAdmin):
    # Especifica los campos que deseas mostrar en la vista de lista
    list_display = ('id','codigo', 'nombre', 'regional', 'uen', 'area')

    list_editable = ('codigo', 'nombre', 'regional', 'uen', 'area')  
    # Para permitir la edición en la vista de lista

    # Campos por los cuales se puede buscar en el panel de administración
    search_fields = ('codigo', 'nombre')

admin.site.register(CentroCostos, CentroCostosAdmin)

class PresupuestoAdmin(admin.ModelAdmin):
    # Especifica los campos que deseas mostrar en la vista de lista
    list_display = ('id','usuario', 'cuenta', 'rubro', 'subrubro', 'item', 'fecha')

    list_editable = ('usuario', 'cuenta', 'rubro', 'subrubro', 'item')  
    # Para permitir la edición en la vista de lista

    # Campos por los cuales se puede buscar en el panel de administración
    search_fields = ('usuario', 'fecha')

admin.site.register(Presupuesto, PresupuestoAdmin)

class SubRubroAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'nombre', 'rubro')
    list_editable = ('codigo', 'nombre', 'rubro')  

admin.site.register(SubRubro, SubRubroAdmin)

admin.site.register(Rubro)
