"""
PYTHON DESDE CERO - LECCIÓN 11: FUNCIONES
==========================================

🎯 ¿Qué son las FUNCIONES?
--------------------------
Una función es como una MÁQUINA o una RECETA que guardas para usarla después.

Imagina que tienes una máquina de hacer jugo:
1. Le pones frutas (ENTRADA)
2. La máquina procesa (HACE ALGO)
3. Te da jugo (SALIDA)

En programación:
- Creas una función UNA VEZ
- La puedes usar MUCHAS VECES
- Le puedes dar diferentes DATOS cada vez

Ejemplo en la vida real:
- Receta de galletas → Siempre los mismos pasos, diferentes ingredientes
- Calculadora → Siempre suma igual, diferentes números
- Tu nombre → Siempre te llaman igual

¿Por qué usar funciones?
- ✅ NO repetir código
- ✅ Organizar mejor tu programa
- ✅ Reutilizar código fácilmente
- ✅ Hacer tu código más fácil de leer

def = DEFINE (crear) una función
"""

import random
print("=" * 60)
print("🎓 LECCIÓN 11: FUNCIONES EN PYTHON")
print("=" * 60)
print()

# ============================================
# 1️⃣ FUNCIÓN SIMPLE (Sin parámetros, sin retorno)
# ============================================
print("=== 1. FUNCIÓN SIMPLE ===")
print()

# Definir la función


def saludar():
    """Esta función saluda"""
    print("   ¡Hola! ¿Cómo estás?")
    print("   ¡Bienvenido a Python!")


print("🎯 EJEMPLO 1 - Función que saluda:")
saludar()  # Llamar a la función
print()

print("🎯 EJEMPLO 2 - Llamar varias veces:")
saludar()
saludar()
print()


def despedirse():
    """Esta función se despide"""
    print("   👋 ¡Adiós!")
    print("   🌟 ¡Hasta pronto!")


print("🎯 EJEMPLO 3 - Otra función:")
despedirse()
print()

print("💡 ESTRUCTURA:")
print("   def nombre_funcion():")
print("       # código que hace algo")
print()

print("-" * 60)
print()


# ============================================
# 2️⃣ FUNCIONES CON PARÁMETROS
# ============================================
print("=== 2. FUNCIONES CON PARÁMETROS ===")
print()


def saludar_persona(nombre):
    """Saluda a una persona específica"""
    print(f"   ¡Hola {nombre}! ¿Cómo estás?")


print("🎯 EJEMPLO 1 - Función con 1 parámetro:")
saludar_persona("Ana")
saludar_persona("Luis")
saludar_persona("María")
print()


def sumar_numeros(a, b):
    """Suma dos números"""
    resultado = a + b
    print(f"   {a} + {b} = {resultado}")


print("🎯 EJEMPLO 2 - Función con 2 parámetros:")
sumar_numeros(5, 3)
sumar_numeros(10, 20)
sumar_numeros(100, 50)
print()


def presentarse(nombre, edad, ciudad):
    """Presentación completa"""
    print(f"   Me llamo {nombre}")
    print(f"   Tengo {edad} años")
    print(f"   Vivo en {ciudad}")


print("🎯 EJEMPLO 3 - Función con 3 parámetros:")
presentarse("Juan", 12, "Lima")
print()

print("-" * 60)
print()


# ============================================
# 3️⃣ FUNCIONES CON RETURN (Devolver valores)
# ============================================
print("=== 3. FUNCIONES CON RETURN ===")
print()


def sumar(a, b):
    """Suma dos números y devuelve el resultado"""
    return a + b


print("🎯 EJEMPLO 1 - Return básico:")
resultado = sumar(5, 3)
print(f"   5 + 3 = {resultado}")

total = sumar(10, 20)
print(f"   10 + 20 = {total}")
print()


def calcular_area_rectangulo(base, altura):
    """Calcula el área de un rectángulo"""
    area = base * altura
    return area


print("🎯 EJEMPLO 2 - Calcular área:")
mi_area = calcular_area_rectangulo(5, 3)
print(f"   Área del rectángulo (5×3): {mi_area}")
print()


def es_mayor_edad(edad):
    """Verifica si es mayor de edad"""
    if edad >= 18:
        return True
    else:
        return False


print("🎯 EJEMPLO 3 - Retornar booleano:")
print(f"   ¿Es mayor de edad (20)? {es_mayor_edad(20)}")
print(f"   ¿Es mayor de edad (15)? {es_mayor_edad(15)}")
print()

