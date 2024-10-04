# Manejo de múltiples excepciones
try:
    numero = int(input("Introduce un número: "))
    resultado = 10 / numero
except ValueError:
    print("¡Error! Debes introducir un número entero.")
except ZeroDivisionError:
    print("¡Error! No se puede dividir entre cero.")
except Exception as e:
    print(f"Ha ocurrido un error: {e}")
finally:
    print("Fin del manejo de excepciones.")

# Definir una excepción personalizada
class MiError(Exception):
    pass

# Usar la excepción personalizada
try:
    raise MiError("Este es un error personalizado.")
except MiError as e:
    print(e)
