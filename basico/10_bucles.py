"""
PYTHON DESDE CERO - LECCIÓN 10: BUCLES (FOR Y WHILE)
=====================================================

🔁 ¿Qué son los BUCLES?
-----------------------
Un bucle es como una RUEDA que da VUELTAS y VUELTAS.
Te permite REPETIR una acción muchas veces sin escribir el código otra vez.

Ejemplo en la vida real:
- Cantar "Feliz Cumpleaños" para 10 amigos (repetir 10 veces)
- Contar del 1 al 100 (repetir 100 veces)
- Revisar cada elemento de tu mochila (repetir hasta terminar)

En Python hay 2 tipos principales:
- FOR → Cuando sabes CUÁNTAS veces repetir
- WHILE → Cuando repites HASTA que algo cambie

¡Es como darle el botón de REPETIR a tu música!
"""

import string
import random
print("=" * 60)
print("🎓 LECCIÓN 10: BUCLES (FOR Y WHILE) EN PYTHON")
print("=" * 60)
print()

# ============================================
# 1️⃣ BUCLE FOR BÁSICO
# ============================================
print("=== 1. BUCLE FOR - REPETIR N VECES ===")
print()

print("🎯 EJEMPLO 1 - Contar del 1 al 5:")
for i in range(5):
    print(f"   {i + 1}")
print()

print("🎯 EJEMPLO 2 - Saludar 3 veces:")
for i in range(3):
    print(f"   ¡Hola! (repetición {i + 1})")
print()

print("🎯 EJEMPLO 3 - Dibujar estrellas:")
for i in range(7):
    print("   ⭐", end="")
print("\n")

print("💡 EXPLICACIÓN de range():")
print("   range(5) → genera: 0, 1, 2, 3, 4")
print("   (Empieza en 0 y termina ANTES del 5)")
print()

print("-" * 60)
print()


# ============================================
# 2️⃣ RANGE() CON DIFERENTES PARÁMETROS
# ============================================
print("=== 2. RANGE() - CONTROLAR EL RANGO ===")
print()

# range(inicio, fin)
print("🔹 range(inicio, fin):")
print("   Contar del 1 al 5:")
for i in range(1, 6):  # Del 1 al 5 (el 6 no se incluye)
    print(f"      {i}", end=" ")
print("\n")

# range(inicio, fin, salto)
print("🔹 range(inicio, fin, salto):")
print("   Números pares del 0 al 10:")
for i in range(0, 11, 2):  # De 2 en 2
    print(f"      {i}", end=" ")
print("\n")

print("   Números impares del 1 al 10:")
for i in range(1, 11, 2):
    print(f"      {i}", end=" ")
print("\n")

print("   Cuenta regresiva del 10 al 1:")
for i in range(10, 0, -1):  # Hacia atrás
    print(f"      {i}", end=" ")
print("\n")

print("-" * 60)
print()


# ============================================
# 3️⃣ FOR CON LISTAS
# ============================================
print("=== 3. FOR CON LISTAS ===")
print()

print("🎯 EJEMPLO 1 - Recorrer frutas:")
frutas = ["manzana", "pera", "uva", "naranja"]
for fruta in frutas:
    print(f"   Me gusta la {fruta}")
print()

print("🎯 EJEMPLO 2 - Suma de números:")
numeros = [10, 20, 30, 40, 50]
suma = 0
for numero in numeros:
    suma += numero
    print(f"   Sumando {numero} → Total: {suma}")
print(f"   Suma final: {suma}")
print()

print("🎯 EJEMPLO 3 - Contar letras de palabras:")
palabras = ["Python", "es", "genial"]
for palabra in palabras:
    print(f"   '{palabra}' tiene {len(palabra)} letras")
print()

print("-" * 60)
print()


# ============================================
# 4️⃣ ENUMERATE (índice + elemento)
# ============================================
print("=== 4. ENUMERATE - OBTENER ÍNDICE Y ELEMENTO ===")
print()

print("🎯 EJEMPLO - Lista numerada:")
frutas = ["manzana", "pera", "uva", "naranja"]
for indice, fruta in enumerate(frutas):
    print(f"   {indice + 1}. {fruta}")
print()

print("🎯 EJEMPLO - Comenzar desde otro número:")
colores = ["rojo", "azul", "verde"]
for numero, color in enumerate(colores, start=1):
    print(f"   Color #{numero}: {color}")
print()

print("-" * 60)
print()


# ============================================
# 5️⃣ FOR CON DICCIONARIOS
# ============================================
print("=== 5. FOR CON DICCIONARIOS ===")
print()

edades = {"Ana": 12, "Luis": 13, "María": 12}

