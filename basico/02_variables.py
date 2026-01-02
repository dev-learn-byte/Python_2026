"""
PYTHON DESDE CERO - LECCIÓN 2: VARIABLES
=========================================

🎒 ¿Qué es una VARIABLE?
------------------------
Una variable es como una CAJA o MOCHILA donde guardas información.
Le pones un NOMBRE a la caja para saber qué hay dentro.

Ejemplo en la vida real:
- Tienes una caja con el nombre "edad" y dentro guardas el número 10
- Tienes una caja con el nombre "nombre" y dentro guardas "Juan"
"""

# ============================================
# 1️⃣ TEXTO (String - str)
# ============================================
print("=== 1. VARIABLES DE TEXTO ===")

# Guardar nombres
nombre = "Fernando"
apellido = "Castigo"
mascota = "Firulais"

print("Mi nombre es:", nombre)
print("Mi apellido es:", apellido)
print("Mi mascota se llama:", mascota)

# Podemos cambiar lo que hay en la caja
nombre = "María"
print("Ahora me llamo:", nombre)

# Unir textos
mensaje = "Hola, soy " + nombre + " y mi perro es " + mascota
print(mensaje)

print()  # Línea en blanco para separar


# ============================================
# 2️⃣ NÚMEROS ENTEROS (Integer - int)
# ============================================
print("=== 2. VARIABLES DE NÚMEROS ENTEROS ===")

# Sin decimales: 1, 2, 3, 100, -5
edad = 10
hermanos = 2
altura_cm = 145
puntos_juego = 9999

print("Tengo", edad, "años")
print("Tengo", hermanos, "hermanos")
print("Mido", altura_cm, "centímetros")
print("Mi puntaje es:", puntos_juego)

# Operaciones matemáticas
suma = 5 + 3
resta = 10 - 4
multiplicacion = 6 * 7
division_entera = 20 // 3  # Divide y quita los decimales

print("5 + 3 =", suma)
print("10 - 4 =", resta)
print("6 x 7 =", multiplicacion)
print("20 ÷ 3 =", division_entera)

print()


# ============================================
# 3️⃣ NÚMEROS DECIMALES (Float)
# ============================================
print("=== 3. VARIABLES DE NÚMEROS DECIMALES ===")

# Con punto decimal: 3.14, 2.5, 0.99
altura_metros = 1.45
precio = 9.99
temperatura = 36.5
promedio = 8.75

print("Mido", altura_metros, "metros")
print("El juguete cuesta $", precio)
print("Mi temperatura es", temperatura, "grados")
print("Mi promedio es", promedio)

# Operaciones con decimales
division_decimal = 10 / 3
print("10 ÷ 3 con decimales =", division_decimal)

print()


# ============================================
# 4️⃣ VERDADERO o FALSO (Boolean - bool)
# ============================================
print("=== 4. VARIABLES VERDADERO/FALSO ===")

# Solo pueden ser True (verdadero) o False (falso)
tengo_hambre = True
esta_lloviendo = False
se_jugar_futbol = True
tengo_dinero = False

print("¿Tengo hambre?", tengo_hambre)
print("¿Está lloviendo?", esta_lloviendo)
print("¿Sé jugar fútbol?", se_jugar_futbol)
print("¿Tengo dinero?", tengo_dinero)

# Comparaciones dan como resultado True o False
soy_mayor_edad = edad >= 18
print("¿Soy mayor de edad?", soy_mayor_edad)

es_barato = precio < 10
print("¿El juguete es barato (menos de $10)?", es_barato)

print()


# ============================================
# 5️⃣ VACÍO (None)
# ============================================
print("=== 5. VARIABLE VACÍA ===")

# None significa "no hay nada aquí"
apellido_mascota = None
print("El apellido de mi mascota es:", apellido_mascota)
print("(Los perros no tienen apellido, así que está vacío)")

print()


# ============================================
# 🎯 EJEMPLOS PRÁCTICOS
# ============================================
print("=== EJEMPLOS DIVERTIDOS ===")

# 🎂 Calculadora de edad en meses
años = 10
meses_totales = años * 12
print("Si tienes", años, "años, tienes", meses_totales, "meses de vida")

# 🍕 Repartir pizza
pizzas = 3
amigos = 4
porciones_cada_uno = (pizzas * 8) / amigos  # Cada pizza tiene 8 porciones
print("Si hay", pizzas, "pizzas y somos", amigos,
      "amigos, nos tocan", porciones_cada_uno, "porciones cada uno")

# 🎮 Sistema de puntos
puntos_nivel1 = 100
puntos_nivel2 = 250
puntos_nivel3 = 500
puntos_totales = puntos_nivel1 + puntos_nivel2 + puntos_nivel3
print("Puntos totales del juego:", puntos_totales)

# 🌡️ Convertir temperatura (Celsius a Fahrenheit)
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(celsius, "grados Celsius son", fahrenheit, "grados Fahrenheit")

print()


# ============================================
# 📚 REGLAS PARA NOMBRES DE VARIABLES
# ============================================
print("=== REGLAS IMPORTANTES ===")
print("✅ Puedes usar: letras, números, guion bajo _")
print("✅ Ejemplos válidos: nombre, edad_usuario, puntos2, mi_mascota_favorita")
print("❌ NO puedes empezar con números: 1nombre")
print("❌ NO uses espacios: mi nombre (usa mi_nombre)")
print("❌ NO uses acentos ni ñ en nombres de variables")
print("❌ NO uses palabras reservadas: print, if, for, etc.")

print()


# ============================================
# 🔍 VER EL TIPO DE DATO
# ============================================
print("=== ¿CÓMO SABER QUÉ TIPO ES? ===")
print("La función type() te dice qué tipo de dato es:")

print("tipo de 'Hola':", type("Hola"))
print("tipo de 42:", type(42))
print("tipo de 3.14:", type(3.14))
print("tipo de True:", type(True))
print("tipo de None:", type(None))

print()
print("🎉 ¡Felicidades! Ya sabes qué son las variables y los tipos de datos 🎉")
