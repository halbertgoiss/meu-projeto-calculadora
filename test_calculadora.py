# test_calculadora.py

import pytest
from calculadora import soma, subtracao, multiplicacao, divisao, potencia, raiz_quadrada

# Testes para SOMA
def test_soma_positivos():
    assert soma(2, 3) == 5

def test_soma_negativos():
    assert soma(-2, -3) == -5

def test_soma_misto():
    assert soma(10, -5) == 5

# Testes para SUBTRAÇÃO
def test_subtracao_positivos():
    assert subtracao(10, 3) == 7

def test_subtracao_negativos():
    assert subtracao(-5, -2) == -3

# Testes para MULTIPLICAÇÃO
def test_multiplicacao_positivos():
    assert multiplicacao(4, 5) == 20

def test_multiplicacao_por_zero():
    assert multiplicacao(10, 0) == 0

# Testes para DIVISÃO
def test_divisao_positivos():
    assert divisao(10, 2) == 5

def test_divisao_por_zero():
    with pytest.raises(ValueError):
        divisao(10, 0)

# Testes para POTÊNCIA
def test_potencia():
    assert potencia(2, 3) == 8

def test_potencia_zero():
    assert potencia(5, 0) == 1

# Testes para RAIZ QUADRADA
def test_raiz_quadrada():
    assert raiz_quadrada(9) == 3

def test_raiz_quadrada_negativo():
    with pytest.raises(ValueError):
        raiz_quadrada(-4)