print("💡 RETURN:")
print("   - Devuelve un valor")
print("   - Termina la ejecución de la función")
print("   - Puedes guardar el resultado en una variable")
print()

print("-" * 60)
print()


# ============================================
# 4️⃣ PARÁMETROS CON VALORES POR DEFECTO
# ============================================
print("=== 4. PARÁMETROS CON VALORES POR DEFECTO ===")
print()


def saludar_idioma(nombre, idioma="español"):
    """Saluda en diferentes idiomas"""
    if idioma == "español":
        print(f"   ¡Hola {nombre}!")
    elif idioma == "inglés":
        print(f"   Hello {nombre}!")
    elif idioma == "francés":
        print(f"   Bonjour {nombre}!")


print("🎯 EJEMPLO - Con y sin valor por defecto:")
saludar_idioma("Ana")  # Usa el valor por defecto (español)
saludar_idioma("Luis", "inglés")  # Usa el valor especificado
saludar_idioma("Marie", "francés")
print()


def calcular_precio(precio_base, descuento=0):
    """Calcula precio con descuento opcional"""
    precio_final = precio_base - (precio_base * descuento / 100)
    return precio_final


print("🎯 EJEMPLO 2 - Descuento opcional:")
print(f"   Precio sin descuento: ${calcular_precio(100)}")
print(f"   Precio con 20% descuento: ${calcular_precio(100, 20)}")
print()

print("-" * 60)
print()


# ============================================
# 5️⃣ RETORNAR MÚLTIPLES VALORES
# ============================================
print("=== 5. RETORNAR MÚLTIPLES VALORES ===")
print()


def calcular_estadisticas(numeros):
    """Calcula min, max y promedio"""
    minimo = min(numeros)
    maximo = max(numeros)
    promedio = sum(numeros) / len(numeros)
    return minimo, maximo, promedio


print("🎯 EJEMPLO - Estadísticas:")
numeros = [10, 20, 30, 40, 50]
min_val, max_val, prom_val = calcular_estadisticas(numeros)
print(f"   Números: {numeros}")
print(f"   Mínimo: {min_val}")
print(f"   Máximo: {max_val}")
print(f"   Promedio: {prom_val}")
print()


def obtener_datos_persona():
    """Retorna múltiples datos"""
    return "Ana", 12, "Lima"


print("🎯 EJEMPLO 2 - Datos de persona:")
nombre, edad, ciudad = obtener_datos_persona()
print(f"   Nombre: {nombre}")
print(f"   Edad: {edad}")
print(f"   Ciudad: {ciudad}")
print()

print("-" * 60)
print()


# ============================================
# 6️⃣ ARGUMENTOS *args (múltiples argumentos)
# ============================================
print("=== 6. *args - MÚLTIPLES ARGUMENTOS ===")
print()


def sumar_todos(*numeros):
    """Suma cualquier cantidad de números"""
    total = 0
    for numero in numeros:
        total += numero
    return total


print("🎯 EJEMPLO - Sumar varios números:")
print(f"   sumar_todos(1, 2, 3) = {sumar_todos(1, 2, 3)}")
print(f"   sumar_todos(10, 20, 30, 40) = {sumar_todos(10, 20, 30, 40)}")
print(f"   sumar_todos(5, 10) = {sumar_todos(5, 10)}")
print()


def presentar_amigos(tu_nombre, *amigos):
    """Presenta a tus amigos"""
    print(f"   Hola, soy {tu_nombre}")
    print(f"   Mis amigos son:")
    for amigo in amigos:
        print(f"      - {amigo}")


print("🎯 EJEMPLO 2 - Lista de amigos:")
presentar_amigos("Juan", "Ana", "Luis", "María", "Pedro")
print()

print("-" * 60)
print()


# ============================================
# 7️⃣ ARGUMENTOS **kwargs (argumentos con nombre)
# ============================================
print("=== 7. **kwargs - ARGUMENTOS CON NOMBRE ===")
print()


def mostrar_datos(**datos):
    """Muestra datos con sus nombres"""
    for clave, valor in datos.items():
        print(f"   {clave}: {valor}")


print("🎯 EJEMPLO - Datos variados:")
mostrar_datos(nombre="Ana", edad=12, ciudad="Lima", hobby="leer")
print()


def crear_personaje(nombre, **atributos):
    """Crea un personaje con atributos"""
    print(f"   🎮 Personaje: {nombre}")
    print(f"   Atributos:")
    for atributo, valor in atributos.items():
        print(f"      {atributo}: {valor}")


