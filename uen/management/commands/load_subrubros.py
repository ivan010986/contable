from django.core.management.base import BaseCommand
from uen.models import Rubro, SubRubro
import pandas as pd

class Command(BaseCommand):
    help = "Cargar datos de SubRubros desde un archivo Excel"

    def handle(self, *args, **kwargs):
        # Ruta al archivo de Excel
        file_path = r'C:\Users\duvan\Downloads\hj.xlsx'
        df = pd.read_excel(file_path)
        
        # Verificar nombres de las columnas
        print(df.columns)  # For verification

        # Recorrer el archivo y alimentar la base de datos
        for _, row in df.iterrows():
            try:
                # Fetch the associated Rubro using rubro_id
                # rubro_instance = Rubro.objects.get(id=row['rubro_id'])

                # Create the SubRubro instance
                SubRubro.objects.create(
                    codigo=row['codigo'],
                    nombre=row['nombre'],
                    # rubro=rubro_instance  # Assign the related Rubro instance
                )
            except Rubro.DoesNotExist:
                self.stdout.write(self.style.ERROR(f"Rubro ID {row['rubro_id']} no encontrado."))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Error al cargar la fila {row}: {e}"))

        self.stdout.write(self.style.SUCCESS("Datos de SubRubros cargados correctamente"))
