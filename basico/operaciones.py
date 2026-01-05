"""
Módulo de Operaciones Matemáticas
Contiene funciones básicas de matemáticas
"""


def sumar(a, b):
    """Suma dos números"""
    return a + b


def restar(a, b):
    """Resta dos números"""
    return a - b


def multiplicar(a, b):
    """Multiplica dos números"""
    return a * b


def dividir(a, b):
    """Divide dos números"""
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"


def potencia(base, exponente):
    """Eleva un número a una potencia"""
    return base ** exponente


def es_par(numero):
    """Verifica si un número es par"""
    return numero % 2 == 0
