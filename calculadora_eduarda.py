import logging

logger = logging.getLogger('meu_logger')

def dividir(numero1: int, numero2: int) -> int:
    if numero1 == 0 or numero2 == 0:
        raise Exception("Não pode fazer divisão por zero")

    return numero1 / numero2;

def calcular_porcentagem(valor: int, total: int) -> int:
    if valor == 0 or total == 0:
        logger.error("Algo deu errado!")
        return 0
    return valor / total * 100

if __name__ == '__main__':
    print(dividir(0, 3))