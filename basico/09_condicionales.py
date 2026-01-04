"""
PYTHON DESDE CERO - LECCIÓN 9: CONDICIONALES (IF, ELSE, ELIF)
==============================================================

🔀 ¿Qué son los CONDICIONALES?
------------------------------
Los condicionales son como DECISIONES en la vida real.
Son instrucciones que le dicen a Python: "SI pasa esto, haz aquello"

Ejemplo en la vida real:
- SI tengo hambre → como algo
- SI llueve → llevo paraguas
- SI es fin de semana → juego videojuegos
- SI NO (ELSE) → hago tarea

En Python usamos:
- IF (si) → Para la primera condición
- ELIF (si no, si) → Para más opciones
- ELSE (si no) → Para cuando nada de lo anterior se cumple

¡Es como elegir caminos en un laberinto!
"""

print("=" * 60)
print("🎓 LECCIÓN 9: CONDICIONALES EN PYTHON")
print("=" * 60)
print()

# ============================================
# 1️⃣ IF SIMPLE (SI)
# ============================================
print("=== 1. IF SIMPLE (SI) ===")
print()

print("🎯 EJEMPLO 1 - ¿Tengo hambre?")
tengo_hambre = True

if tengo_hambre:
    print("   ✅ Como algo delicioso")

print("   (Continúo con el día)")
print()

print("🎯 EJEMPLO 2 - Verificar edad")
edad = 15

if edad >= 13:
    print(f"   Con {edad} años, eres adolescente")

print()

print("🎯 EJEMPLO 3 - ¿Aprobé el examen?")
calificacion = 85

if calificacion >= 70:
    print(f"   🎉 ¡Aprobaste con {calificacion} puntos!")

print()

print("💡 RECUERDA:")
print("   - Después del IF va una CONDICIÓN")
print("   - La condición debe ser True o False")
print("   - El código dentro debe estar INDENTADO (con espacios)")
print()

print("-" * 60)
print()


# ============================================
# 2️⃣ IF-ELSE (SI-SINO)
# ============================================
print("=== 2. IF-ELSE (SI-SINO) ===")
print()

print("🎯 EJEMPLO 1 - ¿Está lloviendo?")
esta_lloviendo = False

if esta_lloviendo:
    print("   ☔ Llevo paraguas")
else:
    print("   ☀️ Salgo sin paraguas")

print()

print("🎯 EJEMPLO 2 - Mayor o menor de edad")
edad = 16

if edad >= 18:
    print(f"   ✅ Con {edad} años, eres mayor de edad")
else:
    print(f"   ❌ Con {edad} años, eres menor de edad")

print()

print("🎯 EJEMPLO 3 - Número par o impar")
numero = 7

if numero % 2 == 0:
    print(f"   {numero} es PAR")
else:
    print(f"   {numero} es IMPAR")

print()

print("💡 EL CAMINO SE DIVIDE EN 2:")
print("   - SI se cumple → ejecuta el IF")
print("   - SI NO se cumple → ejecuta el ELSE")
print()

print("-" * 60)
print()


# ============================================
# 3️⃣ IF-ELIF-ELSE (SI-SINO SI-SINO)
# ============================================
print("=== 3. IF-ELIF-ELSE (Múltiples opciones) ===")
print()

print("🎯 EJEMPLO 1 - Calificación con letra")
nota = 85

if nota >= 90:
    print(f"   Nota: {nota} → Calificación: A (Excelente)")
elif nota >= 80:
    print(f"   Nota: {nota} → Calificación: B (Muy bien)")
elif nota >= 70:
    print(f"   Nota: {nota} → Calificación: C (Bien)")
else:
    print(f"   Nota: {nota} → Calificación: D (Reprobado)")

print()

print("🎯 EJEMPLO 2 - Qué hacer según el día")
dia = "Sábado"

if dia == "Lunes" or dia == "Martes" or dia == "Miércoles" or dia == "Jueves" or dia == "Viernes":
    print(f"   {dia} → 📚 Ir a la escuela")
