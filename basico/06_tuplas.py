"""
PYTHON DESDE CERO - LECCIÓN 6: TUPLAS
======================================

📦 ¿Qué es una TUPLA?
---------------------
Una tupla es como una CAJA SELLADA donde guardas cosas que NO VAN A CAMBIAR.

Es MUY parecida a una LISTA, pero con una diferencia importante:
- LISTA = Mochila (puedes meter y sacar cosas) ✏️
- TUPLA = Caja sellada (una vez que guardas algo, ya no lo puedes cambiar) 🔒

Ejemplo en la vida real:
- Las coordenadas de tu casa: (lat: -12.04, lon: -77.03) ← No cambian
- Los meses del año: ("Enero", "Febrero", "Marzo"...) ← Siempre iguales
- Tu fecha de nacimiento: (15, "Marzo", 2010) ← No cambia

Las tuplas se escriben con PARÉNTESIS ( ) y se separan con COMAS
"""

print("=" * 60)
print("🎓 LECCIÓN 6: TUPLAS EN PYTHON")
print("=" * 60)
print()

# ============================================
# 1️⃣ CREAR TUPLAS
# ============================================
print("=== 1. CÓMO CREAR TUPLAS ===")
print()

# Tupla de frutas
frutas = ("manzana", "pera", "uva", "naranja")
print("🍎 Tupla de frutas:", frutas)

# Tupla de números
numeros = (10, 20, 30, 40, 50)
print("🔢 Tupla de números:", numeros)

# Tupla mixta
datos = ("Juan", 12, True, 1.75)
print("📦 Tupla mixta:", datos, "(nombre, edad, estudiante, altura)")

# Tupla de un solo elemento (OJO: necesita una coma)
un_elemento = (5,)  # La coma es IMPORTANTE
print("☝️ Tupla de un elemento:", un_elemento, "← Necesita coma")

# Sin la coma, NO es tupla
no_es_tupla = (5)  # Esto es solo un número
print("❌ Sin coma NO es tupla:", no_es_tupla, type(no_es_tupla))

# Tupla vacía
tupla_vacia = ()
print("📭 Tupla vacía:", tupla_vacia)

# También se puede crear sin paréntesis (empaquetado)
colores = "rojo", "azul", "verde"
print("🎨 Sin paréntesis también funciona:", colores, type(colores))

print()
print("-" * 60)
print()


# ============================================
# 2️⃣ ACCEDER A ELEMENTOS
# ============================================
print("=== 2. ACCEDER A ELEMENTOS DE LA TUPLA ===")
print()

dias_semana = ("Lunes", "Martes", "Miércoles",
               "Jueves", "Viernes", "Sábado", "Domingo")
print("📅 Días de la semana:", dias_semana)
print()

# Los índices empiezan en 0 (igual que las listas)
print("📍 ACCEDER POR ÍNDICE:")
print(f"   dias_semana[0] = {dias_semana[0]}  (primer día)")
print(f"   dias_semana[4] = {dias_semana[4]}  (viernes)")
print(f"   dias_semana[-1] = {dias_semana[-1]}  (último día)")
print()

# Longitud
print(f"📏 Cantidad de días: len(dias_semana) = {len(dias_semana)}")
print()

print("-" * 60)
print()


# ============================================
# 3️⃣ LA GRAN DIFERENCIA: INMUTABILIDAD
# ============================================
print("=== 3. ¡LAS TUPLAS NO SE PUEDEN MODIFICAR! ===")
print()

print("🔴 DIFERENCIA PRINCIPAL:")
print()

# Con LISTA (mutable - se puede cambiar) ✅
lista_frutas = ["manzana", "pera", "uva"]
print("📝 LISTA:", lista_frutas)
lista_frutas[0] = "sandía"  # ✅ Esto SÍ funciona
print("   Cambié el primer elemento:", lista_frutas)
print()

# Con TUPLA (inmutable - NO se puede cambiar) ❌
tupla_frutas = ("manzana", "pera", "uva")
print("📦 TUPLA:", tupla_frutas)
print("   ❌ NO puedo hacer: tupla_frutas[0] = 'sandía'")
print("   ❌ Daría ERROR: TypeError")
print()

print("💡 ¿Por qué usar tuplas?")
print("   1. Son MÁS RÁPIDAS que las listas")
print("   2. PROTEGEN los datos (nadie los puede cambiar por error)")
print("   3. Se pueden usar como LLAVES en diccionarios")
print("   4. Son más SEGURAS para datos que no deben cambiar")
print()

