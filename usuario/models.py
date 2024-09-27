from django.db import models
from django.contrib.auth.models import AbstractUser

class Area(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
    
class UEN(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Departamento UEN"
        verbose_name_plural = "Departamentos UEN"
          
class Regional(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Zona"
        verbose_name_plural = "Zonas"
    
class CustomUser(AbstractUser):

    regional = models.ForeignKey(Regional, related_name="usuarios", on_delete=models.SET_NULL, null=True, blank=True)
    uen = models.ManyToManyField(UEN, related_name="usuarios", blank=True)
    area = models.ForeignKey(Area, related_name="usuarios", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.get_full_name()