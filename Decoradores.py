# Definir un decorador
def mi_decorador(func):
    def nueva_funcion():
        print("Función decorada.")
        func()
        print("Terminó la función decorada.")
    return nueva_funcion

# Aplicar el decorador a una función
@mi_decorador
def saludo():
    print("¡Hola!")

# Llamar a la función decorada
saludo()
