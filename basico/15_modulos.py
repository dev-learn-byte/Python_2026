"""
PYTHON DESDE CERO - LECCIÓN 15: MÓDULOS
========================================

📦 ¿Qué son los MÓDULOS?
------------------------
Un módulo es como una CAJA DE HERRAMIENTAS que contiene funciones
y variables que puedes usar en tus programas.

METÁFORA: La Caja de Herramientas 🧰
------------------------------------
Imagina tu casa:
- Cocina → Módulo de cocina (tiene: licuadora, cuchillos, ollas)
- Garage → Módulo de garage (tiene: martillo, destornillador, sierra)
- Cuarto → Módulo de cuarto (tiene: juguetes, libros, ropa)

En vez de llevar TODAS las herramientas a todos lados,
solo traes las que necesitas para cada tarea.

En programación:
- math → Herramientas matemáticas (sin, cos, sqrt)
- random → Herramientas de azar (choice, randint)
- datetime → Herramientas de fecha/hora

¿Por qué usar módulos?
- ✅ Organizar código en archivos separados
- ✅ Reutilizar código fácilmente
- ✅ No escribir TODO en un solo archivo gigante
- ✅ Usar código que otros ya escribieron
"""

import os
import time
import datetime
import math as m
from random import randint, choice
from math import sqrt, pi, cos
import random
import math
print("=" * 70)
print("🎓 LECCIÓN 15: MÓDULOS EN PYTHON")
print("=" * 70)
print()

# ============================================
# 1️⃣ IMPORTAR MÓDULOS PREDEFINIDOS
# ============================================
print("=== 1. IMPORTAR MÓDULOS PREDEFINIDOS ===")
print()

print("📦 FORMA 1: import nombre_modulo")
print()

# Importar módulo completo

print("🎯 EJEMPLO - Módulo math:")
print(f"   Raíz cuadrada de 16: {math.sqrt(16)}")
print(f"   Pi: {math.pi}")
print(f"   5 elevado a 3: {math.pow(5, 3)}")
print()


print("🎯 EJEMPLO - Módulo random:")
numero_aleatorio = random.randint(1, 10)
print(f"   Número aleatorio del 1 al 10: {numero_aleatorio}")

colores = ["rojo", "azul", "verde", "amarillo"]
color_elegido = random.choice(colores)
print(f"   Color aleatorio: {color_elegido}")
print()

print("💡 SINTAXIS:")
print("   import modulo")
print("   modulo.funcion()")
print()

print("-" * 70)
print()


# ============================================
# 2️⃣ FROM ... IMPORT (Importar específico)
# ============================================
print("=== 2. FROM ... IMPORT (Traer solo lo que necesitas) ===")
print()

print("📦 FORMA 2: from modulo import función")
print()

# Importar funciones específicas

print("🎯 EJEMPLO - Importar funciones específicas:")
print(f"   Raíz de 25: {sqrt(25)}")
print(f"   Pi: {pi}")
print(f"   Coseno de 0: {cos(0)}")
print("   (No necesitas escribir 'math.' antes)")
print()


print("🎯 EJEMPLO - Random sin prefijo:")
dado = randint(1, 6)
print(f"   Tirada de dado: {dado}")
print()

print("💡 SINTAXIS:")
print("   from modulo import funcion1, funcion2")
print("   funcion1()  # Sin necesidad de 'modulo.'")
print()

print("-" * 70)
print()


# ============================================
# 3️⃣ IMPORT CON ALIAS (Nombres cortos)
# ============================================
print("=== 3. IMPORT CON ALIAS (Apodos) ===")
print()

print("📦 FORMA 3: import modulo as apodo")
print()


print("🎯 EJEMPLO - Math con alias 'm':")
print(f"   Raíz con alias: {m.sqrt(100)}")
print(f"   Pi con alias: {m.pi}")
print()

# Muy común en ciencia de datos
# import pandas as pd
# import numpy as np

print("💡 USO COMÚN:")
print("   import math as m")
print("   import datetime as dt")
print("   Hace el código más corto y fácil de escribir")
print()

print("-" * 70)
print()


# ============================================
# 4️⃣ MÓDULOS PREDEFINIDOS ÚTILES
# ============================================
print("=== 4. MÓDULOS PREDEFINIDOS MÁS ÚTILES ===")
print()

# MATH - Matemáticas
print("🔢 MATH - Operaciones matemáticas:")
print(f"   Raíz cuadrada: math.sqrt(16) = {math.sqrt(16)}")
print(f"   Redondear arriba: math.ceil(3.2) = {math.ceil(3.2)}")
print(f"   Redondear abajo: math.floor(3.8) = {math.floor(3.8)}")
print(f"   Valor absoluto: math.fabs(-5) = {math.fabs(-5)}")
print()

# RANDOM - Números aleatorios
print("🎲 RANDOM - Números aleatorios:")
print(
    f"   Número del 1-100: random.randint(1, 100) = {random.randint(1, 100)}")
