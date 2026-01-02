"""
PYTHON DESDE CERO - LECCIÓN 8: DICCIONARIOS
============================================

📖 ¿Qué es un DICCIONARIO?
--------------------------
Un diccionario es como una AGENDA TELEFÓNICA o un DICCIONARIO de verdad.

En lugar de usar NÚMEROS para buscar (como en listas), 
usas PALABRAS o NOMBRES (llamados LLAVES/KEYS).

Ejemplo en la vida real:
- Agenda: "Juan" → 555-1234 (nombre → teléfono)
- Diccionario real: "casa" → "vivienda donde vive una familia"
- Calificaciones: "Ana" → 95, "Luis" → 88

Estructura: {LLAVE: VALOR, LLAVE: VALOR, ...}

Piensa en un CASILLERO:
- Cada casillero tiene un NÚMERO (llave)
- Dentro hay COSAS (valor)
- Para sacar algo, necesitas saber el número

Los diccionarios se escriben con LLAVES { } 
Cada elemento tiene: LLAVE: VALOR
"""

print("=" * 60)
print("🎓 LECCIÓN 8: DICCIONARIOS EN PYTHON")
print("=" * 60)
print()

# ============================================
# 1️⃣ CREAR DICCIONARIOS
# ============================================
print("=== 1. CÓMO CREAR DICCIONARIOS ===")
print()

# Diccionario de edades
edades = {"Ana": 12, "Luis": 10, "María": 13}
print("👥 Edades de estudiantes:", edades)
print()

# Diccionario de calificaciones
calificaciones = {"Matemáticas": 95, "Ciencias": 88, "Historia": 92}
print("📊 Calificaciones:", calificaciones)
print()

# Diccionario vacío
diccionario_vacio = {}
print("📭 Diccionario vacío:", diccionario_vacio)
print()

# Diccionario con diferentes tipos de valores
persona = {
    "nombre": "Juan",
    "edad": 12,
    "altura": 1.50,
    "estudiante": True
}
print("👤 Datos de persona:", persona)
print()

# Otro método: dict()
colores = dict(rojo="#FF0000", verde="#00FF00", azul="#0000FF")
print("🎨 Códigos de colores:", colores)
print()

print("-" * 60)
print()


# ============================================
# 2️⃣ ACCEDER A VALORES
# ============================================
print("=== 2. ACCEDER A VALORES DEL DICCIONARIO ===")
print()

estudiante = {
    "nombre": "Ana",
    "edad": 12,
    "grado": "7mo",
    "promedio": 92.5
}

print("📋 Datos del estudiante:", estudiante)
print()

# Acceder por llave
print("🔍 ACCEDER POR LLAVE:")
print(f"   estudiante['nombre'] = {estudiante['nombre']}")
print(f"   estudiante['edad'] = {estudiante['edad']}")
print(f"   estudiante['promedio'] = {estudiante['promedio']}")
print()

# Método .get() (más seguro)
print("🔍 MÉTODO .get() (No da error si no existe):")
nombre = estudiante.get('nombre')
print(f"   estudiante.get('nombre') = {nombre}")

# Si la llave no existe, devuelve None (o un valor por defecto)
apellido = estudiante.get('apellido')
print(f"   estudiante.get('apellido') = {apellido}")

apellido_default = estudiante.get('apellido', 'Sin apellido')
print(f"   estudiante.get('apellido', 'Sin apellido') = {apellido_default}")
print()

print("-" * 60)
print()


# ============================================
# 3️⃣ MODIFICAR Y AGREGAR
# ============================================
print("=== 3. MODIFICAR Y AGREGAR ELEMENTOS ===")
print()

videojuego = {
    "nombre": "Super Adventure",
    "puntos": 1000,
    "nivel": 5
}

print("🎮 Videojuego original:", videojuego)
print()

# Modificar un valor existente
print("✏️ MODIFICAR VALOR:")
videojuego["puntos"] = 1500
print("   videojuego['puntos'] = 1500")
print("   Resultado:", videojuego)
print()

# Agregar nuevo par llave-valor
print("➕ AGREGAR NUEVO ELEMENTO:")
videojuego["vidas"] = 3
print("   videojuego['vidas'] = 3")
print("   Resultado:", videojuego)
print()

