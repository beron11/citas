# Universidad Libre - Ingeniería
# Author: Diego Fernando Marin
# Date: Sat Aug 24 07:16:29 -05 2023

# Importar la librería JSON
import json

# Guardar los datos en una lista
datos = []
# Leer un archivo JSON
with open('random_data.json') as json_file:  
    datos = json.load(json_file)

for dato in datos[:5]:
  for llave, valor in dato.items():
    print(llave, ':', valor)
  print()

# https://realpython.com/python-json/
# https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/
# https://docs.python-guide.org/scenarios/json/
