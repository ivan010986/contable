from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser, Regional, UEN, Area
from .forms import CustomUserChangeForm, CustomUserCreationForm

class CustomUserAdmin(BaseUserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    list_display = ('id', 'first_name', 'last_name', 'username', 'email', 'display_uen', 'regional', 'area')
    list_editable = ('first_name', 'last_name', 'username', 'email', 'regional', 'area')
    search_fields = ('first_name', 'last_name', 'username', 'email')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'uen', 'regional', 'area')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'last_name', 'email', 'regional', 'uen', 'password1', 'password2')}
        ),
    )
    
    def display_uen(self, obj):
        return ', '.join(uen.nombre for uen in obj.uen.all())
    display_uen.short_description = 'UENs'

    def save_model(self, request, obj, form, change):
        if not change:
            # Guardar contraseña para el nuevo usuario
            obj.set_password(form.cleaned_data['password1'])
        elif form.cleaned_data.get('password1'):
            # Actualizar contraseña si fue cambiada
            obj.set_password(form.cleaned_data['password1'])
        super().save_model(request, obj, form, change)

# Asegúrate de registrar el modelo CustomUser con el admin
admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(Regional)

class UENAdmin(admin.ModelAdmin):
    # Especifica los campos que deseas mostrar en la vista de lista
    list_display = ('id','nombre')
admin.site.register(UEN, UENAdmin)

admin.site.register(Area)