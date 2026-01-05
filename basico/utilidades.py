"""
Módulo de Utilidades
Contiene funciones útiles para el día a día
"""


def saludar(nombre):
    """Saluda a una persona"""
    return f"¡Hola {nombre}! ¿Cómo estás?"


def despedirse(nombre):
    """Se despide de una persona"""
    return f"¡Adiós {nombre}! ¡Hasta pronto!"


def calcular_promedio(numeros):
    """Calcula el promedio de una lista de números"""
    if numeros:
        return sum(numeros) / len(numeros)
    return 0


def contar_vocales(texto):
    """Cuenta las vocales en un texto"""
    vocales = "aeiouAEIOU"
    return sum(1 for letra in texto if letra in vocales)


def invertir_texto(texto):
    """Invierte un texto"""
    return texto[::-1]