# Actualizar múltiples valores
print("🔄 UPDATE (Agregar/modificar varios):")
videojuego.update({"nivel": 6, "monedas": 250})
print("   .update({'nivel': 6, 'monedas': 250})")
print("   Resultado:", videojuego)
print()

print("-" * 60)
print()


# ============================================
# 4️⃣ ELIMINAR ELEMENTOS
# ============================================
print("=== 4. ELIMINAR ELEMENTOS DEL DICCIONARIO ===")
print()

inventario = {
    "espada": 1,
    "escudo": 1,
    "poción": 5,
    "llave": 1,
    "mapa": 1
}

print("⚔️ Inventario original:", inventario)
print()

# del - Eliminar por llave
print("🗑️ DEL (Eliminar por llave):")
del inventario["mapa"]
print("   del inventario['mapa']")
print("   Resultado:", inventario)
print()

# pop() - Eliminar y devolver el valor
print("🎯 POP (Eliminar y devolver valor):")
pocion_cantidad = inventario.pop("poción")
print(f"   inventario.pop('poción') → Obtuve {pocion_cantidad} pociones")
print("   Resultado:", inventario)
print()

# popitem() - Eliminar el último par agregado
print("🎲 POPITEM (Eliminar el último):")
ultimo = inventario.popitem()
print(f"   inventario.popitem() → Eliminé {ultimo}")
print("   Resultado:", inventario)
print()

# clear() - Vaciar todo
print("🧹 CLEAR (Vaciar todo):")
temp = {"a": 1, "b": 2}
print(f"   Diccionario: {temp}")
temp.clear()
print(f"   .clear() → {temp}")
print()

print("-" * 60)
print()


# ============================================
# 5️⃣ MÉTODOS ÚTILES
# ============================================
print("=== 5. MÉTODOS ÚTILES DE DICCIONARIOS ===")
print()

contactos = {
    "Mamá": "555-0001",
    "Papá": "555-0002",
    "Juan": "555-0003",
    "María": "555-0004"
}

print("📱 Contactos:", contactos)
print()

# keys() - Obtener todas las llaves
print("🔑 KEYS (Obtener llaves):")
llaves = contactos.keys()
print(f"   contactos.keys() = {list(llaves)}")
print()

# values() - Obtener todos los valores
print("💎 VALUES (Obtener valores):")
valores = contactos.values()
print(f"   contactos.values() = {list(valores)}")
print()

# items() - Obtener pares (llave, valor)
print("📦 ITEMS (Obtener pares llave-valor):")
items = contactos.items()
print(f"   contactos.items() =")
for llave, valor in items:
    print(f"      {llave} → {valor}")
print()

# in - Verificar si existe una llave
print("✅ IN (Verificar si existe llave):")
print(f"   'Juan' in contactos → {'Juan' in contactos}")
print(f"   'Pedro' in contactos → {'Pedro' in contactos}")
print()

# len() - Cantidad de elementos
print(f"📏 LEN (Cantidad): len(contactos) = {len(contactos)}")
print()

print("-" * 60)
print()


# ============================================
# 6️⃣ RECORRER DICCIONARIOS
# ============================================
print("=== 6. RECORRER DICCIONARIOS ===")
print()

notas = {"Matemáticas": 95, "Ciencias": 88, "Historia": 92, "Arte": 90}
print("📚 Notas:", notas)
print()

# Recorrer solo las llaves
print("🔁 MÉTODO 1 - Solo llaves:")
for materia in notas:
    print(f"   Materia: {materia}")
print()

# Recorrer solo las llaves (explícito)
print("🔁 MÉTODO 2 - Solo llaves (.keys()):")
for materia in notas.keys():
    print(f"   {materia}")
print()

# Recorrer solo los valores
print("🔁 MÉTODO 3 - Solo valores (.values()):")
for nota in notas.values():
    print(f"   Nota: {nota}")
print()

# Recorrer llaves y valores
print("🔁 MÉTODO 4 - Llaves y valores (.items()):")
for materia, nota in notas.items():
    print(f"   {materia}: {nota} puntos")
print()

print("-" * 60)
print()


