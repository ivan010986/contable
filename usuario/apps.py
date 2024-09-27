from django.apps import AppConfig
from django.conf import settings
import os

class UsuarioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'usuario'
    path = os.path.join(settings.BASE_DIR, 'usuario')