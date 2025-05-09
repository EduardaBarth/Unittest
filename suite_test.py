"""
O TestSuite permite rodar somente alguns testes ecolhidos ao invés de todos os existentes,
caso seja necessário em algum determinado cenário.
"""

from unittest import TestSuite, TextTestRunner, TestLoader
from test_gerenciador_turmas import TestTurma, TestAluno

suite = TestSuite()

suite.addTest(TestAluno("test_criar_aluno_com_mais_de_tres_notas"))
suite.addTest(TestAluno("test_criar_aluno_com_menos_de_tres_notas"))

# Adiciona todos os testes da classe
suite.addTest(TestLoader().loadTestsFromTestCase(TestTurma))

runner = TextTestRunner()
runner.run(suite)
