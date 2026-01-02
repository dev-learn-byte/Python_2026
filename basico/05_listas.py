"""
PYTHON DESDE CERO - LECCIÓN 5: LISTAS
======================================

📋 ¿Qué es una LISTA?
---------------------
Una lista es como una MOCHILA donde puedes guardar VARIAS cosas.
En vez de tener una variable para cada cosa, usas UNA lista para guardarlas todas.

Ejemplo en la vida real:
- Una lista de compras: [manzana, pan, leche, huevos]
- Una lista de calificaciones: [85, 90, 95, 78]
- Una lista de amigos: ["Juan", "María", "Pedro"]

Las listas se escriben con CORCHETES [ ] y se separan con COMAS
"""

import random
print("=" * 60)
print("🎓 LECCIÓN 5: LISTAS EN PYTHON")
print("=" * 60)
print()

# ============================================
# 1️⃣ CREAR LISTAS
# ============================================
print("=== 1. CÓMO CREAR LISTAS ===")
print()

# Lista de frutas (textos)
frutas = ["manzana", "pera", "uva", "naranja"]
print("🍎 Lista de frutas:", frutas)

# Lista de números
calificaciones = [85, 90, 78, 92, 88]
print("📊 Lista de calificaciones:", calificaciones)

# Lista de edades
edades = [10, 12, 8, 15, 11]
print("👶 Lista de edades:", edades)

# Lista mixta (diferentes tipos)
datos = ["Juan", 12, True, 1.75]
print("🎒 Lista mixta:", datos, "(nombre, edad, estudiante, altura)")

# Lista vacía
mi_lista_vacia = []
print("📭 Lista vacía:", mi_lista_vacia)

print()
print("-" * 60)
print()


# ============================================
# 2️⃣ ACCEDER A ELEMENTOS (Índices)
# ============================================
print("=== 2. ACCEDER A ELEMENTOS DE LA LISTA ===")
print()

colores = ["rojo", "azul", "verde", "amarillo", "morado"]
print("🎨 Lista de colores:", colores)
print()

# Los índices empiezan en 0
print("📍 ÍNDICES (posiciones):")
print("   rojo   azul   verde   amarillo   morado")
print("    0      1       2        3         4")
print()

# Acceder por índice
print("🔍 ACCEDER POR ÍNDICE:")
print(f"   colores[0] = {colores[0]}  (primer elemento)")
print(f"   colores[1] = {colores[1]}  (segundo elemento)")
print(f"   colores[3] = {colores[3]}")
print()

# Índices negativos (empiezan desde el final)
print("🔍 ÍNDICES NEGATIVOS (desde el final):")
print(f"   colores[-1] = {colores[-1]}  (último elemento)")
print(f"   colores[-2] = {colores[-2]}  (penúltimo elemento)")
print()

# Longitud de la lista
print(f"📏 Cantidad de colores: len(colores) = {len(colores)}")
print()

print("-" * 60)
print()


# ============================================
# 3️⃣ MODIFICAR ELEMENTOS
# ============================================
print("=== 3. MODIFICAR ELEMENTOS DE LA LISTA ===")
print()

# Cambiar un elemento
numeros = [10, 20, 30, 40, 50]
print("📝 Lista original:", numeros)

numeros[0] = 15  # Cambiar el primer elemento
print("   Cambié numeros[0] = 15")
print("   Lista ahora:", numeros)
print()

numeros[2] = 100  # Cambiar el tercer elemento
print("   Cambié numeros[2] = 100")
print("   Lista ahora:", numeros)
print()

print("-" * 60)
print()


# ============================================
# 4️⃣ MÉTODOS PARA AGREGAR ELEMENTOS
# ============================================
print("=== 4. AGREGAR ELEMENTOS A LA LISTA ===")
print()

# append() - Agregar al final
mascotas = ["perro", "gato"]
print("🐶 Lista de mascotas:", mascotas)

mascotas.append("pájaro")
print("   .append('pájaro') → Agregar al final")
print("   Lista ahora:", mascotas)
print()

mascotas.append("pez")
print("   .append('pez')")
print("   Lista ahora:", mascotas)
print()

# insert() - Insertar en una posición específica
print("📌 INSERT (Insertar en posición específica):")
numeros = [1, 2, 4, 5]
print("   Lista original:", numeros)

numeros.insert(2, 3)  # Insertar 3 en la posición 2
print("   .insert(2, 3) → Insertar 3 en posición 2")
print("   Lista ahora:", numeros)
print()

# extend() - Agregar otra lista completa
print("➕ EXTEND (Unir dos listas):")
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
print("   lista1:", lista1)
print("   lista2:", lista2)

lista1.extend(lista2)
print("   lista1.extend(lista2)")
print("   lista1 ahora:", lista1)
print()

print("-" * 60)
print()


# ============================================
# 5️⃣ MÉTODOS PARA ELIMINAR ELEMENTOS
# ============================================
print("=== 5. ELIMINAR ELEMENTOS DE LA LISTA ===")
print()