print("🎯 EJEMPLO 2 - Personaje de juego:")
crear_personaje("Guerrero", vida=100, ataque=50, defensa=30, velocidad=20)
print()

print("-" * 60)
print()


# ============================================
# 8️⃣ FUNCIONES LAMBDA (Funciones cortas)
# ============================================
print("=== 8. FUNCIONES LAMBDA (Función en 1 línea) ===")
print()

# Función normal


def cuadrado(x):
    return x ** 2


# Función lambda (equivalente)
def cuadrado_lambda(x): return x ** 2


print("🎯 EJEMPLO 1 - Función normal vs Lambda:")
print(f"   Normal: cuadrado(5) = {cuadrado(5)}")
print(f"   Lambda: cuadrado_lambda(5) = {cuadrado_lambda(5)}")
print()

# Lambda con dos parámetros


def sumar_lambda(a, b): return a + b


print("🎯 EJEMPLO 2 - Lambda con 2 parámetros:")
print(f"   sumar_lambda(3, 7) = {sumar_lambda(3, 7)}")
print()

# Lambda en funciones como map
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x ** 2, numeros))
print("🎯 EJEMPLO 3 - Lambda con map:")
print(f"   Números: {numeros}")
print(f"   Cuadrados: {cuadrados}")
print()

print("-" * 60)
print()


# ============================================
# 9️⃣ SCOPE DE VARIABLES (Global vs Local)
# ============================================
print("=== 9. SCOPE - ALCANCE DE VARIABLES ===")
print()

# Variable global
mensaje_global = "Soy global"


def mostrar_scope():
    # Variable local
    mensaje_local = "Soy local"
    print(f"   Dentro de función - Global: {mensaje_global}")
    print(f"   Dentro de función - Local: {mensaje_local}")


print("🎯 EJEMPLO - Variables globales y locales:")
mostrar_scope()
print(f"   Fuera de función - Global: {mensaje_global}")
# print(mensaje_local)  # ❌ ERROR: no existe fuera de la función
print()

contador = 0


def incrementar():
    global contador  # Usar variable global
    contador += 1
    print(f"   Contador: {contador}")


print("🎯 EJEMPLO 2 - Modificar variable global:")
incrementar()
incrementar()
incrementar()
print()

print("-" * 60)
print()


# ============================================
# 🔟 DOCSTRINGS (Documentar funciones)
# ============================================
print("=== 10. DOCSTRINGS - DOCUMENTAR FUNCIONES ===")
print()


def calcular_imc(peso, altura):
    """
    Calcula el Índice de Masa Corporal (IMC)

    Parámetros:
        peso (float): Peso en kilogramos
        altura (float): Altura en metros

    Retorna:
        float: El IMC calculado
    """
    imc = peso / (altura ** 2)
    return imc


print("🎯 EJEMPLO - Función documentada:")
print(f"   IMC (70kg, 1.75m): {calcular_imc(70, 1.75):.2f}")
print()
print("   Documentación de la función:")
print(f"   {calcular_imc.__doc__}")

print("-" * 60)
print()


# ============================================
# 🎯 EJEMPLOS PRÁCTICOS DIVERTIDOS
# ============================================
print("=== 🎯 EJEMPLOS PRÁCTICOS ===")
print()

# 🎂 Función para calcular edad


def calcular_edad(año_nacimiento, año_actual=2026):
    """Calcula la edad de una persona"""
    edad = año_actual - año_nacimiento
    return edad


print("🎂 CALCULAR EDAD:")
edad_ana = calcular_edad(2010)
print(f"   Nacida en 2010 → {edad_ana} años")
edad_luis = calcular_edad(2008)
print(f"   Nacido en 2008 → {edad_luis} años")
print()

# 🌡️ Convertir temperatura


def celsius_a_fahrenheit(celsius):
    """Convierte Celsius a Fahrenheit"""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


def fahrenheit_a_celsius(fahrenheit):
    """Convierte Fahrenheit a Celsius"""
    celsius = (fahrenheit - 32) * 5/9
    return celsius


print("🌡️ CONVERTIR TEMPERATURA:")
temp_c = 25
temp_f = celsius_a_fahrenheit(temp_c)
print(f"   {temp_c}°C = {temp_f}°F")

temp_f2 = 77
temp_c2 = fahrenheit_a_celsius(temp_f2)
print(f"   {temp_f2}°F = {temp_c2:.1f}°C")
print()

