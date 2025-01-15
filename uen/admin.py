from django.contrib import admin
from .models import CentroCostos, Rubro, Presupuesto, SubRubro, Auxiliar, PresupuestoProyectado, SubRubroAlt, MonthlyTotal, RubroTotal, PresupuestoActualizado, PresupuestoMes

# Register your models here.
class CentroCostosAdmin(admin.ModelAdmin):
    # Especifica los campos que deseas mostrar en la vista de lista
    list_display = ('id','codigo', 'nombre', 'regional', 'uen', 'area')

    list_editable = ('codigo', 'nombre', 'regional', 'uen', 'area')  
    # Para permitir la edición en la vista de lista

    # Campos por los cuales se puede buscar en el panel de administración
    search_fields = ('codigo', 'nombre')

admin.site.register(CentroCostos, CentroCostosAdmin)

class PresupuestoProyectadoInline(admin.TabularInline): 
    model = PresupuestoProyectado
    extra = 0  # Number of extra blank fields to display
    
class PresupuestoAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'uen', 'fecha')
    search_fields = ('usuario', 'fecha')
    inlines = [PresupuestoProyectadoInline]

from django.contrib import admin
from .models import Auxiliar, SubRubro, SubRubroAlt, Rubro, MonthlyTotal, RubroTotal, PresupuestoActualizado, PresupuestoMes, Presupuesto

class AuxiliarAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nombre']  # Asegúrate de que estos campos existen en el modelo Auxiliar
    list_editable = ['nombre']  # Asegúrate de que estos campos existen en el modelo Auxiliar

class SubRubroAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nombre']  # Asegúrate de que estos campos existen en el modelo SubRubro
    list_editable = ['nombre']  # Asegúrate de que estos campos existen en el modelo SubRubro

class SubRubroAltAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nombre']  # Asegúrate de que estos campos existen en el modelo SubRubroAlt
    list_editable = ['nombre']  # Asegúrate de que estos campos existen en el modelo SubRubroAlt
    list_display_links = ['codigo']  # Configurar list_display_links para usar list_editable

class RubroAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nombre']  # Asegúrate de que estos campos existen en el modelo Rubro
    list_editable = ['nombre']  # Asegúrate de que estos campos existen en el modelo Rubro
    list_display_links = ['codigo']  # Configurar list_display_links para usar list_editable


admin.site.register(Auxiliar, AuxiliarAdmin)
admin.site.register(SubRubro, SubRubroAdmin)
admin.site.register(SubRubroAlt, SubRubroAltAdmin)
admin.site.register(Rubro, RubroAdmin)
admin.site.register(MonthlyTotal)
admin.site.register(RubroTotal)
admin.site.register(PresupuestoActualizado)
admin.site.register(PresupuestoMes)
admin.site.register(Presupuesto)