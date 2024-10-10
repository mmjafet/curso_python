import unittest

# Definir una función a probar
def sumar(a, b):
    return a + b

# Crear una clase de prueba
class TestSumar(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(sumar(1, 2), 3)
        self.assertEqual(sumar(-1, 1), 0)

# Ejecutar las pruebas
if __name__ == '__main__':
    unittest.main()