elif dia == "Sábado":
    print(f"   {dia} → 🎮 Jugar videojuegos")
elif dia == "Domingo":
    print(f"   {dia} → 👨‍👩‍👧‍👦 Salir con la familia")
else:
    print(f"   {dia} → ❓ No es un día válido")

print()

print("🎯 EJEMPLO 3 - Tamaño de ropa")
altura_cm = 165

if altura_cm < 140:
    print(f"   Altura: {altura_cm}cm → Talla: S (Small)")
elif altura_cm < 160:
    print(f"   Altura: {altura_cm}cm → Talla: M (Medium)")
elif altura_cm < 180:
    print(f"   Altura: {altura_cm}cm → Talla: L (Large)")
else:
    print(f"   Altura: {altura_cm}cm → Talla: XL (Extra Large)")

print()

print("💡 PUEDES TENER MUCHOS ELIF:")
print("   IF → Primera condición")
print("   ELIF → Segunda condición")
print("   ELIF → Tercera condición")
print("   ELIF → Cuarta condición...")
print("   ELSE → Si ninguna se cumplió")
print()

print("-" * 60)
print()


# ============================================
# 4️⃣ OPERADORES DE COMPARACIÓN
# ============================================
print("=== 4. OPERADORES DE COMPARACIÓN ===")
print()

x = 10
y = 20

print(f"x = {x}, y = {y}")
print()

print("== IGUAL A:")
if x == 10:
    print(f"   ✅ {x} == 10 es True")
print()

print("!= DIFERENTE DE:")
if x != y:
    print(f"   ✅ {x} != {y} es True")
print()

print("> MAYOR QUE:")
if y > x:
    print(f"   ✅ {y} > {x} es True")
print()

print("< MENOR QUE:")
if x < y:
    print(f"   ✅ {x} < {y} es True")
print()

print(">= MAYOR O IGUAL:")
edad = 18
if edad >= 18:
    print(f"   ✅ {edad} >= 18 es True")
print()

print("<= MENOR O IGUAL:")
puntos = 50
if puntos <= 100:
    print(f"   ✅ {puntos} <= 100 es True")
print()

print("-" * 60)
print()


# ============================================
# 5️⃣ OPERADORES LÓGICOS (AND, OR, NOT)
# ============================================
print("=== 5. OPERADORES LÓGICOS ===")
print()

print("🔗 AND (Y) - Ambas deben ser verdad:")
edad = 16
tiene_permiso = True

if edad >= 15 and tiene_permiso:
    print(f"   Edad: {edad}, Permiso: {tiene_permiso}")
    print("   ✅ Puede salir (necesita edad Y permiso)")
print()

edad = 14
tiene_permiso = True

if edad >= 15 and tiene_permiso:
    print("   ✅ Puede salir")
else:
    print(f"   Edad: {edad}, Permiso: {tiene_permiso}")
    print("   ❌ NO puede salir (falta la edad)")
print()

print("🔗 OR (O) - Al menos una debe ser verdad:")
es_sabado = False
es_domingo = True

if es_sabado or es_domingo:
    print(f"   Sábado: {es_sabado}, Domingo: {es_domingo}")
    print("   ✅ Es fin de semana (al menos uno es True)")
print()

print("🔗 NOT (NO) - Invierte el valor:")
esta_lloviendo = False

if not esta_lloviendo:
    print(f"   Lloviendo: {esta_lloviendo}")
    print("   ✅ NO está lloviendo, puedo salir")
print()

print("🎯 EJEMPLO COMBINADO:")
edad = 10
tiene_dinero = True
tienda_abierta = True

if edad >= 10 and (tiene_dinero and tienda_abierta):
    print(
        f"   Edad: {edad}, Dinero: {tiene_dinero}, Tienda abierta: {tienda_abierta}")
    print("   ✅ Puede comprar dulces")
print()

print("-" * 60)
print()


# ============================================
# 6️⃣ CONDICIONALES ANIDADOS
# ============================================
print("=== 6. CONDICIONALES ANIDADOS (Uno dentro de otro) ===")
print()

