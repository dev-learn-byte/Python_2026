"""
PYTHON DESDE CERO - LECCIÓN 4: CADENAS DE TEXTO (STRINGS)
==========================================================

📝 ¿Qué es una CADENA DE TEXTO (String)?
----------------------------------------
Una cadena es como un collar de letras. Cada letra es una cuenta del collar.
Por ejemplo: "Hola" es un collar con 4 cuentas: H-o-l-a

Las cadenas son para guardar PALABRAS, FRASES, o cualquier TEXTO.
"""

print("=" * 60)
print("🎓 LECCIÓN 4: CADENAS DE TEXTO EN PYTHON")
print("=" * 60)
print()

# ============================================
# 1️⃣ DECLARACIÓN DE CADENAS
# ============================================
print("=== 1. CÓMO CREAR CADENAS DE TEXTO ===")
print()

# Comillas dobles
nombre = "Fernando"
print('Con comillas dobles: "Fernando" →', nombre)

# Comillas simples
apellido = 'García'
print("Con comillas simples: 'García' →", apellido)

# ¿Cuándo usar cada una?
frase1 = "Me gusta el don't (don't tiene comilla simple dentro)"
frase2 = 'Ella dijo: "Hola" (tiene comillas dobles dentro)'
print("\n📌 Truco: Usa comillas dobles si tu texto tiene comillas simples")
print("   Ejemplo:", frase1)
print("📌 Usa comillas simples si tu texto tiene comillas dobles")
print("   Ejemplo:", frase2)

# Comillas triples (para textos largos de varias líneas)
poema = """
Había una vez
un niño muy feliz
que aprendía Python
y se divertía un montón
"""
print("\n📌 Comillas triples (''' o \"\"\") para textos largos:")
print(poema)

print("-" * 60)
print()


# ============================================
# 2️⃣ OPERACIONES BÁSICAS
# ============================================
print("=== 2. OPERACIONES BÁSICAS CON CADENAS ===")
print()

# CONCATENACIÓN (Juntar textos con +)
print("➕ CONCATENACIÓN (Juntar textos):")
nombre = "Juan"
apellido = "Pérez"
nombre_completo = nombre + " " + apellido
print("   nombre:", nombre)
print("   apellido:", apellido)
print("   nombre completo:", nombre_completo)
print()

# Concatenar con números (¡OJO! hay que convertirlos)
edad = 10
# mensaje = "Tengo " + edad + " años"  # ❌ ESTO DA ERROR
mensaje = "Tengo " + str(edad) + " años"  # ✅ Convertimos el número a texto
print("   Para unir texto con números, usa str():")
print("   Edad:", edad, "→", mensaje)
print()

# LONGITUD (len - cuántas letras tiene)
print("📏 LONGITUD (Contar cuántas letras tiene):")
palabra = "Dinosaurio"
cantidad_letras = len(palabra)
print("   La palabra '" + palabra + "' tiene", cantidad_letras, "letras")
print()

nombre_largo = "Constantinopla"
print("   '" + nombre_largo + "' tiene", len(nombre_largo), "letras")
print()

# REPETICIÓN (*)
print("🔁 REPETICIÓN (Repetir un texto):")
risa = "ja" * 5
print("   'ja' * 5 =", risa)
linea = "-" * 30
print("   '-' * 30 =", linea)
print()

print("-" * 60)
print()


# ============================================
# 3️⃣ SALTOS DE LÍNEA Y TABULACIONES
# ============================================
print("=== 3. CARACTERES ESPECIALES ===")
print()

# \n = Salto de línea (como presionar ENTER)
print("🔽 SALTO DE LÍNEA (\\n):")
print("Primera línea\nSegunda línea\nTercera línea")
print()

# \t = Tabulación (como presionar TAB)
print("➡️ TABULACIÓN (\\t):")
print("Nombre:\tJuan")
print("Edad:\t10 años")
print("Ciudad:\tLima")
print()

# Ejemplo: Lista de compras
print("📝 Ejemplo - Lista de compras:")
lista = "LISTA DE COMPRAS\n\n1.\tManzanas\n2.\tPan\n3.\tLeche\n4.\tHuevos"
print(lista)
print()

print("-" * 60)
print()


# ============================================
# 4️⃣ FORMATEO DE CADENAS
# ============================================
print("=== 4. FORMATEAR CADENAS (Insertar variables en texto) ===")
print()

nombre = "Ana"
edad = 12
altura = 1.50

