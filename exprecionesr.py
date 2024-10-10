import re

# Buscar todas las coincidencias de un patrón en una cadena
patron = r'\d+'  # Buscar números en la cadena
cadena = "Mi número es 123456 y mi código postal es 78910."
numeros = re.findall(patron, cadena)

print(numeros)  # ['123456', '78910']
