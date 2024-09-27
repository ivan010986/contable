# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RubroViewSet, SubRubroViewSet, CentroCostosListView, PresupuestoViewSet, HistorialPresupuestoViewSet

router = DefaultRouter()
router.register(r'rubros', RubroViewSet)
router.register(r'subrubros', SubRubroViewSet)
router.register(r'CentroCostos', CentroCostosListView)
router.register(r'presupuestos', PresupuestoViewSet, basename='presupuesto')
router.register(r'HistorialPresupuesto', HistorialPresupuestoViewSet, basename='historial-presupuesto')

urlpatterns = [
    path('', include(router.urls)),
]