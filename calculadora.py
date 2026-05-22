def soma(a, b):
    """Realiza a soma de dois números"""
    return a + b


def subtracao(a, b):
    """Realiza a subtração de dois números"""
    return a - b


def multiplicacao(a, b):
    """Realiza a multiplicação de dois números"""
    return a * b


def divisao(a, b):
    """Realiza a divisão de dois números"""
    if b == 0:
        raise ValueError("Erro: não é possível dividir por zero!")
    return a / b


def potencia(a, b):
    """Calcula a potência de dois números"""
    return a ** b


def raiz_quadrada(a):
    """Calcula a raiz quadrada de um número"""
    if a < 0:
        raise ValueError("Erro: não é possível calcular raiz de número negativo!")
    return a ** 0.5