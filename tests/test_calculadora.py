import pytest

from src.calculadora import somar, subtrair, multiplicar, dividir


def test_somar():
    assert somar(2, 3) == 5


def test_subtrair():
    assert subtrair(5, 3) == 2


def test_multiplicar():
    assert multiplicar(4, 3) == 12


def test_dividir():
    assert dividir(10, 2) == 5


def test_dividir_por_zero():
    with pytest.raises(ValueError):
        dividir(10, 0)


def test_somar_numeros_negativos():
    assert somar(-2, -3) == -5


def test_somar_numeros_decimais():
    assert somar(2.5, 1.5) == 4.0


def test_multiplicar_por_zero():
    assert multiplicar(10, 0) == 0


def test_dividir_numeros_negativos():
    assert dividir(-10, 2) == -5


def test_dividir_resultado_decimal():
    assert dividir(5, 2) == 2.5