# 📊 Calificación con letra


def obtener_letra_calificacion(nota):
    """Convierte nota numérica a letra"""
    if nota >= 90:
        return "A"
    elif nota >= 80:
        return "B"
    elif nota >= 70:
        return "C"
    elif nota >= 60:
        return "D"
    else:
        return "F"


print("📊 CALIFICACIONES:")
notas = [95, 85, 75, 65, 55]
for nota in notas:
    letra = obtener_letra_calificacion(nota)
    print(f"   Nota {nota} → Calificación {letra}")
print()

# 🎮 Sistema de niveles


def calcular_nivel(puntos):
    """Calcula el nivel según puntos"""
    if puntos >= 2000:
        return "Maestro", "🏆"
    elif puntos >= 1000:
        return "Experto", "⭐"
    elif puntos >= 500:
        return "Intermedio", "🎯"
    else:
        return "Principiante", "🌱"


print("🎮 NIVELES DE JUEGO:")
jugadores = [("Ana", 2500), ("Luis", 1200), ("María", 600), ("Pedro", 300)]
for nombre, puntos in jugadores:
    nivel, emoji = calcular_nivel(puntos)
    print(f"   {nombre} ({puntos} pts) → {nivel} {emoji}")
print()

# 💰 Calculadora de propina


def calcular_propina(cuenta, porcentaje=10):
    """Calcula la propina"""
    propina = cuenta * porcentaje / 100
    total = cuenta + propina
    return propina, total


print("💰 CALCULAR PROPINA:")
cuenta = 150
propina, total = calcular_propina(cuenta, 15)
print(f"   Cuenta: ${cuenta}")
print(f"   Propina (15%): ${propina}")
print(f"   Total: ${total}")
print()

# 🔐 Validar contraseña


def validar_contraseña(password):
    """Valida si una contraseña es segura"""
    if len(password) < 8:
        return False, "Muy corta (mínimo 8 caracteres)"
    if password.isalpha():
        return False, "Debe tener números"
    if password.isdigit():
        return False, "Debe tener letras"
    return True, "Contraseña segura"


print("🔐 VALIDAR CONTRASEÑAS:")
contraseñas = ["abc123", "password", "12345678", "Python2026"]
for pwd in contraseñas:
    valida, mensaje = validar_contraseña(pwd)
    estado = "✅" if valida else "❌"
    print(f"   {estado} '{pwd}': {mensaje}")
print()

# 🎲 Tirar dados


def tirar_dado():
    """Simula tirar un dado de 6 caras"""
    return random.randint(1, 6)


def tirar_multiples_dados(cantidad):
    """Tira múltiples dados"""
    resultados = []
    for i in range(cantidad):
        resultados.append(tirar_dado())
    return resultados


print("🎲 TIRAR DADOS:")
print(f"   Un dado: 🎲 {tirar_dado()}")
tres_dados = tirar_multiples_dados(3)
print(f"   Tres dados: {tres_dados} → Total: {sum(tres_dados)}")
print()

# 🎯 Verificar número primo


def es_primo(numero):
    """Verifica si un número es primo"""
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True


print("🎯 NÚMEROS PRIMOS:")
numeros_test = [2, 3, 4, 5, 10, 13, 17, 20]
for num in numeros_test:
    if es_primo(num):
        print(f"   {num} es primo ✅")
print()

# 📝 Contar palabras


def contar_palabras(texto):
    """Cuenta palabras en un texto"""
    palabras = texto.split()
    return len(palabras)


def contar_caracteres(texto):
    """Cuenta caracteres sin espacios"""
    return len(texto.replace(" ", ""))


print("📝 ANALIZAR TEXTO:")
frase = "Python es un lenguaje genial"
print(f"   Texto: '{frase}'")
print(f"   Palabras: {contar_palabras(frase)}")
print(f"   Caracteres: {contar_caracteres(frase)}")
print()

# 🎨 Generar código de color


def rgb_a_hex(r, g, b):
    """Convierte RGB a código hexadecimal"""
    return f"#{r:02x}{g:02x}{b:02x}"


print("🎨 RGB A HEXADECIMAL:")
print(f"   RGB(255, 0, 0) → {rgb_a_hex(255, 0, 0)} (Rojo)")
print(f"   RGB(0, 255, 0) → {rgb_a_hex(0, 255, 0)} (Verde)")
print(f"   RGB(0, 0, 255) → {rgb_a_hex(0, 0, 255)} (Azul)")
print()

