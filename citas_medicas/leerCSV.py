# Universidad Libre - Ingeniería
# Author: Diego Fernando Marin
# Date: Sat Aug 24 07:16:29 -05 2023

# Importar la librería CSV
import csv
import pprint
pp = pprint.PrettyPrinter(indent=2)

# Guardar los datos en una lista
datos = []
# Leer un archivo CSV
with open("random_data.csv") as archivo:
  fuente = csv.reader(archivo, delimiter='\t')
  for linea in fuente:
    datos.append(linea)
# los titulos estan en la primera fila
titulos = datos[0]
# al borrarla, el resto son los datos
del(datos[0])

# Imprime la tabla de datos
pp.pprint(titulos)
pp.pprint(datos[:5])

# https://docs.python.org/3/library/csv.html
# https://realpython.com/python-csv/
# https://www.programiz.com/python-programming/reading-csv-files

