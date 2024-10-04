# UEN models.py
from django.db import models
from usuario.models import UEN, Regional, CustomUser, Area
from django.utils import timezone

# Create your models here.    
class CentroCostos(models.Model):
    codigo = models.PositiveIntegerField()
    nombre = models.CharField(max_length=100)
    regional = models.ForeignKey(Regional, related_name="centrocostos", on_delete=models.CASCADE, null=True, blank=True)
    uen = models.ForeignKey(UEN, related_name="centrocostos", on_delete=models.CASCADE, null=True, blank=True)
    area = models.ForeignKey(Area, related_name="centrocostos", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} - {self.regional} - {self.uen}"
    
class Rubro (models.Model):
    codigo = models.PositiveIntegerField()
    nombre = models.CharField(max_length=100)
    regional = models.ForeignKey(Regional, related_name="rubros", on_delete=models.CASCADE, null=True, blank=True)
    uen = models.ForeignKey(UEN, related_name="rubros", on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Rubro"
        verbose_name_plural = "Rubros"

    def __str__(self):
        return self.nombre
    
class SubRubro (models.Model):
    codigo = models.PositiveIntegerField()
    nombre = models.CharField(max_length=100)
    rubro = models.ForeignKey(Rubro, related_name="subrubros", on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.nombre

class Presupuesto(models.Model):
    usuario = models.ForeignKey(CustomUser, related_name="presupuesto", on_delete=models.CASCADE, null=True, blank=True)
    cuenta = models.ForeignKey(CentroCostos, related_name="presupuestos", on_delete=models.SET_NULL, null=True, blank=True)
    uen = models.ForeignKey(UEN, related_name="presupuestos", on_delete=models.SET_NULL, null=True, blank=True)
    rubro = models.IntegerField()
    subrubro = models.IntegerField()
    item = models.IntegerField()
    meses = models.IntegerField()
    presupuestomes = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    updatedRubros = models.JSONField(null=True)
    monthlyTotals = models.JSONField(null=True)
    rubrosTotals = models.JSONField(null=True)
    fecha = models.DateField(default=timezone.now)

    def __str__(self):
        return f"Presupuesto {self.cuenta} - Meses {self.meses}"