# 🏆 Calcular promedio


def calcular_promedio(*notas):
    """Calcula el promedio de notas"""
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)


print("🏆 PROMEDIO DE CALIFICACIONES:")
print(f"   Promedio de 85, 90, 88: {calcular_promedio(85, 90, 88):.1f}")
print(
    f"   Promedio de 70, 80, 90, 95: {calcular_promedio(70, 80, 90, 95):.1f}")
print()

# 🎪 Factorial


def factorial(n):
    """Calcula el factorial de un número"""
    if n == 0 or n == 1:
        return 1
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado


print("🎪 FACTORIAL:")
for num in [3, 5, 7]:
    print(f"   {num}! = {factorial(num)}")
print()

# 🔄 Invertir cadena


def invertir_texto(texto):
    """Invierte un texto"""
    return texto[::-1]


print("🔄 INVERTIR TEXTO:")
palabras_invertir = ["Python", "Hola", "2026"]
for palabra in palabras_invertir:
    invertida = invertir_texto(palabra)
    print(f"   '{palabra}' → '{invertida}'")
print()

# 🎯 Encontrar máximo


def encontrar_maximo(*numeros):
    """Encuentra el número máximo"""
    if len(numeros) == 0:
        return None
    maximo = numeros[0]
    for num in numeros:
        if num > maximo:
            maximo = num
    return maximo


print("🎯 ENCONTRAR MÁXIMO:")
print(f"   Máximo de 5, 12, 8, 20, 3: {encontrar_maximo(5, 12, 8, 20, 3)}")
print()

# 💳 Formatear número de tarjeta


def formatear_tarjeta(numero):
    """Formatea número de tarjeta"""
    # Ocultar dígitos excepto los últimos 4
    visible = numero[-4:]
    oculto = "*" * (len(numero) - 4)
    return oculto + visible


print("💳 OCULTAR NÚMERO DE TARJETA:")
tarjeta = "1234567890123456"
print(f"   Original: {tarjeta}")
print(f"   Oculto: {formatear_tarjeta(tarjeta)}")
print()

# 🌟 Crear saludo personalizado


def crear_saludo(nombre, hora):
    """Crea un saludo según la hora"""
    if 5 <= hora < 12:
        return f"Buenos días, {nombre} ☀️"
    elif 12 <= hora < 19:
        return f"Buenas tardes, {nombre} 🌤️"
    else:
        return f"Buenas noches, {nombre} 🌙"


print("🌟 SALUDOS PERSONALIZADOS:")
print(f"   {crear_saludo('Ana', 8)}")
print(f"   {crear_saludo('Luis', 14)}")
print(f"   {crear_saludo('María', 20)}")
print()

# 🎮 Calcular XP necesario


def xp_para_siguiente_nivel(nivel_actual):
    """Calcula XP necesario para subir de nivel"""
    return nivel_actual * 100 + 500


print("🎮 XP PARA SUBIR DE NIVEL:")
for nivel in range(1, 6):
    xp_necesario = xp_para_siguiente_nivel(nivel)
    print(f"   Nivel {nivel} → {nivel + 1}: {xp_necesario} XP")
print()

# 📞 Formatear teléfono


def formatear_telefono(numero):
    """Formatea número telefónico"""
    # Asume formato: 123-456-7890
    return f"({numero[:3]}) {numero[3:6]}-{numero[6:]}"


print("📞 FORMATEAR TELÉFONO:")
telefono = "5551234567"
print(f"   Original: {telefono}")
print(f"   Formateado: {formatear_telefono(telefono)}")
print()

print("=" * 60)
print("🎉 ¡Felicidades! Ya dominas las Funciones en Python 🎉")
print("=" * 60)
print()
print("📌 RESUMEN:")
print("   - def nombre(): → Crear función sin parámetros")
print("   - def nombre(param): → Función con parámetros")
print("   - return → Devolver valor")
print("   - Parámetros por defecto: def func(x=10)")
print("   - *args → Múltiples argumentos posicionales")
print("   - **kwargs → Múltiples argumentos con nombre")
print("   - lambda → Función anónima en 1 línea")
print("   - Scope: global vs local")
print("   - Docstring: Documentar la función")
print()
print("💡 TIPS:")
print("   ✅ Usa nombres descriptivos")
print("   ✅ Una función = Una tarea")
print("   ✅ Documenta tus funciones")
print("   ✅ Reutiliza código con funciones")
print("=" * 60)