print("-" * 60)
print()


# ============================================
# 4️⃣ MÉTODOS DE TUPLAS (Solo 2)
# ============================================
print("=== 4. MÉTODOS DE TUPLAS ===")
print()

numeros = (5, 10, 15, 10, 20, 10, 25)
print("🔍 Tupla de números:", numeros)
print()

# count() - Contar cuántas veces aparece un valor
print("🔢 COUNT (Contar apariciones):")
veces = numeros.count(10)
print(f"   numeros.count(10) → El 10 aparece {veces} veces")
print()

# index() - Encontrar la posición de un valor
print("📍 INDEX (Encontrar posición):")
posicion = numeros.index(15)
print(f"   numeros.index(15) → El 15 está en posición {posicion}")
print()

print("💡 Las tuplas SOLO tienen 2 métodos:")
print("   - count() para contar")
print("   - index() para buscar posición")
print("   (Las listas tienen más: append, remove, sort, etc.)")
print()

print("-" * 60)
print()


# ============================================
# 5️⃣ SLICING EN TUPLAS
# ============================================
print("=== 5. SLICING - CORTAR TUPLAS ===")
print()

numeros = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print("✂️ Tupla de números:", numeros)
print()

print("🔪 CORTAR PEDAZOS (igual que listas):")
print(f"   numeros[0:4] = {numeros[0:4]}")
print(f"   numeros[5:] = {numeros[5:]}")
print(f"   numeros[:3] = {numeros[:3]}")
print(f"   numeros[-3:] = {numeros[-3:]}")
print(f"   numeros[::2] = {numeros[::2]}  (cada 2 elementos)")
print(f"   numeros[::-1] = {numeros[::-1]}  (invertida)")
print()

print("-" * 60)
print()


# ============================================
# 6️⃣ DESEMPAQUETADO DE TUPLAS
# ============================================
print("=== 6. DESEMPAQUETADO DE TUPLAS ===")
print("(Extraer valores a variables separadas)")
print()

# Desempaquetado básico
print("📤 DESEMPAQUETADO BÁSICO:")
coordenadas = (10, 20)
x, y = coordenadas
print(f"   Tupla: {coordenadas}")
print(f"   x = {x}")
print(f"   y = {y}")
print()

# Ejemplo: Datos de persona
print("👤 EJEMPLO - DATOS DE PERSONA:")
persona = ("Ana", 12, "Lima")
nombre, edad, ciudad = persona
print(f"   Tupla: {persona}")
print(f"   Nombre: {nombre}")
print(f"   Edad: {edad}")
print(f"   Ciudad: {ciudad}")
print()

# Intercambiar valores (muy útil)
print("🔄 INTERCAMBIAR VALORES:")
a = 5
b = 10
print(f"   Antes: a = {a}, b = {b}")
a, b = b, a  # ¡Magia! Se intercambian
print(f"   Después: a = {a}, b = {b}")
print()

# Desempaquetado con * (resto de elementos)
print("⭐ DESEMPAQUETADO CON * (Resto):")
numeros = (1, 2, 3, 4, 5, 6)
primero, segundo, *resto = numeros
print(f"   Tupla: {numeros}")
print(f"   Primero: {primero}")
print(f"   Segundo: {segundo}")
print(f"   Resto: {resto}")
print()

print("-" * 60)
print()


# ============================================
# 7️⃣ RECORRER TUPLAS
# ============================================
print("=== 7. RECORRER TUPLAS ===")
print()

colores = ("rojo", "azul", "verde", "amarillo")
print("🎨 Tupla de colores:", colores)
print()

print("🔁 MÉTODO 1 - Por elemento:")
for color in colores:
    print(f"   Color: {color}")
print()

print("🔁 MÉTODO 2 - Con índice:")
for i in range(len(colores)):
    print(f"   Posición {i}: {colores[i]}")
print()

print("🔁 MÉTODO 3 - Con enumerate:")
for i, color in enumerate(colores):
    print(f"   {i}. {color}")
print()

print("-" * 60)
print()


# ============================================
# 8️⃣ OPERACIONES CON TUPLAS
# ============================================
print("=== 8. OPERACIONES CON TUPLAS ===")
print()

# Concatenar tuplas
print("➕ CONCATENAR (Unir tuplas):")
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla3 = tupla1 + tupla2
print(f"   {tupla1} + {tupla2} = {tupla3}")
print()

# Repetir tuplas
print("✖️ REPETIR:")
tupla = ("Hola",)
tupla_repetida = tupla * 3
print(f"   {tupla} * 3 = {tupla_repetida}")
print()

