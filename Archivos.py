# Escribir en un archivo
with open("archivo.txt", "w") as archivo:
    archivo.write("Este es un archivo de texto.\n")
    archivo.write("Estamos escribiendo desde Python.")

# Leer de un archivo
with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()

print(contenido)
