from typing import List
import re


class Aluno:
    def __init__(self, notas: List[int]):
        if len(notas) != 3:
            raise ValueError("O aluno deve ter exatamente 3 notas.")
        self.notas = notas
        self.media = 0.0
        self.situacao = ""

    def calcular_media(self):
        pesos_notas = [1, 2, 2]
        total = 0
        peso_total = 0

        for i in range(len(self.notas)):
            total += self.notas[i] * pesos_notas[i]
            peso_total += pesos_notas[i]

        self.media = total / peso_total

        if self.media >= 7.0:
            self.situacao = "Aprovado"
        elif self.media >= 5.0:
            self.situacao = "Recuperação"
        else:
            self.situacao = "Reprovado"

    def __str__(self):
        return f"Notas: {self.notas} | Média: {self.media:.2f} | Situação: {self.situacao}"


class Turma:
    def __init__(self, ano_sala: str, capacidade_maxima: int):
        padrao_ano_sala = re.compile("^\d-[A-Z]$")

        if len(ano_sala) != 3 or not padrao_ano_sala.match(ano_sala):
            raise ValueError("A identificação da turma deve estar no formato '<número>-<letra>' (Ex: 1-A).")
        
        self.ano_sala = ano_sala
        self.capacidade_maxima = capacidade_maxima
        self.alunos: List[Aluno] = []

    def adicionar_aluno(self, aluno: Aluno) -> bool:
        if len(self.alunos) < self.capacidade_maxima:
            self.alunos.append(aluno)
            return True
        return False

    def __str__(self):
        return f"Turma {self.ano_sala} - Capacidade máxima: {self.capacidade_maxima} alunos - Alunos cadastrados: {len(self.alunos)}"


if __name__ == '__main__':

    turma1A = Turma("1-A", 30)
    # turma2B = Turma("2B", 35) # Formato Inválido, logo lança um erro.