# ============================================
# 7️⃣ DICCIONARIOS ANIDADOS
# ============================================
print("=== 7. DICCIONARIOS ANIDADOS (Dentro de otros) ===")
print()

# Diccionario con diccionarios dentro
estudiantes = {
    "Ana": {
        "edad": 12,
        "grado": "7mo",
        "promedio": 92
    },
    "Luis": {
        "edad": 13,
        "grado": "8vo",
        "promedio": 88
    },
    "María": {
        "edad": 12,
        "grado": "7mo",
        "promedio": 95
    }
}

print("👥 Base de datos de estudiantes:")
print(estudiantes)
print()

# Acceder a datos anidados
print("🔍 ACCEDER A DATOS ANIDADOS:")
print(f"   Edad de Ana: {estudiantes['Ana']['edad']}")
print(f"   Grado de Luis: {estudiantes['Luis']['grado']}")
print(f"   Promedio de María: {estudiantes['María']['promedio']}")
print()

# Recorrer diccionario anidado
print("🔁 RECORRER DICCIONARIO ANIDADO:")
for nombre, datos in estudiantes.items():
    print(f"   {nombre}:")
    print(f"      Edad: {datos['edad']}")
    print(f"      Grado: {datos['grado']}")
    print(f"      Promedio: {datos['promedio']}")
    print()

print("-" * 60)
print()


# ============================================
# 8️⃣ DICCIONARIOS CON LISTAS
# ============================================
print("=== 8. DICCIONARIOS CON LISTAS ===")
print()

# Lista de materias por estudiante
materias_estudiante = {
    "Ana": ["Matemáticas", "Ciencias", "Historia"],
    "Luis": ["Matemáticas", "Arte", "Música"],
    "María": ["Ciencias", "Historia", "Deportes"]
}

print("📚 Materias por estudiante:", materias_estudiante)
print()

print("🔍 ACCEDER:")
print(f"   Materias de Ana: {materias_estudiante['Ana']}")
print(f"   Primera materia de Luis: {materias_estudiante['Luis'][0]}")
print()

# Agregar materia a un estudiante
print("➕ AGREGAR MATERIA:")
materias_estudiante["Ana"].append("Arte")
print(f"   Ana ahora tiene: {materias_estudiante['Ana']}")
print()

print("-" * 60)
print()


# ============================================
# 9️⃣ CONVERTIR ESTRUCTURAS
# ============================================
print("=== 9. CONVERTIR A/DESDE DICCIONARIOS ===")
print()

# Listas de tuplas a diccionario
print("📋 DE LISTA DE TUPLAS A DICCIONARIO:")
pares = [("nombre", "Juan"), ("edad", 12), ("ciudad", "Lima")]
diccionario = dict(pares)
print(f"   Lista: {pares}")
print(f"   Diccionario: {diccionario}")
print()

# Dos listas a diccionario con zip
print("🔗 DOS LISTAS A DICCIONARIO (con zip):")
nombres = ["Ana", "Luis", "María"]
edades = [12, 13, 12]
diccionario_zip = dict(zip(nombres, edades))
print(f"   Nombres: {nombres}")
print(f"   Edades: {edades}")
print(f"   Diccionario: {diccionario_zip}")
print()

print("-" * 60)
print()


# ============================================
# 🔟 DICCIONARIOS VS OTRAS ESTRUCTURAS
# ============================================
print("=== 10. CUÁNDO USAR DICCIONARIOS ===")
print()

print("📖 USA DICCIONARIOS cuando:")
print("   ✅ Necesitas buscar datos por NOMBRE/LLAVE")
print("   ✅ Tienes pares LLAVE-VALOR")
print("   ✅ Datos de una persona, objeto, configuración")
print("   ✅ Contar frecuencias")
print("   ✅ Cachear/guardar resultados con identificadores")
print()

print("📝 USA LISTAS cuando:")
print("   ✅ Necesitas ORDEN específico")
print("   ✅ Accedes por POSICIÓN numérica")
print("   ✅ Secuencias simples de datos")
print()

print("-" * 60)
print()


# ============================================
# 🎯 EJEMPLOS PRÁCTICOS DIVERTIDOS
# ============================================
print("=== 🎯 EJEMPLOS PRÁCTICOS ===")
print()

