def somar(numero1: int, numero2: int) -> int:
    return numero1 + numero2;

def subtrair(numero1: int, numero2: int) -> int:
    return numero1 - numero2;

def multiplicar(numero1: int, numero2: int) -> int:
    return numero1 * numero2;

def dividir(numero1: int, numero2: int) -> int:
    return numero1 / numero2;

def calcular_porcentagem(valor: int, total: int) -> int:
    return valor / total * 100

def calcular_potência(base: int, expoente: int) -> int:
    return base ** expoente;

if __name__ == '__main__':

    print(somar(2, 3))