# remove() - Eliminar por valor
animales = ["perro", "gato", "conejo", "pájaro", "gato"]
print("🐾 Lista de animales:", animales)

animales.remove("conejo")
print("   .remove('conejo') → Eliminar el conejo")
print("   Lista ahora:", animales)
print("   (Si hay duplicados, solo elimina el primero)")
print()

# pop() - Eliminar por índice (y devuelve el elemento)
print("🎯 POP (Eliminar por posición):")
frutas = ["manzana", "pera", "uva", "naranja"]
print("   Lista de frutas:", frutas)

fruta_removida = frutas.pop(1)  # Eliminar en posición 1
print(f"   .pop(1) → Eliminé '{fruta_removida}'")
print("   Lista ahora:", frutas)
print()

ultimo = frutas.pop()  # Sin índice, elimina el último
print(f"   .pop() → Eliminé '{ultimo}' (último elemento)")
print("   Lista ahora:", frutas)
print()

# clear() - Vaciar toda la lista
print("🗑️ CLEAR (Vaciar toda la lista):")
basura = [1, 2, 3, 4, 5]
print("   Lista:", basura)
basura.clear()
print("   .clear()")
print("   Lista ahora:", basura)
print()

print("-" * 60)
print()


# ============================================
# 6️⃣ BUSCAR EN LISTAS
# ============================================
print("=== 6. BUSCAR EN LISTAS ===")
print()

numeros = [10, 20, 30, 40, 20, 50]
print("🔍 Lista de números:", numeros)
print()

# index() - Encontrar la posición de un elemento
print("📍 INDEX (Encontrar posición):")
posicion = numeros.index(30)
print(f"   .index(30) → El 30 está en posición {posicion}")
print()

# count() - Contar cuántas veces aparece
print("🔢 COUNT (Contar apariciones):")
veces = numeros.count(20)
print(f"   .count(20) → El 20 aparece {veces} veces")
print()

# in - Verificar si existe
print("✅ IN (Verificar si existe):")
print(f"   30 in numeros → {30 in numeros}")
print(f"   100 in numeros → {100 in numeros}")
print()

print("-" * 60)
print()


# ============================================
# 7️⃣ ORDENAR LISTAS
# ============================================
print("=== 7. ORDENAR LISTAS ===")
print()

# sort() - Ordenar la lista original
print("📊 SORT (Ordenar de menor a mayor):")
puntos = [85, 92, 78, 95, 88]
print("   Lista original:", puntos)

puntos.sort()
print("   .sort()")
print("   Lista ordenada:", puntos)
print()

puntos.sort(reverse=True)
print("   .sort(reverse=True) → Ordenar de mayor a menor")
print("   Lista ordenada:", puntos)
print()

# sorted() - Crear una nueva lista ordenada (sin cambiar la original)
print("📋 SORTED (Crear nueva lista ordenada):")
numeros = [5, 2, 8, 1, 9]
print("   Lista original:", numeros)
numeros_ordenados = sorted(numeros)
print("   nueva_lista = sorted(numeros)")
print("   Lista original:", numeros, "(no cambió)")
print("   Nueva lista:", numeros_ordenados)
print()

# Ordenar textos alfabéticamente
nombres = ["María", "Ana", "Carlos", "Beatriz"]
print("📝 Ordenar nombres:")
print("   Original:", nombres)
nombres.sort()
print("   .sort():", nombres)
print()

print("-" * 60)
print()


# ============================================
# 8️⃣ SLICING EN LISTAS (Cortar listas)
# ============================================
print("=== 8. SLICING - CORTAR LISTAS ===")
print()

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("✂️ Lista de números:", numeros)
print()

print("🔪 CORTAR PEDAZOS:")
print(f"   numeros[0:3] = {numeros[0:3]}  (del 0 al 3, sin incluir 3)")
print(f"   numeros[3:7] = {numeros[3:7]}  (del 3 al 7)")
print(f"   numeros[:5] = {numeros[:5]}  (desde el inicio hasta 5)")
print(f"   numeros[5:] = {numeros[5:]}  (desde 5 hasta el final)")
print(f"   numeros[-3:] = {numeros[-3:]}  (últimos 3 elementos)")
print()

print("⏭️ CON SALTOS (step):")
print(f"   numeros[::2] = {numeros[::2]}  (cada 2 elementos)")
print(f"   numeros[1::2] = {numeros[1::2]}  (desde 1, cada 2)")
print(f"   numeros[::-1] = {numeros[::-1]}  (lista invertida)")
print()

print("-" * 60)
print()


# ============================================
# 9️⃣ RECORRER LISTAS (Loops)
# ============================================
print("=== 9. RECORRER LISTAS ===")
print()

print("🔁 FOR LOOP (Recorrer uno por uno):")
frutas = ["manzana", "pera", "uva"]

print("   Método 1 - Por elemento:")
for fruta in frutas:
    print(f"      Me gusta la {fruta}")
print()

print("   Método 2 - Por índice:")
for i in range(len(frutas)):
    print(f"      Fruta {i}: {frutas[i]}")
print()

print("   Método 3 - Con enumerate (índice y elemento):")
for i, fruta in enumerate(frutas):
    print(f"      Posición {i}: {fruta}")