# Verificar pertenencia
print("✅ VERIFICAR SI EXISTE (in):")
frutas = ("manzana", "pera", "uva")
print(f"   Tupla: {frutas}")
print(f"   'pera' in frutas → {'pera' in frutas}")
print(f"   'kiwi' in frutas → {'kiwi' in frutas}")
print()

# Min, Max, Sum (con números)
print("📊 MIN, MAX, SUM:")
numeros = (15, 8, 23, 4, 16)
print(f"   Tupla: {numeros}")
print(f"   min(numeros) = {min(numeros)}")
print(f"   max(numeros) = {max(numeros)}")
print(f"   sum(numeros) = {sum(numeros)}")
print()

print("-" * 60)
print()


# ============================================
# 9️⃣ CONVERTIR ENTRE TUPLAS Y LISTAS
# ============================================
print("=== 9. CONVERTIR ENTRE TUPLAS Y LISTAS ===")
print()

# Tupla → Lista
print("📦 → 📝 TUPLA A LISTA:")
tupla_original = (1, 2, 3, 4, 5)
lista_convertida = list(tupla_original)
print(f"   Tupla: {tupla_original} (tipo: {type(tupla_original).__name__})")
print(
    f"   Lista: {lista_convertida} (tipo: {type(lista_convertida).__name__})")
print()

# Lista → Tupla
print("📝 → 📦 LISTA A TUPLA:")
lista_original = ["a", "b", "c"]
tupla_convertida = tuple(lista_original)
print(f"   Lista: {lista_original} (tipo: {type(lista_original).__name__})")
print(
    f"   Tupla: {tupla_convertida} (tipo: {type(tupla_convertida).__name__})")
print()

# ¿Para qué sirve esto?
print("💡 ¿CUÁNDO ES ÚTIL?")
print("   Si necesitas modificar una tupla:")
print("   1. Conviértela a lista")
print("   2. Modifica la lista")
print("   3. Conviértela de vuelta a tupla")
print()

# Ejemplo práctico
tupla_meses = ("Enero", "Febrero", "Marzo")
print(f"   Tupla original: {tupla_meses}")
lista_meses = list(tupla_meses)
lista_meses.append("Abril")
tupla_meses = tuple(lista_meses)
print(f"   Tupla modificada: {tupla_meses}")
print()

print("-" * 60)
print()


# ============================================
# 🔟 TUPLAS VS LISTAS - ¿CUÁNDO USAR CADA UNA?
# ============================================
print("=== 10. TUPLAS VS LISTAS - ¿CUÁL USAR? ===")
print()

print("📦 USA TUPLAS cuando:")
print("   ✅ Los datos NO deben cambiar")
print("   ✅ Coordenadas: (lat, lon)")
print("   ✅ Fechas: (día, mes, año)")
print("   ✅ Configuraciones fijas")
print("   ✅ Retornar múltiples valores de funciones")
print("   ✅ Necesitas más velocidad")
print()

print("📝 USA LISTAS cuando:")
print("   ✅ Los datos PUEDEN cambiar")
print("   ✅ Lista de tareas (agregas/quitas)")
print("   ✅ Carrito de compras")
print("   ✅ Historial de puntajes")
print("   ✅ Cualquier colección dinámica")
print()

print("-" * 60)
print()


# ============================================
# 🎯 EJEMPLOS PRÁCTICOS DIVERTIDOS
# ============================================
print("=== 🎯 EJEMPLOS PRÁCTICOS ===")
print()

# 📍 Coordenadas GPS
print("📍 COORDENADAS GPS:")
casa = (-12.0464, -77.0428)
escuela = (-12.0520, -77.0365)
print(f"   Casa: {casa}")
print(f"   Escuela: {escuela}")
lat_casa, lon_casa = casa
print(f"   Latitud de casa: {lat_casa}")
print(f"   Longitud de casa: {lon_casa}")
print()

# 🎂 Fecha de nacimiento
print("🎂 FECHA DE NACIMIENTO:")
fecha_nacimiento = (15, "Marzo", 2010)
dia, mes, año = fecha_nacimiento
print(f"   Fecha completa: {fecha_nacimiento}")
print(f"   Nací el {dia} de {mes} de {año}")
print()

# 🎨 Colores RGB
print("🎨 COLORES RGB:")
rojo = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)
morado = (128, 0, 128)