print(f"   Decimal 0-1: random.random() = {random.random():.3f}")

lista = [1, 2, 3, 4, 5]
random.shuffle(lista)
print(f"   Lista mezclada: {lista}")
print()

# DATETIME - Fecha y hora
print("📅 DATETIME - Fecha y hora:")
ahora = datetime.datetime.now()
print(f"   Fecha/hora actual: {ahora}")
print(f"   Solo fecha: {ahora.date()}")
print(f"   Solo hora: {ahora.time()}")
print(f"   Año: {ahora.year}")
print()

# TIME - Tiempo
print("⏱️ TIME - Medición de tiempo:")
print("   Pausando 1 segundo...")
inicio = time.time()
time.sleep(1)
fin = time.time()
print(f"   Tiempo transcurrido: {fin - inicio:.2f} segundos")
print()

# OS - Sistema operativo
print("💻 OS - Información del sistema:")
print(f"   Directorio actual: {os.getcwd()}")
print(f"   Sistema: {os.name}")
print()

print("-" * 70)
print()


# ============================================
# 5️⃣ CREAR TU PROPIO MÓDULO
# ============================================
print("=== 5. CREAR TU PROPIO MÓDULO ===")
print()

print("📝 PASO 1: Crear un archivo separado")
print("   Crea un archivo llamado: mi_modulo.py")
print("   Dentro pon tus funciones")
print()

print("📝 PASO 2: Importarlo en tu programa")
print("   import mi_modulo")
print("   mi_modulo.mi_funcion()")
print()

# Vamos a crear un módulo ahora
print("🎯 CREANDO módulo 'operaciones.py'...")
print()

print("-" * 70)
print()


# ============================================
# 🎯 EJEMPLOS PRÁCTICOS CON MÓDULOS
# ============================================
print("=== 🎯 EJEMPLOS PRÁCTICOS ===")
print()

# 🎮 Juego de adivinanza con random
print("🎮 EJEMPLO 1 - JUEGO DE ADIVINANZA:")

numero_secreto = random.randint(1, 10)
print(f"   Número secreto generado (del 1 al 10)")
intentos = [3, 7, 5]  # Simulamos intentos

for intento in intentos:
    print(f"   Intentaste: {intento}")
    if intento == numero_secreto:
        print(f"   🎉 ¡Correcto! Era {numero_secreto}")
        break
    elif intento < numero_secreto:
        print(f"   ⬆️ Más alto")
    else:
        print(f"   ⬇️ Más bajo")
print()

# 🎲 Tirar dados múltiples
print("🎲 EJEMPLO 2 - TIRAR 2 DADOS:")
dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)
total = dado1 + dado2
print(f"   Dado 1: {dado1}")
print(f"   Dado 2: {dado2}")
print(f"   Total: {total}")
print()

# 📐 Calculadora matemática
print("📐 EJEMPLO 3 - CALCULADORA CIENTÍFICA:")

numero = 16
print(f"   Número: {numero}")
print(f"   Raíz cuadrada: {math.sqrt(numero)}")
print(f"   Al cuadrado: {math.pow(numero, 2)}")
print(f"   Logaritmo: {math.log(numero):.2f}")
print()

# 🎯 Convertir grados a radianes
angulo_grados = 90
angulo_radianes = math.radians(angulo_grados)
print(f"   {angulo_grados}° = {angulo_radianes:.2f} radianes")
print(f"   Seno de {angulo_grados}°: {math.sin(angulo_radianes):.2f}")
print()

# ⏰ Medidor de tiempo de ejecución
print("⏰ EJEMPLO 4 - MEDIR TIEMPO:")

print("   Iniciando tarea...")
inicio = time.time()

# Simulamos una tarea
total = 0
for i in range(1000000):
    total += i

fin = time.time()
tiempo_total = fin - inicio
print(f"   Tarea completada en {tiempo_total:.4f} segundos")
print()

# 📅 Calcular edad
print("📅 EJEMPLO 5 - CALCULAR EDAD:")

año_nacimiento = 2010
año_actual = datetime.datetime.now().year
edad = año_actual - año_nacimiento
print(f"   Año de nacimiento: {año_nacimiento}")
print(f"   Año actual: {año_actual}")
print(f"   Edad: {edad} años")
print()

# 🎰 Lotería
print("🎰 EJEMPLO 6 - NÚMEROS DE LOTERÍA:")

numeros_loteria = random.sample(range(1, 50), 6)
numeros_loteria.sort()
print(f"   Números ganadores: {numeros_loteria}")
print()

# 🃏 Barajar cartas
print("🃏 EJEMPLO 7 - BARAJAR MAZO:")
cartas = ["As", "2", "3", "4", "5", "Rey", "Reina", "Jack"]
print(f"   Mazo original: {cartas}")
random.shuffle(cartas)
print(f"   Mazo barajado: {cartas}")
print()