print()

print("-" * 60)
print()


# ============================================
# 🔟 OPERACIONES CON LISTAS
# ============================================
print("=== 10. OPERACIONES CON LISTAS ===")
print()

# Concatenar listas
print("➕ CONCATENAR (Unir):")
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = lista1 + lista2
print(f"   {lista1} + {lista2} = {lista3}")
print()

# Repetir listas
print("✖️ REPETIR:")
lista = [0]
lista_repetida = lista * 5
print(f"   {lista} * 5 = {lista_repetida}")
print()

# Mínimo, máximo y suma
print("📊 MIN, MAX, SUM:")
numeros = [15, 8, 23, 4, 16, 42]
print(f"   Lista: {numeros}")
print(f"   min(numeros) = {min(numeros)}  (el menor)")
print(f"   max(numeros) = {max(numeros)}  (el mayor)")
print(f"   sum(numeros) = {sum(numeros)}  (la suma de todos)")
print()

print("-" * 60)
print()


# ============================================
# 🎯 EJEMPLOS PRÁCTICOS DIVERTIDOS
# ============================================
print("=== 🎯 EJEMPLOS PRÁCTICOS ===")
print()

# 📝 Lista de tareas
print("📝 LISTA DE TAREAS:")
tareas = ["Hacer tarea", "Pasear al perro", "Leer un libro"]
print("   Mis tareas:", tareas)

tareas.append("Estudiar Python")
print("   Agregué una tarea:", tareas)

tarea_completada = tareas.pop(0)
print(f"   ✅ Completé: {tarea_completada}")
print("   Tareas pendientes:", tareas)
print()

# 🎮 Sistema de puntajes
print("🎮 PUNTAJES DE VIDEOJUEGO:")
puntajes = [850, 920, 780, 1000, 950]
print("   Puntajes:", puntajes)
print(f"   Puntaje más alto: {max(puntajes)}")
print(f"   Puntaje más bajo: {min(puntajes)}")
print(f"   Promedio: {sum(puntajes) / len(puntajes):.2f}")
print()

# 🛒 Carrito de compras
print("🛒 CARRITO DE COMPRAS:")
carrito = []
print("   Carrito vacío:", carrito)

carrito.append("Laptop")
carrito.append("Mouse")
carrito.append("Teclado")
print("   Agregué productos:", carrito)

print(f"   Total de productos: {len(carrito)}")

if "Laptop" in carrito:
    print("   ✅ La laptop está en el carrito")
print()

# 👥 Registro de estudiantes
print("👥 REGISTRO DE CLASE:")
estudiantes = ["Ana", "Luis", "María", "Pedro", "Juan"]
print("   Estudiantes:", estudiantes)

# Estudiante nuevo
estudiantes.insert(2, "Sofia")
print("   Llegó Sofia (en medio):", estudiantes)

# Pasar lista
print("   📋 Pasando lista:")
for i, estudiante in enumerate(estudiantes, 1):
    print(f"      {i}. {estudiante}")
print()

# 🍕 Repartir pizza
print("🍕 REPARTIR PIZZA:")
porciones = [2, 3, 2, 4, 1]
nombres = ["Ana", "Luis", "María", "Pedro", "Juan"]

print("   Distribución de pizza:")
for nombre, porcion in zip(nombres, porciones):
    print(f"      {nombre} recibió {porcion} porciones")

total_porciones = sum(porciones)
print(f"   Total de porciones repartidas: {total_porciones}")
print()

# 📊 Top 3 calificaciones
print("📊 TOP 3 MEJORES CALIFICACIONES:")
calificaciones = [78, 92, 85, 95, 88, 90]
print("   Todas las calificaciones:", calificaciones)

top3 = sorted(calificaciones, reverse=True)[:3]
print("   🏆 Top 3:", top3)
print()

# 🎲 Juego de dados
print("🎲 HISTORIAL DE DADOS:")
tiradas = [random.randint(1, 6) for _ in range(10)]
print("   Tiradas:", tiradas)
print(f"   Cantidad de 6: {tiradas.count(6)}")
print(f"   Promedio: {sum(tiradas) / len(tiradas):.1f}")
print()

# 🎨 Paleta de colores favoritos
print("🎨 MIS COLORES FAVORITOS:")
colores_favoritos = ["azul", "verde", "morado", "rojo"]
print("   Lista original:", colores_favoritos)

# Invertir la lista
colores_favoritos.reverse()
print("   Lista invertida (.reverse()):", colores_favoritos)
print()

# 📱 Contactos
print("📱 AGENDA DE CONTACTOS:")
contactos = ["Mamá", "Papá", "Juan", "María", "Pedro"]
print("   Mis contactos:", contactos)
print(f"   Total de contactos: {len(contactos)}")
print(f"   Primer contacto: {contactos[0]}")
print(f"   Últimos 3 contactos: {contactos[-3:]}")
print()

print("=" * 60)
print("🎉 ¡Felicidades! Ya dominas las listas en Python 🎉")
print("=" * 60)
