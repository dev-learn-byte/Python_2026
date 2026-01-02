"""
Variables y Tipos de Datos en Python
Aprende los conceptos básicos de variables y tipos de datos
"""

# ============================================
# 1. VARIABLES
# ============================================
# En Python no necesitas declarar el tipo de variable
nombre = "Juan"
edad = 25
altura = 1.75
es_estudiante = True

print("=== VARIABLES ===")
print(f"Nombre: {nombre}")
print(f"Edad: {edad}")
print(f"Altura: {altura}")
print(f"Es estudiante: {es_estudiante}")

# ============================================
# 2. TIPOS DE DATOS BÁSICOS
# ============================================
print("\n=== TIPOS DE DATOS ===")

# Enteros (int)
numero_entero = 42
print(f"Entero: {numero_entero}, Tipo: {type(numero_entero)}")

# Flotantes (float)
numero_flotante = 3.14159
print(f"Flotante: {numero_flotante}, Tipo: {type(numero_flotante)}")

# Cadenas de texto (str)
texto = "Hola, Python!"
print(f"Cadena: {texto}, Tipo: {type(texto)}")

# Booleanos (bool)
verdadero = True
falso = False
print(f"Booleano: {verdadero}, Tipo: {type(verdadero)}")

# ============================================
# 3. CONVERSIÓN DE TIPOS
# ============================================
print("\n=== CONVERSIÓN DE TIPOS ===")

# De cadena a entero
edad_texto = "30"
edad_numero = int(edad_texto)
print(f"'{edad_texto}' convertido a entero: {edad_numero}")

# De entero a cadena
numero = 100
numero_texto = str(numero)
print(f"{numero} convertido a cadena: '{numero_texto}'")

# De cadena a flotante
precio_texto = "19.99"
precio_numero = float(precio_texto)
print(f"'{precio_texto}' convertido a flotante: {precio_numero}")

# ============================================
# 4. MÚLTIPLES ASIGNACIONES
# ============================================
print("\n=== MÚLTIPLES ASIGNACIONES ===")

# Asignar múltiples variables en una línea
x, y, z = 10, 20, 30
print(f"x={x}, y={y}, z={z}")

# Asignar el mismo valor a múltiples variables
a = b = c = 100
print(f"a={a}, b={b}, c={c}")

# ============================================
# 5. EJERCICIO PRÁCTICO
# ============================================
print("\n=== EJERCICIO: CÁLCULO DE IMC ===")

# Calculadora de Índice de Masa Corporal
peso = 70  # kilogramos
altura_metros = 1.75  # metros
imc = peso / (altura_metros ** 2)

print(f"Peso: {peso} kg")
print(f"Altura: {altura_metros} m")
print(f"IMC: {imc:.2f}")

if imc < 18.5:
    categoria = "Bajo peso"
elif imc < 25:
    categoria = "Peso normal"
elif imc < 30:
    categoria = "Sobrepeso"
else:
    categoria = "Obesidad"

print(f"Categoría: {categoria}")