print(f"   Rojo: {rojo}")
print(f"   Verde: {verde}")
print(f"   Azul: {azul}")
print(f"   Morado: {morado}")

r, g, b = morado
print(f"   El morado tiene: R={r}, G={g}, B={b}")
print()

# 📐 Dimensiones (ancho, alto)
print("📐 DIMENSIONES:")
pantalla_laptop = (1920, 1080)
pantalla_telefono = (1080, 2340)

ancho, alto = pantalla_laptop
print(f"   Laptop: {pantalla_laptop}")
print(f"   Ancho: {ancho}px, Alto: {alto}px")
print()

# 🎮 Estadísticas de jugador
print("🎮 ESTADÍSTICAS DE JUGADOR:")
jugador = ("ProGamer123", 1500, 42, 38)
nombre, puntos, victorias, derrotas = jugador

print(f"   Datos: {jugador}")
print(f"   Jugador: {nombre}")
print(f"   Puntos: {puntos}")
print(f"   Victorias: {victorias}")
print(f"   Derrotas: {derrotas}")
print(f"   Ratio V/D: {victorias/derrotas:.2f}")
print()

# 📊 Calificaciones de trimestre
print("📊 CALIFICACIONES DEL TRIMESTRE:")
matematicas = (85, 90, 92)
ciencias = (88, 85, 90)

print(f"   Matemáticas: {matematicas}")
print(f"   Promedio: {sum(matematicas) / len(matematicas):.1f}")

print(f"   Ciencias: {ciencias}")
print(f"   Promedio: {sum(ciencias) / len(ciencias):.1f}")
print()

# 🌡️ Temperatura (min, max, promedio)
print("🌡️ TEMPERATURAS DEL DÍA:")
lunes = (18, 28, 23)
martes = (19, 30, 24)

min_lun, max_lun, prom_lun = lunes
min_mar, max_mar, prom_mar = martes

print(f"   Lunes: Min={min_lun}°C, Max={max_lun}°C, Promedio={prom_lun}°C")
print(f"   Martes: Min={min_mar}°C, Max={max_mar}°C, Promedio={prom_mar}°C")
print()

# 🎯 Retornar múltiples valores
print("🎯 FUNCIÓN QUE RETORNA MÚLTIPLES VALORES:")


def calcular_estadisticas(numeros_lista):
    """Función que retorna min, max y promedio"""
    minimo = min(numeros_lista)
    maximo = max(numeros_lista)
    promedio = sum(numeros_lista) / len(numeros_lista)
    return (minimo, maximo, promedio)  # Retorna una tupla


notas = [85, 92, 78, 90, 88]
print(f"   Notas: {notas}")

# Desempaquetar los resultados
min_nota, max_nota, prom_nota = calcular_estadisticas(notas)
print(f"   Nota mínima: {min_nota}")
print(f"   Nota máxima: {max_nota}")
print(f"   Promedio: {prom_nota:.1f}")
print()

# 🎲 Dados
print("🎲 LANZAMIENTO DE DADOS:")
dados = (
    (3, 5),  # Jugador 1
    (6, 6),  # Jugador 2
    (2, 4),  # Jugador 3
)

for i, (dado1, dado2) in enumerate(dados, 1):
    total = dado1 + dado2
    print(f"   Jugador {i}: dado1={dado1}, dado2={dado2}, total={total}")
print()

# 📅 Días laborables
print("📅 DÍAS LABORABLES:")
dias_laborables = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes")
fin_semana = ("Sábado", "Domingo")

print(f"   Trabajo: {dias_laborables}")
print(f"   Descanso: {fin_semana}")
print(f"   Total días laborables: {len(dias_laborables)}")
print()

# 🏆 Top 3 puntajes (tuplas anidadas)
print("🏆 TOP 3 PUNTAJES:")
top3 = (
    ("ProGamer", 9500),
    ("MasterX", 9200),
    ("Champion", 9000)
)

print("   🥇 🥈 🥉")
for posicion, (usuario, puntaje) in enumerate(top3, 1):
    print(f"   {posicion}. {usuario}: {puntaje} puntos")
print()

print("=" * 60)
print("🎉 ¡Felicidades! Ya dominas las tuplas en Python 🎉")
print("=" * 60)
print()
print("📌 RESUMEN:")
print("   - Tuplas = Inmutables (no se pueden modificar)")
print("   - Se crean con paréntesis: (1, 2, 3)")
print("   - Más rápidas que las listas")
print("   - Perfectas para datos que no cambian")
print("   - Solo 2 métodos: count() e index()")
print("=" * 60)
