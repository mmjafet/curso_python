import requests

# Hacer una solicitud GET
respuesta = requests.get('https://jsonplaceholder.typicode.com/posts/1')

# Imprimir el contenido de la respuesta
if respuesta.status_code == 200:
    datos = respuesta.json()
    print(datos)
