import multiprocessing

# Función que será ejecutada en un proceso separado
def imprimir_nombre(nombre):
    print(f"Hola {nombre}")

# Crear y ejecutar un proceso
if __name__ == "__main__":
    proceso = multiprocessing.Process(target=imprimir_nombre, args=("Name",))
    proceso.start()
    proceso.join()  # Espera a que el proceso termine
