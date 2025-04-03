import unittest
import calculadora


class TestCalculadora(unittest.TestCase):
    def test_somar_dois_numeros_positivos(self):
        resultado = calculadora.somar(2, 3)
        self.assertEqual(resultado, 5)

    def test_somar_dois_numeros_negativos(self):
        resultado = calculadora.somar(-2, -3)
        self.assertEqual(resultado, -5)

    def test_subtrair_dois_numeros_positivos(self):
        resultado = calculadora.subtrair(2, 3)
        self.assertEqual(resultado, -1)

    def test_subtrair_dois_numeros_negativos(self):
        resultado = calculadora.subtrair(-2, -3)
        self.assertEqual(resultado, 1)


if __name__ == '__main__':
    unittest.main() 