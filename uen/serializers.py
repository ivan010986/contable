from rest_framework import serializers
from .models import Rubro, SubRubro, CentroCostos, Presupuesto, PresupuestoTotal
from usuario.models import CustomUser, UEN, Regional

class SubRubroSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubRubro
        fields = ['id', 'codigo', 'nombre']

class RubroSerializer(serializers.ModelSerializer):
    subrubros = SubRubroSerializer(many=True, read_only=True)

    class Meta:
        model = Rubro
        fields = ['id', 'codigo', 'nombre', 'subrubros']

class UENSerializer(serializers.ModelSerializer):
    class Meta:
        model = UEN
        fields = ['nombre']

class RegionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regional
        fields = ['nombre']

class CentroCostosSerializer(serializers.ModelSerializer):
    uen = UENSerializer(read_only=True)
    regional = RegionalSerializer(read_only=True)
    
    class Meta:
        model = CentroCostos
        fields = ['id', 'codigo', 'nombre', 'regional', 'uen']

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'email']

class HistorialPresupuestoSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=True)
    uen = UENSerializer(read_only=True)

    class Meta:
        model = Presupuesto
        fields = ['id', 'usuario', 'uen', 'cuenta', 'rubro', 'subrubro', 'item', 'meses', 'presupuestomes', 'fecha', 'updatedRubros', 'monthlyTotals', 'rubrosTotals']

class PresupuestoSerializer(serializers.ModelSerializer):
    uen = serializers.SlugRelatedField(queryset=UEN.objects.all(), slug_field='nombre')
    class Meta:
        model = Presupuesto
        fields = ['usuario', 'uen', 'cuenta', 'rubro', 'subrubro', 'item', 'meses', 'presupuestomes', 'updatedRubros', 'monthlyTotals', 'rubrosTotals']

class PresupuestoListSerializer(serializers.ListSerializer):
    child = PresupuestoSerializer()
    def create(self, validated_data):
        instances = [Presupuesto(**item) for item in validated_data]
        return Presupuesto.objects.bulk_create(instances)
    
class InformeDetalladoPresupuestoSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=True)
    uen = UENSerializer(read_only=True)
    cuenta = serializers.SerializerMethodField()

    class Meta:
        model = Presupuesto
        fields = ['id', 'usuario', 'uen', 'cuenta', 'rubro', 'subrubro', 'item', 'meses', 'presupuestomes', 'fecha', 'updatedRubros', 'monthlyTotals', 'rubrosTotals']

    def get_cuenta(self, obj):
        return {
            'codigo': obj.cuenta.codigo,
            'nombre': obj.cuenta.nombre,
            'regional': obj.cuenta.regional.nombre
        }

class PresupuestoTotalSerializer(serializers.ModelSerializer):
    class Meta:
        model = PresupuestoTotal
        fields = '__all__'