# Método 1: Concatenación (ya lo vimos)
print("1️⃣ CONCATENACIÓN (+):")
mensaje1 = "Hola, soy " + nombre + " y tengo " + str(edad) + " años"
print("   ", mensaje1)
print()

# Método 2: Usando comas en print (más fácil)
print("2️⃣ USANDO COMAS:")
print("   Hola, soy", nombre, "y tengo", edad, "años")
print()

# Método 3: .format()
print("3️⃣ MÉTODO .format():")
mensaje2 = "Hola, soy {} y tengo {} años".format(nombre, edad)
print("   ", mensaje2)

mensaje3 = "Me llamo {}, tengo {} años y mido {} metros".format(
    nombre, edad, altura)
print("   ", mensaje3)
print()

# Método 4: F-strings (el MÁS MODERNO y FÁCIL) ⭐
print("4️⃣ F-STRINGS (El mejor método) ⭐:")
mensaje4 = f"Hola, soy {nombre} y tengo {edad} años"
print("   ", mensaje4)

mensaje5 = f"Me llamo {nombre}, tengo {edad} años y mido {altura} metros"
print("   ", mensaje5)

# Con f-strings puedes hacer operaciones directamente
print(f"   El próximo año tendré {edad + 1} años")
print(f"   La suma de 5 + 3 = {5 + 3}")
print()

print("-" * 60)
print()


# ============================================
# 5️⃣ SLICING (Cortar cadenas)
# ============================================
print("=== 5. SLICING - CORTAR Y EXTRAER PARTES DEL TEXTO ===")
print()

palabra = "PYTHON"
print("La palabra es:", palabra)
print()

# Los índices empiezan en 0
print("📍 ÍNDICES (posiciones):")
print("   P  Y  T  H  O  N")
print("   0  1  2  3  4  5")
print()

# Acceder a una letra específica
print("🔍 ACCEDER A UNA LETRA:")
print(f"   palabra[0] = {palabra[0]}  (primera letra)")
print(f"   palabra[1] = {palabra[1]}  (segunda letra)")
print(f"   palabra[5] = {palabra[5]}  (última letra)")
print(f"   palabra[-1] = {palabra[-1]}  (última letra, otra forma)")
print(f"   palabra[-2] = {palabra[-2]}  (penúltima letra)")
print()

# Extraer un rango (slicing)
print("✂️ EXTRAER UN PEDAZO:")
print(
    f"   palabra[0:3] = {palabra[0:3]}  (desde posición 0 hasta 3, sin incluir 3)")
print(f"   palabra[2:5] = {palabra[2:5]}  (desde posición 2 hasta 5)")
print(f"   palabra[:3] = {palabra[:3]}  (desde el inicio hasta 3)")
print(f"   palabra[3:] = {palabra[3:]}  (desde posición 3 hasta el final)")
print()

# Ejemplo práctico
frase = "Hola Mundo"
print("Ejemplo con:", frase)
print(f"   Primeras 4 letras: {frase[:4]}")
print(f"   Últimas 5 letras: {frase[5:]}")
print(f"   Solo 'Mundo': {frase[5:10]}")
print()

print("-" * 60)
print()


# ============================================
# 6️⃣ MÉTODOS ÚTILES PARA CADENAS
# ============================================
print("=== 6. MÉTODOS ÚTILES (Herramientas para manipular texto) ===")
print()

texto = "hola mundo desde python"
print("Texto original:", texto)
print()

# MAYÚSCULAS Y MINÚSCULAS
print("🔤 CAMBIAR ENTRE MAYÚSCULAS Y MINÚSCULAS:")
print(f"   .upper() → {texto.upper()}")
print(f"   .lower() → {texto.lower()}")
print(f"   .title() → {texto.title()} (Primera letra de cada palabra)")
print(f"   .capitalize() → {texto.capitalize()} (Solo primera letra)")
print()

# BUSCAR Y CONTAR
print("🔍 BUSCAR Y CONTAR:")
frase = "me gusta Python, Python es genial"
print("Frase:", frase)
print(f"   .count('Python') → {frase.count('Python')} (aparece 2 veces)")
print(f"   .find('genial') → {frase.find('genial')} (está en posición 26)")
print(f"   'Python' in frase → {'Python' in frase} (¿está la palabra Python?)")
print()

# REEMPLAZAR
print("🔄 REEMPLAZAR:")
print(f"   .replace('Python', 'Java') → {frase.replace('Python', 'Java')}")
print()

