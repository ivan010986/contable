from django.core.management.base import BaseCommand
from uen.models import CentroCostos
import pandas as pd

class Command(BaseCommand):
    help = "Cargar datos de Centros de Costos (codigo y nombre) desde un archivo Excel"

    def handle(self, *args, **kwargs):
        # Ruta al archivo de Excel
        file_path = r'C:\Users\duvan\Downloads\CentroCostos - DEPURADOS 29 SEP 2024.xlsx'
        df = pd.read_excel(file_path)
        print(df.columns)  # Para verificar los nombres de las columnas

        # Recorrer el archivo y alimentar la base de datos
        for _, row in df.iterrows():
            try:
                CentroCostos.objects.create(
                    codigo=row['Código'],
                    nombre=row['Nombre']
                )
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Error al cargar la fila {row}: {e}"))

        self.stdout.write(self.style.SUCCESS("Datos cargados correctamente"))