# 📱 Agenda telefónica
print("📱 AGENDA TELEFÓNICA:")
agenda = {
    "Mamá": "555-0001",
    "Papá": "555-0002",
    "Mejor Amigo": "555-1234",
    "Emergencias": "911"
}
print("   Agenda completa:")
for contacto, telefono in agenda.items():
    print(f"      {contacto}: {telefono}")

print(f"\n   Llamar a Mamá: {agenda['Mamá']}")
print()

# 🎮 Estadísticas de jugador
print("🎮 PERFIL DE JUGADOR:")
jugador = {
    "usuario": "ProGamer123",
    "nivel": 45,
    "puntos": 12500,
    "victorias": 89,
    "derrotas": 34,
    "oro": 5600
}

print(f"   Usuario: {jugador['usuario']}")
print(f"   Nivel: {jugador['nivel']}")
print(f"   Puntos: {jugador['puntos']}")
print(f"   Récord: {jugador['victorias']}V - {jugador['derrotas']}D")
print(f"   Ratio: {jugador['victorias']/jugador['derrotas']:.2f}")
print()

# 🛒 Carrito de compras
print("🛒 CARRITO DE COMPRAS:")
carrito = {
    "Laptop": 599.99,
    "Mouse": 29.99,
    "Teclado": 79.99,
    "Monitor": 199.99
}

print("   Productos en el carrito:")
total = 0
for producto, precio in carrito.items():
    print(f"      {producto}: ${precio}")
    total += precio

print(f"   Total a pagar: ${total:.2f}")
print()

# 📊 Inventario de tienda
print("📦 INVENTARIO DE TIENDA:")
inventario = {
    "Manzanas": 50,
    "Peras": 30,
    "Naranjas": 45,
    "Plátanos": 60
}

print("   Stock disponible:")
for producto, cantidad in inventario.items():
    print(f"      {producto}: {cantidad} unidades")

# Vender productos
print("\n   Vendí 10 manzanas...")
inventario["Manzanas"] -= 10
print(f"   Manzanas ahora: {inventario['Manzanas']}")
print()

# 🎓 Sistema de calificaciones
print("🎓 SISTEMA DE CALIFICACIONES:")
calificaciones_clase = {
    "Ana": [95, 88, 92, 90],
    "Luis": [85, 82, 88, 86],
    "María": [92, 95, 90, 93]
}

print("   Promedios de estudiantes:")
for estudiante, notas in calificaciones_clase.items():
    promedio = sum(notas) / len(notas)
    print(f"      {estudiante}: {promedio:.1f}")
print()

# 🗳️ Contador de votos
print("🗳️ VOTACIÓN - SABOR DE HELADO FAVORITO:")
votos = {
    "Chocolate": 0,
    "Vainilla": 0,
    "Fresa": 0,
    "Menta": 0
}

# Simulando votos
votos_lista = ["Chocolate", "Chocolate", "Vainilla", "Fresa",
               "Chocolate", "Menta", "Chocolate", "Vainilla"]

for voto in votos_lista:
    votos[voto] += 1

print("   Resultados:")
for sabor, cantidad in votos.items():
    print(f"      {sabor}: {cantidad} votos")

# Encontrar el ganador
ganador = max(votos, key=votos.get)
print(f"   🏆 Ganador: {ganador} con {votos[ganador]} votos")
print()

# 🌡️ Temperaturas de la semana
print("🌡️ TEMPERATURAS DE LA SEMANA:")
temperaturas = {
    "Lunes": 22,
    "Martes": 24,
    "Miércoles": 23,
    "Jueves": 25,
    "Viernes": 26,
    "Sábado": 28,
    "Domingo": 27
}

print("   Registro semanal:")
for dia, temp in temperaturas.items():
    print(f"      {dia}: {temp}°C")

temp_promedio = sum(temperaturas.values()) / len(temperaturas)
temp_max = max(temperaturas.values())
temp_min = min(temperaturas.values())

print(f"\n   Promedio: {temp_promedio:.1f}°C")
print(f"   Máxima: {temp_max}°C")
print(f"   Mínima: {temp_min}°C")
print()

