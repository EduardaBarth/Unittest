import logging
import warnings
from typing import Any

logger = logging.getLogger('meu_logger')


def somar(numero1: float, numero2: float) -> float:
    return numero1 + numero2


def subtrair(numero1: float, numero2: float) -> float:
    return numero1 - numero2


def multiplicar(numero1: float, numero2: float) -> float:
    return numero1 * numero2


def dividir(dividendo: float, divisor: float) -> float:
    if divisor == 0:
        raise Exception("Não pode fazer divisão por zero")

    if dividendo == 0:
        warnings.warn("Você vai dividir um valor zerado. Está correto?", UserWarning)

    return dividendo / divisor


def calcular_porcentagem(valor: float, total: float) -> Any:
    if total == 0 or total < 0:
        logger.error("Algo deu errado!")
        return None

    return valor / total * 100


def calcular_potencia(base: int, expoente: int) -> float:
    return base ** expoente


if __name__ == '__main__':

    print(somar(2, 3))
    print(multiplicar(0.5, 0.5))