"""
Estructuras de Control de Flujo
Aprende a controlar el flujo de ejecución del programa
"""

# ============================================
# 1. CONDICIONAL IF
# ============================================
print("=== CONDICIONAL IF ===")

edad = 18

if edad >= 18:
    print(f"Edad: {edad} - Eres mayor de edad")
else:
    print(f"Edad: {edad} - Eres menor de edad")

# ============================================
# 2. IF-ELIF-ELSE
# ============================================
print("\n=== IF-ELIF-ELSE ===")

calificacion = 85

if calificacion >= 90:
    nota = "A - Excelente"
elif calificacion >= 80:
    nota = "B - Muy bien"
elif calificacion >= 70:
    nota = "C - Bien"
elif calificacion >= 60:
    nota = "D - Suficiente"
else:
    nota = "F - Reprobado"

print(f"Calificación: {calificacion} -> {nota}")

# ============================================
# 3. OPERADOR TERNARIO
# ============================================
print("\n=== OPERADOR TERNARIO ===")

numero = 7
resultado = "Par" if numero % 2 == 0 else "Impar"
print(f"El número {numero} es {resultado}")

# ============================================
# 4. BUCLE FOR
# ============================================
print("\n=== BUCLE FOR ===")

# Iterar sobre una lista
frutas = ["manzana", "banana", "naranja", "uva"]
print("Frutas:")
for fruta in frutas:
    print(f"  - {fruta}")

# Iterar con range()
print("\nNúmeros del 1 al 5:")
for i in range(1, 6):
    print(f"  {i}")

# Iterar con índice usando enumerate()
print("\nFrutas con índice:")
for indice, fruta in enumerate(frutas, start=1):
    print(f"  {indice}. {fruta}")

# ============================================
# 5. BUCLE WHILE
# ============================================
print("\n=== BUCLE WHILE ===")

contador = 1
print("Conteo del 1 al 5:")
while contador <= 5:
    print(f"  {contador}")
    contador += 1

# ============================================
# 6. BREAK Y CONTINUE
# ============================================
print("\n=== BREAK Y CONTINUE ===")

# Ejemplo de break
print("Buscar el número 3 (break):")
for num in range(1, 10):
    if num == 3:
        print(f"  ¡Encontrado! Deteniendo búsqueda...")
        break
    print(f"  Buscando... número actual: {num}")

# Ejemplo de continue
print("\nMostrar solo números impares (continue):")
for num in range(1, 11):
    if num % 2 == 0:
        continue  # Saltar números pares
    print(f"  {num}")

# ============================================
# 7. ELSE EN BUCLES
# ============================================
print("\n=== ELSE EN BUCLES ===")

# El else se ejecuta si el bucle termina normalmente (sin break)
print("Buscar número mayor que 10:")
for num in range(1, 8):
    if num > 10:
        print(f"  Encontrado: {num}")
        break
else:
    print("  No se encontró ningún número mayor que 10")

# ============================================
# 8. BUCLES ANIDADOS
# ============================================
print("\n=== BUCLES ANIDADOS ===")

print("Tabla de multiplicar del 2 y 3:")
for i in [2, 3]:
    print(f"\nTabla del {i}:")
    for j in range(1, 6):
        print(f"  {i} x {j} = {i * j}")

# ============================================
# 9. MATCH-CASE (Python 3.10+)
# ============================================
print("\n=== MATCH-CASE ===")

def obtener_dia(numero):
    match numero:
        case 1:
            return "Lunes"
        case 2:
            return "Martes"
        case 3:
            return "Miércoles"
        case 4:
            return "Jueves"
        case 5:
            return "Viernes"
        case 6:
            return "Sábado"
        case 7:
            return "Domingo"
        case _:
            return "Número inválido"

dia_numero = 3
print(f"Día {dia_numero}: {obtener_dia(dia_numero)}")

# ============================================
# 10. EJERCICIO PRÁCTICO
# ============================================
print("\n=== EJERCICIO: NÚMEROS PRIMOS ===")

# Encontrar números primos del 1 al 20
print("Números primos del 1 al 20:")
for numero in range(2, 21):
    es_primo = True
    for divisor in range(2, int(numero ** 0.5) + 1):
        if numero % divisor == 0:
            es_primo = False
            break
    
    if es_primo:
        print(f"  {numero}", end=" ")

print()  # Nueva línea al final
