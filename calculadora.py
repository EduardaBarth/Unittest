import logging

logger = logging.getLogger('meu_logger')

def somar(numero1: float, numero2: float) -> float:
    return numero1 + numero2

def subtrair(numero1: float, numero2: float) -> float:
    return numero1 - numero2

def multiplicar(numero1: float, numero2: float) -> float:
    return numero1 * numero2

def dividir(numero1: float, numero2: float) -> float:
    if numero1 == 0 or numero2 == 0:
        raise Exception("Não pode fazer divisão por zero")

    return numero1 / numero2

def calcular_porcentagem(valor: float, total: float) -> float:
    if valor == 0 or total == 0:
        logger.error("Algo deu errado!")
        return 0
    return valor / total * 100

def calcular_potencia(base: int, expoente: int) -> float:
    return base ** expoente


if __name__ == '__main__':

    print(somar(2, 3))
    print(multiplicar(0.5, 0.5))