print("🎯 EJEMPLO - Sistema de acceso:")
tiene_tarjeta = True
codigo_correcto = True

if tiene_tarjeta:
    print("   ✅ Tarjeta detectada")

    if codigo_correcto:
        print("   ✅ Código correcto")
        print("   🚪 ACCESO PERMITIDO")
    else:
        print("   ❌ Código incorrecto")
        print("   🚫 ACCESO DENEGADO")
else:
    print("   ❌ No tiene tarjeta")
    print("   🚫 ACCESO DENEGADO")

print()

print("🎯 EJEMPLO - Elegir actividad:")
dia = "Sábado"
hace_sol = True

if dia == "Sábado" or dia == "Domingo":
    print(f"   📅 Es {dia} (fin de semana)")

    if hace_sol:
        print("   ☀️ Hace sol")
        print("   🏖️ Vamos a la playa")
    else:
        print("   ☁️ Está nublado")
        print("   🎬 Vamos al cine")
else:
    print(f"   📅 Es {dia} (día de escuela)")
    print("   📚 A estudiar")

print()

print("-" * 60)
print()


# ============================================
# 7️⃣ OPERADOR TERNARIO (Condicional en una línea)
# ============================================
print("=== 7. OPERADOR TERNARIO (Atajo IF-ELSE) ===")
print()

# Forma normal
edad = 16
print("🔹 Forma normal:")
if edad >= 18:
    mensaje = "Mayor de edad"
else:
    mensaje = "Menor de edad"
print(f"   {mensaje}")
print()

# Forma ternaria (en una línea)
print("🔹 Forma ternaria (en 1 línea):")
edad = 16
mensaje = "Mayor de edad" if edad >= 18 else "Menor de edad"
print(f"   {mensaje}")
print()

# Más ejemplos
print("🔹 Más ejemplos:")
numero = 7
tipo = "PAR" if numero % 2 == 0 else "IMPAR"
print(f"   {numero} es {tipo}")

temperatura = 25
clima = "Calor" if temperatura > 25 else "Frío"
print(f"   {temperatura}°C → {clima}")
print()

print("-" * 60)
print()


# ============================================
# 8️⃣ IN - VERIFICAR SI ESTÁ EN UNA LISTA
# ============================================
print("=== 8. OPERADOR IN (Verificar pertenencia) ===")
print()

frutas = ["manzana", "pera", "uva", "naranja"]
print(f"🍎 Lista de frutas: {frutas}")
print()

fruta_buscar = "pera"
if fruta_buscar in frutas:
    print(f"   ✅ '{fruta_buscar}' SÍ está en la lista")

fruta_buscar = "kiwi"
if fruta_buscar in frutas:
    print(f"   ✅ '{fruta_buscar}' está en la lista")
else:
    print(f"   ❌ '{fruta_buscar}' NO está en la lista")

print()

print("🎯 EJEMPLO - Día laborable:")
dias_laborables = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
dia_hoy = "Sábado"

if dia_hoy in dias_laborables:
    print(f"   {dia_hoy} → 📚 Día de escuela")
else:
    print(f"   {dia_hoy} → 🎉 Día libre")

print()

print("-" * 60)
print()


# ============================================
# 🎯 EJEMPLOS PRÁCTICOS DIVERTIDOS
# ============================================
print("=== 🎯 EJEMPLOS PRÁCTICOS ===")
print()

# 🎮 Sistema de videojuego
print("🎮 SISTEMA DE NIVELES:")
puntos = 1500

if puntos >= 2000:
    nivel = "Maestro"
    recompensa = "Espada legendaria"
elif puntos >= 1000:
    nivel = "Experto"
    recompensa = "Armadura especial"
elif puntos >= 500:
    nivel = "Intermedio"
    recompensa = "Escudo mágico"
else:
    nivel = "Principiante"
    recompensa = "Espada básica"

print(f"   Puntos: {puntos}")
print(f"   Nivel: {nivel}")
print(f"   Recompensa: {recompensa}")
print()