print("🔹 Solo llaves:")
for nombre in edades:
    print(f"   {nombre}")
print()

print("🔹 Solo valores:")
for edad in edades.values():
    print(f"   {edad} años")
print()

print("🔹 Llaves y valores:")
for nombre, edad in edades.items():
    print(f"   {nombre} tiene {edad} años")
print()

print("-" * 60)
print()


# ============================================
# 6️⃣ BUCLES ANIDADOS (Uno dentro de otro)
# ============================================
print("=== 6. BUCLES ANIDADOS ===")
print()

print("🎯 EJEMPLO 1 - Tabla de multiplicar del 1 al 3:")
for i in range(1, 4):  # Tablas del 1 al 3
    print(f"   Tabla del {i}:")
    for j in range(1, 6):  # Del 1 al 5
        print(f"      {i} × {j} = {i * j}")
    print()

print("🎯 EJEMPLO 2 - Dibujar un cuadrado:")
filas = 4
columnas = 6
for i in range(filas):
    for j in range(columnas):
        print("   ■", end="")
    print()  # Salto de línea
print()

print("-" * 60)
print()


# ============================================
# 7️⃣ WHILE - REPETIR MIENTRAS SEA VERDAD
# ============================================
print("=== 7. BUCLE WHILE - REPETIR MIENTRAS... ===")
print()

print("🎯 EJEMPLO 1 - Contar del 1 al 5:")
contador = 1
while contador <= 5:
    print(f"   Número: {contador}")
    contador += 1  # ¡IMPORTANTE! Incrementar el contador
print()

print("🎯 EJEMPLO 2 - Cuenta regresiva:")
cuenta = 5
while cuenta > 0:
    print(f"   {cuenta}...")
    cuenta -= 1
print("   🚀 ¡Despegue!")
print()

print("🎯 EJEMPLO 3 - Juntar dinero:")
dinero = 0
meta = 50
dia = 1

while dinero < meta:
    ahorro_dia = 10
    dinero += ahorro_dia
    print(f"   Día {dia}: Ahorré ${ahorro_dia} → Total: ${dinero}")
    dia += 1
print(f"   🎉 ¡Llegué a mi meta de ${meta}!")
print()

print("⚠️ CUIDADO: Si la condición NUNCA se vuelve False, el bucle será INFINITO")
print()

print("-" * 60)
print()


# ============================================
# 8️⃣ BREAK - SALIR DEL BUCLE
# ============================================
print("=== 8. BREAK - SALIR DEL BUCLE ===")
print()

print("🎯 EJEMPLO 1 - Buscar un número:")
numeros = [5, 12, 8, 20, 15, 30]
buscar = 20

for numero in numeros:
    print(f"   Revisando: {numero}")
    if numero == buscar:
        print(f"   ✅ ¡Encontré el {buscar}!")
        break  # Salir del bucle
print()

print("🎯 EJEMPLO 2 - Límite de intentos:")
intentos = 0
max_intentos = 3

while True:  # Bucle infinito
    intentos += 1
    print(f"   Intento #{intentos}")

    if intentos >= max_intentos:
        print("   ❌ Llegaste al límite de intentos")
        break
print()

print("-" * 60)
print()


# ============================================
# 9️⃣ CONTINUE - SALTAR A LA SIGUIENTE ITERACIÓN
# ============================================
print("=== 9. CONTINUE - SALTAR ITERACIÓN ===")
print()

print("🎯 EJEMPLO 1 - Saltar números pares:")
print("   Números impares del 1 al 10:")
for i in range(1, 11):
    if i % 2 == 0:  # Si es par
        continue  # Saltar al siguiente
    print(f"      {i}")
print()

print("🎯 EJEMPLO 2 - Filtrar palabras cortas:")
palabras = ["sol", "Python", "luz", "programación", "día"]
print("   Palabras con más de 3 letras:")
for palabra in palabras:
    if len(palabra) <= 3:
        continue  # Saltar palabras cortas
    print(f"      {palabra}")
print()

print("-" * 60)
print()


# ============================================
# 🔟 ELSE EN BUCLES
# ============================================
print("=== 10. ELSE EN BUCLES ===")
print()

print("🎯 EJEMPLO 1 - Buscar con éxito:")
numeros = [3, 7, 12, 18, 25]
buscar = 12

for num in numeros:
    if num == buscar:
        print(f"   ✅ Encontré {buscar}")
        break
else:
    # Se ejecuta si NO se usó break
    print(f"   ❌ No encontré {buscar}")
print()

print("🎯 EJEMPLO 2 - Sin encontrar:")
numeros = [3, 7, 12, 18, 25]
buscar = 99

for num in numeros:
    if num == buscar:
        print(f"   ✅ Encontré {buscar}")
        break