# DIVIDIR Y UNIR
print("✂️ DIVIDIR (split):")
frutas = "manzana,pera,uva,sandía"
lista_frutas = frutas.split(",")
print(f"   '{frutas}'.split(',') → {lista_frutas}")
print()

print("🔗 UNIR (join):")
palabras = ["Hola", "amigo", "mío"]
frase_unida = " ".join(palabras)
print(f"   ' '.join({palabras}) → '{frase_unida}'")
print()

# LIMPIAR ESPACIOS
print("🧹 LIMPIAR ESPACIOS:")
texto_sucio = "   Hola   Python   "
print(f"   Original: '{texto_sucio}'")
print(
    f"   .strip() → '{texto_sucio.strip()}' (quita espacios al inicio/final)")
print()

# VERIFICACIONES
print("✅ VERIFICAR TIPO DE CONTENIDO:")
numero_texto = "12345"
palabra_texto = "Hola"
print(f"   '{numero_texto}'.isnumeric() → {numero_texto.isnumeric()} (¿es número?)")
print(f"   '{palabra_texto}'.isnumeric() → {palabra_texto.isnumeric()}")
print(f"   '{palabra_texto}'.isalpha() → {palabra_texto.isalpha()} (¿solo letras?)")
print()

# COMIENZA Y TERMINA
print("🎯 COMIENZA / TERMINA CON:")
archivo = "foto.png"
print(f"   '{archivo}'.startswith('foto') → {archivo.startswith('foto')}")
print(f"   '{archivo}'.endswith('.png') → {archivo.endswith('.png')}")
print()

print("-" * 60)
print()


# ============================================
# 🎯 EJEMPLOS PRÁCTICOS DIVERTIDOS
# ============================================
print("=== 🎯 EJEMPLOS PRÁCTICOS ===")
print()

# 📧 Validar email
print("📧 VALIDAR EMAIL:")
email = "fernando@gmail.com"
tiene_arroba = "@" in email
termina_com = email.endswith(".com")
es_valido = tiene_arroba and termina_com
print(f"   Email: {email}")
print(f"   ¿Tiene @? {tiene_arroba}")
print(f"   ¿Termina en .com? {termina_com}")
print(f"   ¿Es válido? {es_valido}")
print()

# 🔐 Crear usuario
print("🔐 CREAR NOMBRE DE USUARIO:")
nombre_completo = "Fernando García López"
usuario = nombre_completo.lower().replace(" ", "_")
print(f"   Nombre: {nombre_completo}")
print(f"   Usuario: {usuario}")
print()

# 📊 Análisis de texto
print("📊 ANÁLISIS DE TEXTO:")
cuento = "Había una vez un dragón que amaba los libros. El dragón leía todos los días."
print(f"   Texto: {cuento}")
print(f"   Longitud: {len(cuento)} caracteres")
print(f"   Palabras 'dragón': {cuento.lower().count('dragón')}")
print(f"   Primera palabra: {cuento.split()[0]}")
print(f"   Última palabra: {cuento.split()[-1]}")
print()

# 🎨 Arte ASCII
print("🎨 CREAR ARTE CON TEXTO:")
feliz_año = """
╔═════════════════════════════════════╗
║                                     ║
║   🎉  FELIZ AÑO NUEVO 2026  🎉     ║
║                                     ║
║         ✨ 2️⃣0️⃣2️⃣6️⃣ ✨           ║
║                                     ║
║   🎆  Que tengas un gran año  🎇   ║
║                                     ║
╚═════════════════════════════════════╝
"""
print(feliz_año)

# 🎮 Menú de juego
print("🎮 MENÚ DE JUEGO:")
titulo = "SUPER ADVENTURE"
print("\n" + "=" * 30)
print(titulo.center(30))  # Centrar texto
print("=" * 30)
print("1. Nuevo Juego")
print("2. Continuar")
print("3. Opciones")
print("4. Salir")
print("=" * 30)
print()

# 🏷️ Etiqueta de precio
print("🏷️ ETIQUETA DE PRODUCTO:")
producto = "laptop"
precio = 599.99
descuento = 10
precio_final = precio - (precio * descuento / 100)

etiqueta = f"""
╔════════════════════════╗
║  {producto.upper().center(20)}  ║
║                        ║
║  Precio: ${precio:.2f}     ║
║  Descuento: {descuento}%        ║
║  TOTAL: ${precio_final:.2f}      ║
╚════════════════════════╝
"""
print(etiqueta)

print("=" * 60)
print("🎉 ¡Felicidades! Ya sabes trabajar con cadenas de texto 🎉")
print("=" * 60)