# 🌡️ Termómetro
print("🌡️ RECOMENDACIÓN SEGÚN TEMPERATURA:")
temperatura = 18

if temperatura >= 30:
    print(f"   {temperatura}°C → 🔥 Hace mucho calor, quédate en casa con AC")
elif temperatura >= 25:
    print(f"   {temperatura}°C → ☀️ Clima cálido, usa ropa ligera")
elif temperatura >= 15:
    print(f"   {temperatura}°C → 😊 Clima agradable, perfecto para salir")
elif temperatura >= 5:
    print(f"   {temperatura}°C → 🧥 Hace frío, lleva chamarra")
else:
    print(f"   {temperatura}°C → ❄️ Hace mucho frío, abrígate bien")
print()

# 🎂 Descuento por edad
print("🎟️ DESCUENTO EN ENTRADA AL CINE:")
edad = 10
precio_base = 10

if edad < 5:
    descuento = 100  # Gratis
    precio_final = 0
    print(f"   Edad: {edad} años → 🎁 ¡GRATIS!")
elif edad < 12:
    descuento = 50
    precio_final = precio_base * (1 - descuento/100)
    print(f"   Edad: {edad} años → 50% descuento → ${precio_final}")
elif edad >= 60:
    descuento = 30
    precio_final = precio_base * (1 - descuento/100)
    print(f"   Edad: {edad} años → 30% descuento → ${precio_final}")
else:
    precio_final = precio_base
    print(f"   Edad: {edad} años → Precio normal → ${precio_final}")
print()

# 🚦 Semáforo
print("🚦 SEMÁFORO:")
color = "Verde"

if color == "Rojo":
    print(f"   {color} → 🛑 STOP - Detente")
elif color == "Amarillo":
    print(f"   {color} → ⚠️ PRECAUCIÓN - Reduce velocidad")
elif color == "Verde":
    print(f"   {color} → ✅ AVANZA - Puedes pasar")
else:
    print(f"   {color} → ❓ Color no válido")
print()

# 📱 Batería del teléfono
print("🔋 ESTADO DE BATERÍA:")
bateria = 25

if bateria >= 80:
    print(f"   Batería: {bateria}% → 🟢 Excelente")
elif bateria >= 50:
    print(f"   Batería: {bateria}% → 🟡 Bien")
elif bateria >= 20:
    print(f"   Batería: {bateria}% → 🟠 Baja, considera cargar")
else:
    print(f"   Batería: {bateria}% → 🔴 Crítica, ¡carga ahora!")
print()

# 🎯 Sistema de contraseñas
print("🔐 VALIDAR CONTRASEÑA:")
contraseña = "Python123"
longitud_minima = 8

if len(contraseña) < longitud_minima:
    print(f"   Contraseña: {contraseña}")
    print(f"   ❌ Muy corta (mínimo {longitud_minima} caracteres)")
elif contraseña.isalpha():  # Solo letras
    print(f"   Contraseña: {contraseña}")
    print(f"   ❌ Debe tener números")
elif contraseña.isdigit():  # Solo números
    print(f"   Contraseña: {contraseña}")
    print(f"   ❌ Debe tener letras")
else:
    print(f"   Contraseña: {contraseña}")
    print(f"   ✅ Contraseña válida")
print()

# 🏆 Medallas olímpicas
print("🏅 POSICIÓN EN LA CARRERA:")
posicion = 2

if posicion == 1:
    print(f"   Posición: {posicion} → 🥇 Medalla de ORO")
elif posicion == 2:
    print(f"   Posición: {posicion} → 🥈 Medalla de PLATA")
elif posicion == 3:
    print(f"   Posición: {posicion} → 🥉 Medalla de BRONCE")
elif posicion <= 10:
    print(f"   Posición: {posicion} → 👏 Buen trabajo")
else:
    print(f"   Posición: {posicion} → 💪 Sigue entrenando")
print()

# 🍕 Pizzería - Calcular precio
print("🍕 PIZZERÍA - CALCULADOR DE PRECIO:")
tamaño = "Mediana"
ingredientes_extra = 2
precio = 0

