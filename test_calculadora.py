import unittest
import calculadora
import logging


class TestCalculadora(unittest.TestCase):
    
    # Testes somar
    
    def test_somar_dois_numeros_positivos(self):
        resultado = calculadora.somar(2, 3)
        self.assertEqual(resultado, 5)

    def test_somar_dois_numeros_negativos(self):
        resultado = calculadora.somar(-2, -3)
        self.assertEqual(resultado, -5)
    
    def test_somar_string_com_numero_deve_resultar_em_erro(self) :
        self.assertRaises(TypeError, calculadora.somar, '', 1)

    def test_somar_numero_positivo_com_negativo(self) :
        resultado = calculadora.somar(5, -10)
        self.assertEqual(resultado, -5)

    def test_cinco_deve_ser_maior_que_um_mais_dois(self) :
        self.assertGreater(5, calculadora.somar(1,2))
        
    def test_somar_deve_retornar_int(self) :
        self.assertIsInstance(calculadora.somar(1,1), int)

    
    # Testes subtrair
    
    def test_subtrair_dois_numeros_positivos(self):
        resultado = calculadora.subtrair(2, 3)
        self.assertEqual(resultado, -1)

    def test_subtrair_dois_numeros_negativos(self):
        resultado = calculadora.subtrair(-2, -3)
        self.assertEqual(resultado, 1)
        
    def test_tres_deve_ser_menor_que_cinco_menos_um(self) :
        self.assertLess(3, calculadora.subtrair(5,1))
    
    # Testes dividir
    
    def test_dividir_sucesso(self):
        resultado = calculadora.dividir(4, 2)
        self.assertEqual(resultado, 2)
    
    def test_dividir_valor_errado(self):
        self.assertNotEqual(calculadora.dividir(8, 2), 5)
    
    def test_dividir_com_zero_no_numero1(self):
        """
        Esse teste verifica se a exceção lançada é a esperada quando o primeiro número é zero.
        Com uma mensagem de erro específica.
        """
        with self.assertRaises(Exception) as contexto:
            calculadora.dividir(0, 2)

        self.assertEqual(str(contexto.exception), "Não pode fazer divisão por zero")

    # Testes calcular porcentagem
    
    def test_calcular_porcentagem_sucesso(self):
        resultado = calculadora.calcular_porcentagem(25, 50)
        self.assertEqual(resultado, 50)

    def test_calcular_porcentagem_tipo_do_retorno(self):
        """
        O IsInstace verifica se o tipo do objeto é o esperado.
        É util para verificar se um objeto é da classe esperada, por exemplo.
        """
        self.assertIsInstance(calculadora.calcular_porcentagem(25, 50), float)
        self.assertNotIsInstance(calculadora.calcular_porcentagem, int)

    def test_calcular_porcentagem_logger(self):
        """
        Aqui o teste verifica se o logger foi lançado no método corretamente.
        """
        logger = logging.getLogger('meu_logger')
        logger.setLevel(logging.DEBUG)

        with self.assertLogs(logger, level='ERROR') as log:
            calculadora.calcular_porcentagem(0, 60)

        # Vejo se o tipo do log é uma lista
        self.assertIsInstance(log.output, list)
        
        # Vejo se a mensagem de log contém o texto esperado.
        self.assertIn("Algo deu errado!", log.output[0])

if __name__ == '__main__':
    unittest.main() 