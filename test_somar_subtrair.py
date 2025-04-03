import unittest
import calculadora

class TestSomar(unittest.TestCase) :
    def test_somar_string_com_numero_deve_resultar_em_erro(self) :
        self.assertRaises(TypeError, calculadora.somar, '', 1)

    def test_somar_dois_numeros_negativos(self):
        resultado = calculadora.somar(-2, -3)
        self.assertEqual(resultado, -5)

    def test_somar_numero_positivo_com_negativo(self) :
        resultado = calculadora.somar(5, -10)
        self.assertEqual(resultado, -5)

    def test_cinco_deve_ser_maior_que_um_mais_dois(self) :
        self.assertGreater(5, calculadora.somar(1,2))

    def test_tres_deve_ser_menor_que_cinco_menos_um(self) :
        self.assertLess(3, calculadora.subtrair(5,1))

    def test_somar_deve_retornar_int(self) :
        self.assertIsInstance(calculadora.somar(1,1), int)

    def 

if __name__ == '__main__':
    unittest.main() 