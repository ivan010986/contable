# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RubroViewSet, SubRubroViewSet, CentroCostosListView, PresupuestoViewSet, HistorialPresupuestoViewSet, InformeDetalladoPresupuestoViewSet
from . import views

router = DefaultRouter()
router.register(r'rubros', RubroViewSet)
router.register(r'subrubros', SubRubroViewSet)
router.register(r'CentroCostos', CentroCostosListView)
router.register(r'presupuestos', PresupuestoViewSet, basename='presupuesto')
router.register(r'HistorialPresupuesto', HistorialPresupuestoViewSet, basename='historial-presupuesto')
router.register(r'InformeDetalladoPresupuesto', InformeDetalladoPresupuestoViewSet, basename='Informe-Detallado-presupuesto')
# router.register(r'save-presupuesto-total', save_presupuesto_totalViewSet, basename='save-presupuesto-total'),

urlpatterns = [
    path('', include(router.urls)),
    path('save-presupuesto-total/', views.save_presupuesto_total, name='save-presupuesto-total'),
]