# 📖 Traductor simple
print("📖 MINI TRADUCTOR ESPAÑOL-INGLÉS:")
traductor = {
    "hola": "hello",
    "adiós": "goodbye",
    "gracias": "thank you",
    "casa": "house",
    "perro": "dog",
    "gato": "cat"
}

palabra = "perro"
print(f"   '{palabra}' en inglés: {traductor[palabra]}")

palabra2 = "gato"
print(f"   '{palabra2}' en inglés: {traductor[palabra2]}")
print()

# 🎵 Playlist de música
print("🎵 MI PLAYLIST:")
playlist = {
    1: {"titulo": "Canción 1", "artista": "Artista A", "duración": "3:45"},
    2: {"titulo": "Canción 2", "artista": "Artista B", "duración": "4:20"},
    3: {"titulo": "Canción 3", "artista": "Artista C", "duración": "3:30"}
}

print("   Lista de reproducción:")
for numero, cancion in playlist.items():
    print(
        f"      {numero}. {cancion['titulo']} - {cancion['artista']} ({cancion['duración']})")
print()

# 🏅 Tabla de posiciones
print("🏅 TABLA DE POSICIONES:")
equipos = {
    "Equipo A": {"puntos": 45, "victorias": 14, "derrotas": 3},
    "Equipo B": {"puntos": 42, "victorias": 13, "derrotas": 4},
    "Equipo C": {"puntos": 40, "victorias": 12, "derrotas": 5}
}

print("   Posiciones:")
for equipo, stats in equipos.items():
    print(
        f"      {equipo}: {stats['puntos']} pts ({stats['victorias']}V-{stats['derrotas']}D)")
print()

# 🍕 Menú de restaurante
print("🍕 MENÚ DEL RESTAURANTE:")
menu = {
    "Pizza Margarita": 12.99,
    "Pizza Pepperoni": 14.99,
    "Ensalada César": 8.99,
    "Pasta Alfredo": 13.99,
    "Refresco": 2.99
}

print("   Nuestro menú:")
for plato, precio in menu.items():
    print(f"      {plato}: ${precio}")

# Hacer un pedido
print("\n   Mi pedido:")
pedido = ["Pizza Pepperoni", "Refresco"]
total_pedido = sum(menu[item] for item in pedido)

for item in pedido:
    print(f"      - {item}: ${menu[item]}")
print(f"   Total: ${total_pedido:.2f}")
print()

# 💰 Conversor de monedas
print("💰 CONVERSOR DE MONEDAS:")
tasas_cambio = {
    "USD": 1.0,
    "EUR": 0.85,
    "GBP": 0.73,
    "JPY": 110.0,
    "PEN": 3.70  # Soles peruanos
}

cantidad_usd = 100
print(f"   ${cantidad_usd} USD equivale a:")
for moneda, tasa in tasas_cambio.items():
    if moneda != "USD":
        conversion = cantidad_usd * tasa
        print(f"      {conversion:.2f} {moneda}")
print()

# 🎯 Configuración de un juego
print("⚙️ CONFIGURACIÓN DEL JUEGO:")
config = {
    "volumen": 80,
    "dificultad": "Normal",
    "idioma": "Español",
    "graficos": "Alto",
    "controles": {
        "saltar": "Espacio",
        "disparar": "Click",
        "moverse": "WASD"
    }
}

print("   Configuración actual:")
print(f"      Volumen: {config['volumen']}%")
print(f"      Dificultad: {config['dificultad']}")
print(f"      Idioma: {config['idioma']}")
print(f"      Gráficos: {config['graficos']}")
print("      Controles:")
for accion, tecla in config['controles'].items():
    print(f"         {accion.capitalize()}: {tecla}")
print()

print("=" * 60)
print("🎉 ¡Felicidades! Ya dominas los Diccionarios en Python 🎉")
print("=" * 60)
print()
print("📌 RESUMEN:")
print("   - Diccionarios = Pares LLAVE: VALOR")
print("   - Se crean con llaves: {'nombre': 'Juan', 'edad': 12}")
print("   - Acceder: diccionario['llave']")
print("   - Métodos: .keys(), .values(), .items()")
print("   - Perfectos para buscar datos por nombre")
print("   - Muy rápidos para encontrar valores")
print("=" * 60)
