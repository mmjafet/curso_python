# Manejo de excepciones en Python
try:
    numero = int(input("Introduce un número: "))
    resultado = 10 / numero
    print(f"El resultado es {resultado}")
except ValueError:
    print("¡Error! No introdujiste un número.")
except ZeroDivisionError:
    print("¡Error! No se puede dividir entre cero.")
finally:
    print("Fin del programa.")
