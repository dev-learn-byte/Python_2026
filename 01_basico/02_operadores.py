"""
Operadores en Python
Aprende los diferentes tipos de operadores
"""

# ============================================
# 1. OPERADORES ARITMÉTICOS
# ============================================
print("=== OPERADORES ARITMÉTICOS ===")

a = 10
b = 3

print(f"a = {a}, b = {b}")
print(f"Suma: {a} + {b} = {a + b}")
print(f"Resta: {a} - {b} = {a - b}")
print(f"Multiplicación: {a} * {b} = {a * b}")
print(f"División: {a} / {b} = {a / b}")
print(f"División entera: {a} // {b} = {a // b}")
print(f"Módulo (residuo): {a} % {b} = {a % b}")
print(f"Potencia: {a} ** {b} = {a ** b}")

# ============================================
# 2. OPERADORES DE COMPARACIÓN
# ============================================
print("\n=== OPERADORES DE COMPARACIÓN ===")

x = 5
y = 10

print(f"x = {x}, y = {y}")
print(f"x == y: {x == y}")  # Igual a
print(f"x != y: {x != y}")  # Diferente de
print(f"x > y: {x > y}")    # Mayor que
print(f"x < y: {x < y}")    # Menor que
print(f"x >= y: {x >= y}")  # Mayor o igual que
print(f"x <= y: {x <= y}")  # Menor o igual que

# ============================================
# 3. OPERADORES LÓGICOS
# ============================================
print("\n=== OPERADORES LÓGICOS ===")

p = True
q = False

print(f"p = {p}, q = {q}")
print(f"p and q: {p and q}")  # Y lógico
print(f"p or q: {p or q}")    # O lógico
print(f"not p: {not p}")      # Negación lógica
print(f"not q: {not q}")

# Ejemplo con números
edad = 25
tiene_licencia = True

print(f"\nEdad: {edad}, Tiene licencia: {tiene_licencia}")
puede_conducir = edad >= 18 and tiene_licencia
print(f"¿Puede conducir?: {puede_conducir}")

# ============================================
# 4. OPERADORES DE ASIGNACIÓN
# ============================================
print("\n=== OPERADORES DE ASIGNACIÓN ===")

numero = 10
print(f"Valor inicial: {numero}")

numero += 5  # numero = numero + 5
print(f"Después de += 5: {numero}")

numero -= 3  # numero = numero - 3
print(f"Después de -= 3: {numero}")

numero *= 2  # numero = numero * 2
print(f"Después de *= 2: {numero}")

numero //= 4  # numero = numero // 4
print(f"Después de //= 4: {numero}")

# ============================================
# 5. OPERADORES DE PERTENENCIA
# ============================================
print("\n=== OPERADORES DE PERTENENCIA ===")

frutas = ["manzana", "banana", "naranja"]
print(f"Lista de frutas: {frutas}")

print(f"'manzana' in frutas: {'manzana' in frutas}")
print(f"'uva' in frutas: {'uva' in frutas}")
print(f"'uva' not in frutas: {'uva' not in frutas}")

texto = "Python es genial"
print(f"\nTexto: '{texto}'")
print(f"'Python' in texto: {'Python' in texto}")
print(f"'Java' in texto: {'Java' in texto}")

# ============================================
# 6. OPERADORES DE IDENTIDAD
# ============================================
print("\n=== OPERADORES DE IDENTIDAD ===")

lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
lista3 = lista1

print(f"lista1: {lista1}")
print(f"lista2: {lista2}")
print(f"lista3: {lista3}")

print(f"lista1 is lista2: {lista1 is lista2}")  # False (diferentes objetos)
print(f"lista1 is lista3: {lista1 is lista3}")  # True (mismo objeto)
print(f"lista1 == lista2: {lista1 == lista2}")  # True (mismo contenido)

# ============================================
# 7. EJERCICIO PRÁCTICO
# ============================================
print("\n=== EJERCICIO: CALCULADORA SIMPLE ===")

num1 = 15
num2 = 4

print(f"Número 1: {num1}")
print(f"Número 2: {num2}")
print(f"Suma: {num1 + num2}")
print(f"Resta: {num1 - num2}")
print(f"Multiplicación: {num1 * num2}")
print(f"División: {num1 / num2:.2f}")
print(f"¿Es {num1} mayor que {num2}?: {num1 > num2}")
print(f"¿Son diferentes?: {num1 != num2}")
