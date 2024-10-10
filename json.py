import json
# Definir un diccionario
datos = {
    'nombre': 'goku',
    'edad': 30,
    'ciudad': 'Madrid'
}

# Serializar el diccionario a JSON
json_datos = json.dumps(datos)
print(json_datos)

# Escribir JSON en un archivo
with open('datos.json', 'w') as archivo:
    json.dump(datos, archivo)

# Leer JSON desde un archivo
with open('datos.json', 'r') as archivo:
    datos_cargados = json.load(archivo)

print(datos_cargados)
