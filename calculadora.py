import logging
import warnings
from typing import Any
from datetime import datetime, timedelta

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
        logger.info("O valor total está como zero!")
        return None

    return valor / total * 100


def calcular_potencia(base: int, expoente: int) -> float:
    return base ** expoente


def somar_hora_atual_com_minutos(minutes: int) -> str:
    hora_atual = datetime.now()
    nova_data = hora_atual + timedelta(minutes=minutes)
    return nova_data.strftime("%Y-%m-%d %H:%M:%S")


if __name__ == '__main__':

    print(somar(2, 3))
    print(multiplicar(0.5, 0.5))
    print(somar_hora_atual_com_minutos(10))