else:
    print(f"   ❌ No encontré {buscar}")
print()

print("-" * 60)
print()


# ============================================
# 🎯 EJEMPLOS PRÁCTICOS DIVERTIDOS
# ============================================
print("=== 🎯 EJEMPLOS PRÁCTICOS ===")
print()

# 🎂 Cantar cumpleaños
print("🎂 CANTAR CUMPLEAÑOS:")
nombre = "Ana"
for i in range(3):
    print("   ♫ Feliz cumpleaños ♫")
print(f"   ♫ Feliz cumpleaños querida {nombre} ♫")
print()

# 🎮 Barra de vida
print("🎮 BARRA DE VIDA:")
vida_maxima = 10
vida_actual = 7

print("   Vida: ", end="")
for i in range(vida_maxima):
    if i < vida_actual:
        print("❤️ ", end="")
    else:
        print("🖤 ", end="")
print(f" ({vida_actual}/{vida_maxima})")
print()

# 📊 Promedio de calificaciones
print("📊 CALCULAR PROMEDIO:")
calificaciones = [85, 92, 78, 90, 88]
suma = 0

print(f"   Calificaciones: {calificaciones}")
for nota in calificaciones:
    suma += nota

promedio = suma / len(calificaciones)
print(f"   Promedio: {promedio:.1f}")
print()

# 🔢 Tabla de multiplicar
print("🔢 TABLA DEL 7:")
numero = 7
for i in range(1, 11):
    resultado = numero * i
    print(f"   7 × {i:2} = {resultado:2}")
print()

# 🎲 Tirar un dado
print("🎲 TIRAR DADO 5 VECES:")
for i in range(1, 6):
    dado = random.randint(1, 6)
    print(f"   Tirada {i}: 🎲 {dado}")
print()

# 🌟 Pirámide de estrellas
print("🌟 PIRÁMIDE:")
altura = 5
for i in range(1, altura + 1):
    espacios = " " * (altura - i)
    estrellas = "⭐" * i
    print(f"   {espacios}{estrellas}")
print()

# 📝 Contar vocales
print("📝 CONTAR VOCALES:")
texto = "Python es genial"
vocales = "aeiouAEIOU"
contador = 0

for letra in texto:
    if letra in vocales:
        contador += 1

print(f"   Texto: '{texto}'")
print(f"   Vocales encontradas: {contador}")
print()

# 🎯 Números primos
print("🎯 NÚMEROS PRIMOS DEL 1 AL 20:")
print("   ", end="")
for num in range(2, 21):
    es_primo = True
    for i in range(2, num):
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        print(num, end=" ")
print("\n")

# 🛒 Total del carrito
print("🛒 CARRITO DE COMPRAS:")
productos = {
    "Laptop": 599.99,
    "Mouse": 29.99,
    "Teclado": 79.99
}

total = 0
print("   Productos:")
for producto, precio in productos.items():
    print(f"      {producto}: ${precio}")
    total += precio

print(f"   Total a pagar: ${total:.2f}")
print()

# 📨 Validar email
print("📨 VALIDAR EMAILS:")
emails = ["ana@mail.com", "luis.mail.com", "maria@gmail.com", "@error.com"]

for email in emails:
    if "@" in email and "." in email:
        print(f"   ✅ {email} es válido")
    else:
        print(f"   ❌ {email} es inválido")
print()

# 🎰 Juego de adivinanza
print("🎰 JUEGO DE ADIVINANZA (simulado):")
numero_secreto = 7
intentos = [3, 5, 7]

for intento in intentos:
    print(f"   Intento: {intento}")
    if intento == numero_secreto:
        print(f"   🎉 ¡Correcto! Era {numero_secreto}")
        break
    elif intento < numero_secreto:
        print("   ⬆️ Más alto")
    else:
        print("   ⬇️ Más bajo")
print()

# 🏆 Top 3 puntajes
print("🏆 TOP 3 PUNTAJES:")
puntajes = [850, 920, 780, 950, 880]
puntajes_ordenados = sorted(puntajes, reverse=True)

for posicion, puntaje in enumerate(puntajes_ordenados[:3], 1):
    if posicion == 1:
        medalla = "🥇"
    elif posicion == 2:
        medalla = "🥈"
    else:
        medalla = "🥉"
    print(f"   {medalla} Posición {posicion}: {puntaje} puntos")
print()

# ⏱️ Contador regresivo
print("⏱️ CUENTA REGRESIVA:")
tiempo = 5
while tiempo > 0:
    print(f"   {tiempo}...", end=" ")
    tiempo -= 1
print("🎉 ¡Feliz Año Nuevo!")
print()

