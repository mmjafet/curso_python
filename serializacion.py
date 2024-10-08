import pickle

# Definir un diccionario de ejemplo
datos = {'nombre': 'Jafet', 'edad': 30, 'ciudad': 'Madrid'}

# Serializar el diccionario a un archivo
with open('datos.pickle', 'wb') as archivo:
    pickle.dump(datos, archivo)

# Deserializar los datos de nuevo
with open('datos.pickle', 'rb') as archivo:
    datos_cargados = pickle.load(archivo)

print(datos_cargados)
