from django.core.management.base import BaseCommand
from uen.models import CentroCostos, Regional, UEN, Area
import pandas as pd

class Command(BaseCommand):
    help = "Cargar datos de Centros de Costos (codigo y nombre) desde un archivo Excel"

    def handle(self, *args, **kwargs):
        # Ruta al archivo de Excel
        file_path = r'C:\Users\duvan\Downloads\hg.xlsx'
        df = pd.read_excel(file_path)
        print(df.columns)  # Para verificar los nombres de las columnas

        # Recorrer el archivo y alimentar la base de datos
        for _, row in df.iterrows():
            try:
                # Fetch related instances using the provided IDs
                # regional_instance = Regional.objects.get(id=row['regional_id'])
                # uen_instance = UEN.objects.get(id=row['uen_id'])
                # area_instance = Area.objects.get(id=row['area_id'])

                # Check if CentroCostos with this ID exists
                centro_costos, created = CentroCostos.objects.get_or_create(
                    id=row['id'],  # This will either create or get the existing instance
                    defaults={
                        'codigo': row['codigo'],
                        'nombre': row['nombre'],
                        # 'regional': regional_instance,
                        # 'uen': uen_instance,
                        # 'area': area_instance,
                    }
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f"CentroCostos {centro_costos} creado."))
                else:
                    self.stdout.write(self.style.WARNING(f"CentroCostos con ID {row['id']} ya existe. Se omite."))

            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Error al cargar la fila {row}: {e}"))

        self.stdout.write(self.style.SUCCESS("Datos cargados correctamente"))