# 📱 Batería descargándose
print("🔋 BATERÍA DESCARGÁNDOSE:")
bateria = 100
while bateria > 0:
    if bateria % 20 == 0:  # Mostrar cada 20%
        print(f"   Batería: {bateria}%")
    bateria -= 10
print("   🔴 Batería agotada")
print()

# 🎨 Generar paleta de colores
print("🎨 CÓDIGOS DE COLORES RGB:")
colores = {
    "Rojo": (255, 0, 0),
    "Verde": (0, 255, 0),
    "Azul": (0, 0, 255),
    "Amarillo": (255, 255, 0)
}

for nombre, (r, g, b) in colores.items():
    print(f"   {nombre}: RGB({r}, {g}, {b})")
print()

# 🌡️ Temperaturas de la semana
print("🌡️ ANÁLISIS DE TEMPERATURAS:")
temperaturas = [22, 24, 23, 25, 26, 28, 27]
dias = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]

temp_max = max(temperaturas)
temp_min = min(temperaturas)
temp_prom = sum(temperaturas) / len(temperaturas)

print("   Temperaturas de la semana:")
for dia, temp in zip(dias, temperaturas):
    if temp == temp_max:
        emoji = "🔥"
    elif temp == temp_min:
        emoji = "❄️"
    else:
        emoji = "🌡️"
    print(f"      {dia}: {temp}°C {emoji}")

print(f"\n   Máxima: {temp_max}°C")
print(f"   Mínima: {temp_min}°C")
print(f"   Promedio: {temp_prom:.1f}°C")
print()

# 🎵 Lista de reproducción
print("🎵 REPRODUCIENDO PLAYLIST:")
canciones = ["Canción 1", "Canción 2", "Canción 3", "Canción 4"]

for i, cancion in enumerate(canciones, 1):
    print(f"   ▶️ Ahora suena: {cancion} ({i}/{len(canciones)})")
print("   ✅ Playlist terminada")
print()

# 🎯 Fibonacci
print("🔢 SERIE DE FIBONACCI (primeros 10 números):")
a, b = 0, 1
print("   ", end="")
for i in range(10):
    print(a, end=" ")
    a, b = b, a + b
print("\n")

# 🎪 Patrón de números
print("🎪 PATRÓN TRIANGULAR:")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(f"   {j}", end=" ")
    print()
print()

# 🔐 Generar contraseña
print("🔐 GENERAR CONTRASEÑA ALEATORIA:")
caracteres = string.ascii_letters + string.digits
contraseña = ""
for i in range(8):
    contraseña += random.choice(caracteres)
print(f"   Contraseña generada: {contraseña}")
print()

# 🎖️ Sistema de recompensas
print("🎖️ SISTEMA DE RECOMPENSAS POR RACHA:")
dias_consecutivos = [1, 2, 3, 4, 5, 6, 7]

for dia in dias_consecutivos:
    if dia % 7 == 0:
        recompensa = "🏆 Gran premio"
    elif dia % 3 == 0:
        recompensa = "🎁 Regalo especial"
    else:
        recompensa = "⭐ Estrella"
    print(f"   Día {dia}: {recompensa}")
print()

# 🎲 Simular lanzamientos hasta sacar 6
print("🎲 LANZAR HASTA SACAR UN 6:")
lanzamientos = 0
while True:
    lanzamientos += 1
    dado = random.randint(1, 6)
    print(f"   Lanzamiento {lanzamientos}: 🎲 {dado}")
    if dado == 6:
        print(f"   🎉 ¡Sacaste 6 en {lanzamientos} intentos!")
        break
    if lanzamientos >= 10:  # Límite de seguridad
        print("   ⏱️ Límite de lanzamientos alcanzado")
        break
print()

# 📚 Invertir una palabra
print("📚 INVERTIR PALABRA:")
palabra = "Python"
palabra_invertida = ""

for letra in palabra:
    palabra_invertida = letra + palabra_invertida

print(f"   Original: {palabra}")
print(f"   Invertida: {palabra_invertida}")
print()

print("=" * 60)
print("🎉 ¡Felicidades! Ya dominas los Bucles en Python 🎉")
print("=" * 60)
print()
print("📌 RESUMEN:")
print("   - FOR → Cuando sabes cuántas veces repetir")
print("   - WHILE → Repite mientras la condición sea True")
print("   - range(n) → 0, 1, 2, ..., n-1")
print("   - range(inicio, fin, salto) → Control completo")
print("   - enumerate() → Obtener índice y elemento")
print("   - BREAK → Salir del bucle")
print("   - CONTINUE → Saltar a la siguiente iteración")
print("   - ELSE → Se ejecuta si no hubo break")
print("=" * 60)