if tamaño == "Pequeña":
    precio = 8
elif tamaño == "Mediana":
    precio = 12
elif tamaño == "Grande":
    precio = 16
elif tamaño == "Familiar":
    precio = 20

precio_ingredientes = ingredientes_extra * 2
precio_total = precio + precio_ingredientes

print(f"   Tamaño: {tamaño} → ${precio}")
print(f"   Ingredientes extra: {ingredientes_extra} → ${precio_ingredientes}")
print(f"   Total: ${precio_total}")
print()

# 🎓 Sistema de becas
print("🎓 SISTEMA DE BECAS:")
promedio = 92
situacion_economica = "Baja"

if promedio >= 90 and situacion_economica == "Baja":
    print(f"   Promedio: {promedio}, Situación: {situacion_economica}")
    print(f"   ✅ BECA COMPLETA (100%)")
elif promedio >= 90:
    print(f"   Promedio: {promedio}, Situación: {situacion_economica}")
    print(f"   ✅ Beca por mérito (50%)")
elif situacion_economica == "Baja":
    print(f"   Promedio: {promedio}, Situación: {situacion_economica}")
    print(f"   ✅ Beca económica (30%)")
else:
    print(f"   Promedio: {promedio}, Situación: {situacion_economica}")
    print(f"   ❌ No califica para beca")
print()

# 🎪 Montaña rusa
print("🎢 REQUISITOS PARA MONTAÑA RUSA:")
altura = 145  # cm
edad = 12
acompañado = False

if altura >= 140 and edad >= 10:
    print(f"   Altura: {altura}cm, Edad: {edad} años")
    print(f"   ✅ Puedes subir solo")
elif altura >= 120 and acompañado:
    print(f"   Altura: {altura}cm, Acompañado: {acompañado}")
    print(f"   ✅ Puedes subir con un adulto")
else:
    print(f"   Altura: {altura}cm, Edad: {edad} años")
    print(f"   ❌ No cumples los requisitos")
print()

# 📅 Determinar estación del año
print("🌸 ESTACIÓN DEL AÑO (Hemisferio Sur):")
mes = "Enero"

if mes in ["Diciembre", "Enero", "Febrero"]:
    print(f"   {mes} → ☀️ Verano")
elif mes in ["Marzo", "Abril", "Mayo"]:
    print(f"   {mes} → 🍂 Otoño")
elif mes in ["Junio", "Julio", "Agosto"]:
    print(f"   {mes} → ❄️ Invierno")
elif mes in ["Septiembre", "Octubre", "Noviembre"]:
    print(f"   {mes} → 🌸 Primavera")
else:
    print(f"   {mes} → ❓ Mes no válido")
print()

# 💧 Sistema de riego automático
print("💧 SISTEMA DE RIEGO AUTOMÁTICO:")
humedad_tierra = 30  # porcentaje
temperatura = 28

if humedad_tierra < 20:
    print(f"   Humedad: {humedad_tierra}% → 💦 Riego INTENSO (tierra muy seca)")
elif humedad_tierra < 40 and temperatura > 25:
    print(
        f"   Humedad: {humedad_tierra}%, Temp: {temperatura}°C → 💧 Riego MODERADO")
elif humedad_tierra < 40:
    print(f"   Humedad: {humedad_tierra}% → 💧 Riego LIGERO")
else:
    print(f"   Humedad: {humedad_tierra}% → ✅ No necesita riego")
print()

print("=" * 60)
print("🎉 ¡Felicidades! Ya dominas los Condicionales en Python 🎉")
print("=" * 60)
print()
print("📌 RESUMEN:")
print("   - IF → Si se cumple la condición")
print("   - ELIF → Si no, prueba esta otra condición")
print("   - ELSE → Si ninguna se cumplió")
print("   - Comparaciones: ==, !=, >, <, >=, <=")
print("   - Lógicos: and (y), or (o), not (no)")
print("   - IN → Verificar si está en una lista")
print("   - Ternario → condición_true if condición else condición_false")
print("=" * 60)