# 📊 Redondear números
print("📊 EJEMPLO 8 - REDONDEAR NÚMEROS:")

precio = 15.783
print(f"   Precio original: ${precio}")
print(f"   Redondear arriba: ${math.ceil(precio)}")
print(f"   Redondear abajo: ${math.floor(precio)}")
print(f"   Redondear normal: ${round(precio, 2)}")
print()

# 🎨 Elegir color aleatorio
print("🎨 EJEMPLO 9 - SELECTOR DE COLOR:")
colores = ["Rojo", "Azul", "Verde", "Amarillo", "Morado", "Naranja"]
color_del_dia = random.choice(colores)
print(f"   Colores disponibles: {colores}")
print(f"   Color del día: {color_del_dia}")
print()

# ⏲️ Contador regresivo
print("⏲️ EJEMPLO 10 - CONTADOR REGRESIVO:")

for i in range(3, 0, -1):
    print(f"   {i}...")
    time.sleep(0.5)  # Pausa de medio segundo
print("   🚀 ¡Despegue!")
print()

print("-" * 70)
print()


# ============================================
# 📚 MÓDULOS MÁS COMUNES Y SUS USOS
# ============================================
print("=== 📚 MÓDULOS MÁS COMUNES ===")
print()

print("🔢 MATH (Matemáticas):")
print("   - sqrt(), pow(), pi")
print("   - sin(), cos(), tan()")
print("   - ceil(), floor()")
print()

print("🎲 RANDOM (Aleatorio):")
print("   - randint(), random()")
print("   - choice(), shuffle()")
print("   - sample()")
print()

print("📅 DATETIME (Fecha/Hora):")
print("   - datetime.now()")
print("   - date(), time()")
print("   - timedelta()")
print()

print("⏱️ TIME (Tiempo):")
print("   - sleep()")
print("   - time()")
print()

print("💻 OS (Sistema Operativo):")
print("   - getcwd(), listdir()")
print("   - mkdir(), remove()")
print()

print("📁 sys (Sistema):")
print("   - exit()")
print("   - argv (argumentos)")
print()

print("-" * 70)
print()


# ============================================
# 🎯 PROYECTO: Creando un módulo personalizado
# ============================================
print("=== 🎯 PROYECTO: CREAR MÓDULO PERSONALIZADO ===")
print()

print("Vamos a crear módulos personalizados reales...")
print()

# Este código crea los archivos de módulos
crear_modulos = """
# Archivo 1: operaciones.py
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

# Archivo 2: utilidades.py
def saludar(nombre):
    return f"¡Hola {nombre}!"

def despedirse(nombre):
    return f"¡Adiós {nombre}!"

def calcular_promedio(numeros):
    if numeros:
        return sum(numeros) / len(numeros)
    return 0
"""

print("📝 Contenido de los módulos a crear:")
print(crear_modulos)
print()

print("-" * 70)
print()

# ============================================
# ✅ BUENAS PRÁCTICAS
# ============================================
print("=== ✅ BUENAS PRÁCTICAS ===")
print()

print("1️⃣ Importa solo lo que necesitas:")
print("   ✅ from math import sqrt")
print("   ❌ from math import *")
print()

print("2️⃣ Usa alias para nombres largos:")
print("   ✅ import datetime as dt")
print()

print("3️⃣ Organiza tus imports arriba del archivo:")
print("   # Primero módulos estándar")
print("   import math")
print("   import random")
print("   # Luego tus módulos")
print("   import mi_modulo")
print()

print("4️⃣ Un módulo = Un propósito:")
print("   matematicas.py → operaciones matemáticas")
print("   utilidades.py → funciones útiles")
print("   juegos.py → funciones de juegos")
print()

print("-" * 70)
print()

print("=" * 70)
print("🎉 ¡Felicidades! Ya sabes usar módulos en Python 🎉")
print("=" * 70)
print()
print("📌 RESUMEN:")
print("   - MÓDULO = Archivo con funciones/variables")
print("   - import modulo → Importar todo")
print("   - from modulo import funcion → Importar específico")
print("   - import modulo as alias → Usar apodo")
print()
print("🔑 MÓDULOS IMPORTANTES:")
print("   math → Matemáticas")
print("   random → Números aleatorios")
print("   datetime → Fecha y hora")
print("   time → Tiempo y pausas")
print("   os → Sistema operativo")
print()
print("💡 VENTAJAS:")
print("   ✅ Código organizado")
print("   ✅ Reutilizable")
print("   ✅ Fácil de mantener")
print("   ✅ Colaboración en equipo")
print()
print("🎯 PUEDES CREAR TUS PROPIOS MÓDULOS:")
print("   1. Crea archivo.py con tus funciones")
print("   2. Impórtalo: import archivo")
print("   3. Usa: archivo.funcion()")
print("=" * 70)
