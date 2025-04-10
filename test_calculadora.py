import sys
import unittest
import calculadora
import logging
import warnings


class TestCalculadora(unittest.TestCase):
    
    # Testes somar

    @unittest.skipIf(sys.platform.startswith('win'), "Test skipped on Windows platform")
    def test_pular_ambiente_windows(self):
        self.fail("Não deveria ser executado em ambiente Windows")

    def test_somar_dois_numeros_iguais(self):
        resultado = calculadora.somar(2, 2)
        self.assertIs(resultado, 4)
        self.assertIsNot(resultado, 5)
    
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
    
    
    # Testes multiplicar

    def test_multiplicar_dois_numeros_positivos(self):
        resultado = calculadora.multiplicar(2, 3)
        self.assertEqual(resultado, 6, "Falhou no teste de multiplicação entre dois números positivos.")

    def test_multiplicar_dois_numeros_negativos(self):
        resultado = calculadora.multiplicar(-2, -3)
        self.assertEqual(resultado, 6, "Falhou no teste de multiplicação entre dois números negativos.")

    def test_multiplicar_um_positivo_e_um_negativo(self):
        resultado = calculadora.multiplicar(2, -3)
        self.assertEqual(resultado, -6, "Falhou no teste de multiplicação entre um positivo e um negativo.")

    def test_multiplicar_por_zero(self):
        resultado = calculadora.multiplicar(3, 0)
        self.assertEqual(resultado, 0, "Falhou no teste de multiplicação por zero.")

    def test_multiplicar_decimais(self):
        resultado = calculadora.multiplicar(0.5, 0.5)
        self.assertEqual(resultado, 0.25, "Falhou no teste de multiplicação entre dois números decimais.")

    def test_multiplicar_numeros_muito_elevados(self):
        resultado = calculadora.multiplicar(100000000000000000000, 100000000000000000000)
        self.assertEqual(resultado, 10000000000000000000000000000000000000000, "Falhou no teste de multiplicação com números muito elevados.")


    # Testes dividir
    
    def test_dividir_dois_numeros_positivos_diferente_de_zero(self):
        resultado = calculadora.dividir(4, 2)
        self.assertEqual(resultado, 2)
    
    def test_dividir_valor_com_resultado_nao_esperado(self):
        self.assertNotEqual(calculadora.dividir(8, 2), 5)
    
    def test_dividir_com_zero_no_divisor(self):
        """
        Esse teste verifica se a exceção lançada é a esperada quando o primeiro número é zero.
        Com uma mensagem de erro específica.
        """
        with self.assertRaises(Exception) as contexto:
            calculadora.dividir(2, 0)

        self.assertEqual(str(contexto.exception), "Não pode fazer divisão por zero")

    def test_dividir_com_zero_no_dividendo(self):
        """
        Verifica se retorna um warning avisando que o dividendo é zero, para caso seja algum erro inconsciente
        """
        with self.assertWarns(UserWarning):
            resultado = calculadora.dividir(0, 2)
            self.assertEqual(resultado, 0.0)

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
            calculadora.calcular_porcentagem(60, 0)

        # Vejo se o tipo do log é uma lista
        self.assertIsInstance(log.output, list)
        
        # Vejo se a mensagem de log contém o texto esperado.
        self.assertIn("Algo deu errado!", log.output[0])

    def test_calcular_porcentagem_com_numero_negativo(self):
        """
        Verifico se o retono está vindo vazio no caso do valor total ser negativo
        """
        resultado = calculadora.calcular_porcentagem(50, -80)

        self.assertIsNone(resultado)


    # Teste calcular potência

    def test_calcular_potencia_base_positiva_expoente_positivo(self):
        resultado = calculadora.calcular_potencia(2, 3)
        self.assertEqual(resultado, 8, "Falhou no teste de potência com base e expoente positivos.")

    def test_calcular_potencia_base_positiva_expoente_negativo(self):
        resultado = calculadora.calcular_potencia(2, -3)
        self.assertEqual(resultado, 0.125, "Falhou no teste de potência com base positiva e expoente negativo.")

    def test_calcular_potencia_base_negativa_expoente_positivo(self):
        resultado = calculadora.calcular_potencia(-2, 3)
        self.assertEqual(resultado, -8, "Falhou no teste de potência com base negativa e expoente positivo.")

    def test_calcular_potencia_expoente_zero(self):
        resultado = calculadora.calcular_potencia(3, 0)
        self.assertEqual(resultado, 1, "Falhou no teste de potência com expoente zero.")

    def test_calcular_potencia_expoente_negativo_elevado(self):
        resultado = calculadora.calcular_potencia(3, -8)
        self.assertAlmostEqual(resultado, 0.0001524, places=6, msg="Falhou no teste de potência com expoente negativo elevado.")

    def test_calcular_potencia_com_tipo_invalido(self):
        with self.assertRaises(TypeError):
            calculadora.calcular_potencia('a', 2)


if __name__ == '__main__':
    unittest.main() 