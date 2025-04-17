import unittest
from gerenciador_turmas import Aluno, Turma


class TestAluno(unittest.TestCase):
        
    def test_criar_aluno_com_sucesso(self):
        aluno = Aluno([7, 8, 9])
        self.assertIsInstance(aluno, Aluno, "Falha no teste de criação de nova intância de Aluno.")

    def test_criar_aluno_com_mais_de_tres_notas(self):
        with self.assertRaises(ValueError):
            Aluno([7, 8, 9, 10])

    def test_criar_aluno_com_menos_de_tres_notas(self):
        with self.assertRaises(ValueError):
            Aluno([7, 8]) 

    def test_aluno_com_situacao_aprovado(self):
        aluno = Aluno([8, 7, 9])
        aluno.calcular_media()
        self.assertEqual(aluno.situacao, "Aprovado")
        self.assertGreaterEqual(aluno.media, 7.0)

    def test_aluno_com_situacao_recuperacao(self):
        aluno = Aluno([5, 6, 5])
        aluno.calcular_media()
        self.assertEqual(aluno.situacao, "Recuperação")
        self.assertGreaterEqual(aluno.media, 5.0)
        self.assertLess(aluno.media, 7.0)

    def test_aluno_com_situacao_reprovado(self):
        aluno = Aluno([3, 4, 4])
        aluno.calcular_media()
        self.assertEqual(aluno.situacao, "Reprovado")
        self.assertLess(aluno.media, 5.0)


class TestTurma(unittest.TestCase):
    
    def setUp(self):
        self.turma = Turma("1-A", 30)
        # print("O método setUp é executado antes de cada teste.")

    def test_turma_vazia(self):
        self.assertEqual(len(self.turma.alunos), 0)

    def test_turma_com_ano_sala_tamanho_invalido(self):
        with self.assertRaises(ValueError):
            Turma("1A", 20)

    def test_turma_formatos_ano_sala(self):
        self.assertRegex("1-A", self.turma.formato_ano_sala, "Falha no teste de validação do formato de ano e sala.")
        self.assertNotRegex("1-a", self.turma.formato_ano_sala, "Falha no teste de validação do formato de ano e sala.")
        self.assertNotRegex("1A", self.turma.formato_ano_sala, "Falha no teste de validação do formato de ano e sala.")
        self.assertNotRegex("A-1", self.turma.formato_ano_sala, "Falha no teste de validação do formato de ano e sala.")

    def test_adicionar_aluno_com_sucesso(self):
        aluno = Aluno([7, 8, 9])
        resultado = self.turma.adicionar_aluno(aluno)
        self.assertTrue(resultado)
        self.assertEqual(len(self.turma.alunos), 1)
        self.assertIs(self.turma.alunos[0], aluno)

    def test_nao_adicionar_quando_cheia(self):
        turma = Turma("2-B", 1)
        aluno1 = Aluno([6, 6, 6])
        aluno2 = Aluno([7, 7, 7])
        turma.adicionar_aluno(aluno1)
        resultado = turma.adicionar_aluno(aluno2)
        self.assertFalse(resultado)
        self.assertEqual(len(turma.alunos), 1)
    
    def test_adicao_de_multiplos_alunos(self):
        turma = Turma("3-C", 4)

        aluno1 = Aluno([6, 6, 6])
        aluno2 = Aluno([7, 7, 7])
        aluno3 = Aluno([8, 8, 8])
        aluno4 = Aluno([9, 9, 9])

        turma.adicionar_aluno(aluno1)
        turma.adicionar_aluno(aluno2)
        turma.adicionar_aluno(aluno3)
        turma.adicionar_aluno(aluno4)

        self.assertCountEqual([aluno4, aluno1, aluno3, aluno2], turma.alunos)
    

    # def tearDown(self):
    #     print("O método tearDown é executado após cada teste.")
    

if __name__ == "__main__":
    unittest.main()
