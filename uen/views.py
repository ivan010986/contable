from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.decorators import action, api_view
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Rubro, SubRubro, CentroCostos, Presupuesto
from .serializers import RubroSerializer, SubRubroSerializer, CentroCostosSerializer, PresupuestoSerializer, PresupuestoListSerializer, HistorialPresupuestoSerializer, InformeDetalladoPresupuestoSerializer, PresupuestoTotalSerializer

class RubroViewSet(viewsets.ModelViewSet):
    queryset = Rubro.objects.all()
    serializer_class = RubroSerializer
    permission_classes = [IsAuthenticated]

class SubRubroViewSet(viewsets.ModelViewSet):
    queryset = SubRubro.objects.all()
    serializer_class = SubRubroSerializer
    permission_classes = [IsAuthenticated]

class CentroCostosListView(viewsets.ModelViewSet):
    serializer_class = CentroCostosSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = CentroCostos.objects.none()

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and user.uen.exists():
            queryset = CentroCostos.objects.filter(uen__in=user.uen.all())
            return queryset
        return CentroCostos.objects.none()

    def list(self, request, *args, **kwargs):
        # token = get_token(request)
        original_response = super().list(request, *args, **kwargs)
        response_data = original_response.data
        
        user_id = request.user.id
        
        if isinstance(response_data, dict):
            response_data['user_id'] = user_id
        elif isinstance(response_data, list):
            response_data = {
                'user_id': user_id,
                'results': response_data
            }
        else:
            response_data = {
                'user_id': user_id,
                'results': []
            }

        return Response(response_data, status=status.HTTP_200_OK)

class PresupuestoViewSet(viewsets.ModelViewSet):
    queryset = Presupuesto.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = PresupuestoSerializer

    @action(detail=False, methods=['patch'], url_path='batch-update')
    def update_batch(self, request):
        if not isinstance(request.data, list):
            return Response({"error": "Formato de datos inválido"}, status=status.HTTP_400_BAD_REQUEST)

        # Obtener los IDs proporcionados en la petición
        ids = [item.get('id') for item in request.data if 'id' in item]

        # Filtrar los objetos existentes en la base de datos
        instances = Presupuesto.objects.filter(id__in=ids)
        instance_map = {instance.id: instance for instance in instances}

        updated_instances = []
        new_instances = []
        not_valid_data = []

        for data in request.data:
            instance = instance_map.get(data.get('id'))

            if instance:
                # Si el objeto existe, actualizarlo
                serializer = self.get_serializer(instance, data=data, partial=True)
                if serializer.is_valid():
                    self.perform_update(serializer)
                    updated_instances.append(serializer.instance)
                else:
                    not_valid_data.append(data)
            else:
                # Si el objeto no existe, crearlo
                serializer = self.get_serializer(data=data)
                if serializer.is_valid():
                    instance = serializer.save()
                    new_instances.append(instance)
                else:
                    not_valid_data.append(data)

        return Response({
            "status": "Actualización por lotes exitosa",
            "updated": len(updated_instances),
            "created": len(new_instances),
            "invalid_data": not_valid_data 
        }, status=status.HTTP_200_OK)

    @action(detail=False, methods=['delete'], url_path='batch-delete')
    def delete_batch(self, request):
        if not isinstance(request.data, list):
            return Response({"error": "Formato de datos inválido"}, status=status.HTTP_400_BAD_REQUEST)

        # Extract IDs from request data
        ids = [item.get('id') for item in request.data if 'id' in item]

        # Ensure all IDs are provided
        if not ids:
            return Response({"error": "No se proporcionaron IDs válidos"}, status=status.HTTP_400_BAD_REQUEST)

        # Attempt to delete the instances
        try:
            deleted_count, _ = Presupuesto.objects.filter(id__in=ids).delete()
            return Response({"status": "Eliminación exitosa", "deleted_count": deleted_count}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": f"Error al eliminar: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Presupuesto.objects.filter(usuario=user)
        return Presupuesto.objects.none()

class HistorialPresupuestoViewSet(viewsets.ModelViewSet):
    queryset = Presupuesto.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = HistorialPresupuestoSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return HistorialPresupuestoSerializer
        return super().get_serializer_class()

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Presupuesto.objects.filter(usuario=user)
        return Presupuesto.objects.none()
    
class InformeDetalladoPresupuestoViewSet(viewsets.ModelViewSet):
    queryset = Presupuesto.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = InformeDetalladoPresupuestoSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return InformeDetalladoPresupuestoSerializer
        return super().get_serializer_class()

    def get_queryset(self):
        return Presupuesto.objects.select_related('uen', 'cuenta__regional').order_by('uen__nombre', 'cuenta__regional__nombre')

@api_view(['POST'])
def save_presupuesto_total(request):
    if request.method == 'POST':
        serializer = PresupuestoTotalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)