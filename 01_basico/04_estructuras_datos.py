"""
Estructuras de Datos en Python
Aprende las principales estructuras de datos
"""

# ============================================
# 1. LISTAS (Lists)
# ============================================
print("=== LISTAS ===")

# Crear lista
numeros = [1, 2, 3, 4, 5]
print(f"Lista de números: {numeros}")

# Listas mixtas
mixta = [1, "texto", 3.14, True]
print(f"Lista mixta: {mixta}")

# Acceder a elementos
frutas = ["manzana", "banana", "naranja", "uva"]
print(f"\nPrimera fruta: {frutas[0]}")
print(f"Última fruta: {frutas[-1]}")

# Slicing (rebanado)
print(f"Primeras dos frutas: {frutas[0:2]}")
print(f"Desde el segundo: {frutas[1:]}")

# Métodos de listas
frutas.append("sandía")  # Agregar al final
print(f"Después de append: {frutas}")

frutas.insert(1, "pera")  # Insertar en posición
print(f"Después de insert: {frutas}")

frutas.remove("banana")  # Eliminar por valor
print(f"Después de remove: {frutas}")

ultimo = frutas.pop()  # Eliminar y retornar último
print(f"Elemento eliminado: {ultimo}")
print(f"Lista actual: {frutas}")

# ============================================
# 2. TUPLAS (Tuples)
# ============================================
print("\n=== TUPLAS ===")

# Las tuplas son inmutables (no se pueden modificar)
coordenadas = (10, 20)
print(f"Coordenadas: {coordenadas}")

# Desempaquetado
x, y = coordenadas
print(f"x = {x}, y = {y}")

# Tupla con un solo elemento
tupla_uno = (5,)  # Nota la coma
print(f"Tupla de un elemento: {tupla_uno}")

# Acceder a elementos
dias_semana = ("Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom")
print(f"Primer día: {dias_semana[0]}")
print(f"Últimos tres días: {dias_semana[-3:]}")

# ============================================
# 3. CONJUNTOS (Sets)
# ============================================
print("\n=== CONJUNTOS ===")

# Conjuntos no permiten duplicados y no están ordenados
numeros_set = {1, 2, 3, 4, 5}
print(f"Conjunto: {numeros_set}")

# Eliminar duplicados de una lista
lista_con_duplicados = [1, 2, 2, 3, 3, 3, 4, 5]
sin_duplicados = set(lista_con_duplicados)
print(f"Lista con duplicados: {lista_con_duplicados}")
print(f"Sin duplicados: {sin_duplicados}")

# Operaciones de conjuntos
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(f"\nConjunto A: {set_a}")
print(f"Conjunto B: {set_b}")
print(f"Unión (A | B): {set_a | set_b}")
print(f"Intersección (A & B): {set_a & set_b}")
print(f"Diferencia (A - B): {set_a - set_b}")

# Métodos de conjuntos
colores = {"rojo", "azul", "verde"}
colores.add("amarillo")  # Agregar elemento
print(f"Después de add: {colores}")

# ============================================
# 4. DICCIONARIOS (Dictionaries)
# ============================================
print("\n=== DICCIONARIOS ===")

# Pares clave-valor
persona = {
    "nombre": "Ana",
    "edad": 28,
    "ciudad": "Madrid",
    "profesion": "Ingeniera"
}

print(f"Diccionario persona: {persona}")
print(f"Nombre: {persona['nombre']}")
print(f"Edad: {persona.get('edad')}")

# Agregar o modificar
persona["email"] = "ana@email.com"
persona["edad"] = 29
print(f"\nDespués de modificar: {persona}")

# Iterar sobre diccionario
print("\nIterando sobre el diccionario:")
for clave, valor in persona.items():
    print(f"  {clave}: {valor}")

# Métodos útiles
print(f"\nClaves: {list(persona.keys())}")
print(f"Valores: {list(persona.values())}")

# ============================================
# 5. COMPRENSIÓN DE LISTAS
# ============================================
print("\n=== COMPRENSIÓN DE LISTAS ===")

# Forma tradicional
cuadrados = []
for i in range(1, 6):
    cuadrados.append(i ** 2)
print(f"Cuadrados (tradicional): {cuadrados}")

# Comprensión de listas
cuadrados_comp = [i ** 2 for i in range(1, 6)]
print(f"Cuadrados (comprensión): {cuadrados_comp}")

# Con condicional
pares = [i for i in range(1, 11) if i % 2 == 0]
print(f"Números pares: {pares}")

# ============================================
# 6. COMPRENSIÓN DE DICCIONARIOS
# ============================================
print("\n=== COMPRENSIÓN DE DICCIONARIOS ===")

# Crear diccionario con comprensión
cuadrados_dict = {x: x ** 2 for x in range(1, 6)}
print(f"Diccionario de cuadrados: {cuadrados_dict}")

# ============================================
# 7. EJERCICIO PRÁCTICO
# ============================================
print("\n=== EJERCICIO: GESTIÓN DE ESTUDIANTES ===")

estudiantes = [
    {"nombre": "Juan", "edad": 20, "nota": 85},
    {"nombre": "María", "edad": 22, "nota": 92},
    {"nombre": "Pedro", "edad": 21, "nota": 78},
    {"nombre": "Ana", "edad": 20, "nota": 88}
]

print("Lista de estudiantes:")
for est in estudiantes:
    print(f"  {est['nombre']}: {est['nota']} puntos")

# Calcular promedio
promedio = sum(e["nota"] for e in estudiantes) / len(estudiantes)
print(f"\nPromedio de notas: {promedio:.2f}")

# Estudiantes con nota mayor a 80
aprobados = [e["nombre"] for e in estudiantes if e["nota"] >= 80]
print(f"Estudiantes con nota >= 80: {aprobados}")
