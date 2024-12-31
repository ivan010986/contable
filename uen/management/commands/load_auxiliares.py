from django.core.management.base import BaseCommand
from uen.models import Rubro, SubRubro, Auxiliar
import pandas as pd

class Command(BaseCommand):
    help = "Cargar datos de Auxiliares desde un archivo Excel"

    def handle(self, *args, **kwargs):
        # Ruta al archivo de Excel
        file_path = r'C:\Users\duvan\Downloads\cuentas3.xlsx'
        df = pd.read_excel(file_path)
        
        # Verificar nombres de las columnas
        print(df.columns)  # For verification

        # Recorrer el archivo y alimentar la base de datos
        for _, row in df.iterrows():
            try:
                # Fetch the associated Rubro using rubro_id
                # subrubro_instance = Rubro.objects.get(id=row['surubro_id'])

                # Create the SubRubro instance
                Auxiliar.objects.create(
                    codigo=row['Codigo'],
                    nombre=row['Nombre'],
                    # subrubro=subrubro_instance  # Assign the related Rubro instance
                )

            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Error al cargar la fila {row}: {e}"))

        self.stdout.write(self.style.SUCCESS("Datos de Auxiliares cargados correctamente"))
