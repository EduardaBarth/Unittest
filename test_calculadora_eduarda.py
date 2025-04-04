import unittest
import calculadora_eduarda
import logging


class TestCalculadora(unittest.TestCase):
    def test_dividir_sucesso(self):
        resultado = calculadora_eduarda.dividir(4, 2)
        self.assertEqual(resultado, 2)
    
    def test_dividir_com_zero_no_numero1(self):
        with self.assertRaises(Exception) as contexto:
            calculadora_eduarda.dividir(0, 2)

        self.assertEqual(str(contexto.exception), "Não pode fazer divisão por zero")

    def test_calcular_porcentagem_sucesso(self):
        resultado = calculadora_eduarda.calcular_porcentagem(25, 50)
        self.assertEqual(resultado, 50)

    def test_dividir_valor_errado(self):
        self.assertNotEqual(calculadora_eduarda.dividir(8, 2), 5)

    def test_calcular_porcentagem(self):
        self.assertNotIsInstance(calculadora_eduarda.calcular_porcentagem, int)

    def test_calcular_porcentagem(self):
        logger = logging.getLogger('meu_logger')
        logger.setLevel(logging.DEBUG)

        with self.assertLogs(logger, level='ERROR') as log:
            calculadora_eduarda.calcular_porcentagem(0, 60)

        self.assertIn("Algo deu errado!", log.output[0])

if __name__ == '__main__':
    unittest.main() 