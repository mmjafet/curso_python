import requests
from bs4 import BeautifulSoup

# Realizar una solicitud a una página web
respuesta = requests.get('https://www.example.com')

# Crear un objeto BeautifulSoup
soup = BeautifulSoup(respuesta.text, 'html.parser')

# Extraer el título de la página
titulo = soup.title.string
print("Título de la página:", titulo)
