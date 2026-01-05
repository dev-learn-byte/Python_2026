"""
PYTHON PROFUNDO - SCOPE DE VARIABLES (Alcance de Variables)
============================================================

🏠 ¿Qué es el SCOPE (Alcance)?
------------------------------
El SCOPE es como decidir DÓNDE puede vivir una variable.

METÁFORA: La Casa y sus Habitaciones 🏠
--------------------------------------
Imagina tu casa con diferentes habitaciones:

🏠 CASA (Programa completo)
   📺 Sala = Variables GLOBALES (todos las pueden ver)
   🛏️ Tu habitación = Variables LOCALES (solo tú las ves)
   🚪 Baño = Variables LOCALES (solo quien está adentro)

Ejemplo en la vida real:
- Tu NOMBRE en tu casa → Todos saben cómo te llamas (GLOBAL)
- Tu DIARIO en tu cuarto → Solo tú lo lees (LOCAL)
- Los JUGUETES en la sala → Todos juegan con ellos (GLOBAL)
- Tu ROPA en tu clóset → Solo en tu cuarto (LOCAL)

En Python hay diferentes "niveles" de scope:
1. LOCAL → Dentro de una función
2. ENCLOSING → En funciones anidadas (una dentro de otra)
3. GLOBAL → En todo el programa
4. BUILT-IN → Variables predefinidas de Python
"""

print("=" * 70)
print("🎓 SCOPE DE VARIABLES EN PYTHON")
print("=" * 70)
print()

# ============================================
# 1️⃣ SCOPE LOCAL (Variables en funciones)
# ============================================
print("=== 1. SCOPE LOCAL - VARIABLES EN FUNCIONES ===")
print()

print("🏠 METÁFORA: Variable en tu habitación")
print("   Solo existe DENTRO de tu habitación")
print()


def mi_funcion():
    # Variable LOCAL - solo existe dentro de la función
    mensaje = "Soy una variable LOCAL"
    print(f"   Dentro de la función: {mensaje}")


print("🎯 EJEMPLO 1 - Variable local:")
mi_funcion()
# print(mensaje)  # ❌ ERROR! mensaje no existe fuera de la función
print("   (Si intentas usar 'mensaje' aquí, da ERROR)")
print()


def hacer_suma():
    # Variables locales
    a = 5
    b = 3
    resultado = a + b
    print(f"   Dentro de la función: {a} + {b} = {resultado}")
    return resultado


print("🎯 EJEMPLO 2 - Varias variables locales:")
total = hacer_suma()
print(f"   Fuera de la función: total = {total}")
print(a)  # ❌ ERROR! 'a' no existe fuera
print()

print("💡 REGLA:")
print("   - Variables creadas DENTRO de una función son LOCALES")
print("   - Solo existen DENTRO de esa función")
print("   - Se DESTRUYEN cuando la función termina")
print()

print("-" * 70)
print()


# ============================================
# 2️⃣ SCOPE GLOBAL (Variables fuera de funciones)
# ============================================
print("=== 2. SCOPE GLOBAL - VARIABLES FUERA DE FUNCIONES ===")
print()

print("🏠 METÁFORA: Variable en la sala de tu casa")
print("   Todos en la casa pueden verla y usarla")
print()

# Variable GLOBAL - existe en todo el programa
nombre_global = "Python"


def mostrar_nombre():
    # Puede LEER la variable global
    print(f"   Dentro de la función: {nombre_global}")


print("🎯 EJEMPLO 1 - Leer variable global:")
print(f"   Fuera de la función: {nombre_global}")
mostrar_nombre()
print()

# Múltiples variables globales
edad = 10
ciudad = "Lima"


def mostrar_info():
    print(f"   Edad: {edad}")
    print(f"   Ciudad: {ciudad}")


print("🎯 EJEMPLO 2 - Leer varias variables globales:")
mostrar_info()
print()

print("💡 REGLA:")
print("   - Variables creadas FUERA de funciones son GLOBALES")
print("   - Se pueden LEER desde cualquier lugar")
print("   - Existen durante TODO el programa")
print()

print("-" * 70)
print()


# ============================================
# 3️⃣ GLOBAL vs LOCAL con el mismo nombre
# ============================================
print("=== 3. ¿QUÉ PASA SI HAY DOS VARIABLES CON EL MISMO NOMBRE? ===")
print()

print("🏠 METÁFORA: Dos juguetes con el mismo nombre")
print("   - Un 'carro' en tu habitación")
print("   - Un 'carro' en la sala")
print("   Son DIFERENTES objetos")
print()

# Variable global
color = "Rojo"


def cambiar_color():
    # Esta es una variable LOCAL diferente
    color = "Azul"
    print(f"   Dentro de la función: color = {color}")


print("🎯 EJEMPLO - Variables con el mismo nombre:")
print(f"   Antes de llamar la función: color = {color}")
cambiar_color()
print(f"   Después de llamar la función: color = {color}")
print("   (La global NO cambió)")
print()

print("💡 REGLA:")
print("   - Python primero busca en el scope LOCAL")
print("   - Si no la encuentra, busca en el GLOBAL")
print("   - Una variable local OCULTA a la global del mismo nombre")
print()

print("-" * 70)
print()


# ============================================
# 4️⃣ PALABRA CLAVE 'global' (Modificar globales)
# ============================================
print("=== 4. PALABRA CLAVE 'global' - MODIFICAR VARIABLES GLOBALES ===")
print()

print("🏠 METÁFORA: Permiso para modificar algo de la sala")
print("   Necesitas permiso especial para cambiar cosas de la sala")
print()

contador = 0  # Variable global


def incrementar_mal():
    # Esto NO modifica la global, crea una local
    contador = contador + 1  # ❌ ERROR!


def incrementar_bien():
    # Con 'global' podemos modificar la variable global
    global contador
    contador = contador + 1
    print(f"   Contador incrementado: {contador}")


print("🎯 EJEMPLO - Usar 'global' para modificar:")
print(f"   Contador inicial: {contador}")
incrementar_bien()
incrementar_bien()
incrementar_bien()
print(f"   Contador final: {contador}")
print()

# Otro ejemplo
puntos = 0


def ganar_puntos(cantidad):
    global puntos
    puntos += cantidad
    print(f"   🎮 Ganaste {cantidad} puntos!")


def perder_puntos(cantidad):
    global puntos
    puntos -= cantidad
    print(f"   ❌ Perdiste {cantidad} puntos")


print("🎯 EJEMPLO 2 - Sistema de puntos:")
print(f"   Puntos iniciales: {puntos}")
ganar_puntos(50)
ganar_puntos(30)
perder_puntos(20)
print(f"   Puntos finales: {puntos}")
print()

print("💡 REGLA:")
print("   - Sin 'global': Solo puedes LEER variables globales")
print("   - Con 'global': Puedes MODIFICAR variables globales")
print("   - Usa: global nombre_variable")
print()

print("-" * 70)
print()


# ============================================
# 5️⃣ FUNCIONES ANIDADAS (Una dentro de otra)
# ============================================
print("=== 5. FUNCIONES ANIDADAS - UNA DENTRO DE OTRA ===")
print()

print("🏠 METÁFORA: Casas dentro de casas (muñecas rusas)")
print("   - Casa grande → Función externa")
print("   - Casa pequeña dentro → Función interna")
print()


def funcion_externa():
    mensaje_externo = "Soy de la función externa"

    def funcion_interna():
        mensaje_interno = "Soy de la función interna"
        # Puedo ver mensaje_externo
        print(f"      Interna ve: {mensaje_externo}")
        print(f"      Interna tiene: {mensaje_interno}")

    print(f"   Externa tiene: {mensaje_externo}")
    funcion_interna()
    # print(mensaje_interno)  # ❌ ERROR! No puede ver la de la interna


print("🎯 EJEMPLO 1 - Funciones anidadas:")
funcion_externa()
print()


def contador_clicks():
    clicks = 0

    def hacer_click():
        nonlocal clicks  # Para modificar variable de función externa
        clicks += 1
        print(f"      Click #{clicks}")

    print("   Haciendo clicks:")
    hacer_click()
    hacer_click()
    hacer_click()
    print(f"   Total de clicks: {clicks}")


print("🎯 EJEMPLO 2 - Usar 'nonlocal':")
contador_clicks()
print()

print("💡 REGLA:")
print("   - Función interna puede VER variables de la externa")
print("   - Función externa NO puede ver variables de la interna")
print("   - Usa 'nonlocal' para modificar variables de la externa")
print()

print("-" * 70)
print()


# ============================================
# 6️⃣ REGLA LEGB (Orden de búsqueda)
# ============================================
print("=== 6. REGLA LEGB - ORDEN DE BÚSQUEDA ===")
print()

print("🔍 Python busca variables en este ORDEN:")
print("   L → LOCAL (función actual)")
print("   E → ENCLOSING (función que contiene)")
print("   G → GLOBAL (módulo)")
print("   B → BUILT-IN (Python predefinidos)")
print()

x = "Global X"  # Global


def externa():
    x = "Enclosing X"  # Enclosing

    def interna():
        x = "Local X"  # Local
        print(f"      Interna ve: {x}")  # Usa Local

    interna()
    print(f"   Externa ve: {x}")  # Usa Enclosing


print("🎯 EJEMPLO - LEGB en acción:")
print(f"   Global tiene: {x}")
externa()
print()

# Sin variable local


def funcion_sin_local():
    # No hay 'y' local, busca en global
    print(f"   Función ve: {y}")


y = "Global Y"
print("🎯 EJEMPLO 2 - Sin variable local:")
funcion_sin_local()
print()

print("-" * 70)
print()


# ============================================
# 🎯 EJEMPLOS PRÁCTICOS Y DETALLADOS
# ============================================
print("=== 🎯 EJEMPLOS PRÁCTICOS DETALLADOS ===")
print()

# 🎮 Juego con puntuación global
print("🎮 EJEMPLO 1 - SISTEMA DE JUEGO:")
print()

puntaje = 0
nivel = 1
vidas = 3


def iniciar_juego():
    global puntaje, nivel, vidas
    puntaje = 0
    nivel = 1
    vidas = 3
    print("   🎮 Juego iniciado")
    print(f"   Puntos: {puntaje} | Nivel: {nivel} | Vidas: {vidas}")


def derrotar_enemigo():
    global puntaje
    puntos_ganados = 100 * nivel
    puntaje += puntos_ganados
    print(f"   ⚔️ Enemigo derrotado! +{puntos_ganados} puntos")


def subir_nivel():
    global nivel, puntaje
    nivel += 1
    puntaje += 500
    print(f"   🎉 Nivel {nivel} alcanzado! Bonus: +500 puntos")


def perder_vida():
    global vidas
    vidas -= 1
    print(f"   💔 Perdiste una vida. Vidas restantes: {vidas}")


def mostrar_estado():
    print(f"   📊 Puntos: {puntaje} | Nivel: {nivel} | Vidas: {vidas}")


iniciar_juego()
derrotar_enemigo()
derrotar_enemigo()
subir_nivel()
derrotar_enemigo()
perder_vida()
mostrar_estado()
print()

# 🏪 Tienda con inventario
print("🏪 EJEMPLO 2 - TIENDA CON INVENTARIO:")
print()

inventario = {"manzanas": 10, "peras": 5, "naranjas": 8}
dinero = 100


def comprar(producto, cantidad):
    global inventario, dinero
    precio_unitario = 5
    costo_total = precio_unitario * cantidad

    if dinero >= costo_total:
        dinero -= costo_total
        if producto in inventario:
            inventario[producto] += cantidad
        else:
            inventario[producto] = cantidad
        print(f"   ✅ Compraste {cantidad} {producto} por ${costo_total}")
        print(f"   💰 Dinero restante: ${dinero}")
    else:
        print(f"   ❌ No tienes suficiente dinero")


def vender(producto, cantidad):
    global inventario, dinero
    precio_venta = 7

    if producto in inventario and inventario[producto] >= cantidad:
        inventario[producto] -= cantidad
        ganancia = precio_venta * cantidad
        dinero += ganancia
        print(f"   💰 Vendiste {cantidad} {producto} por ${ganancia}")
        print(f"   💵 Dinero actual: ${dinero}")
    else:
        print(f"   ❌ No tienes suficiente {producto}")


def mostrar_inventario():
    print(f"   📦 Inventario actual:")
    for producto, cantidad in inventario.items():
        print(f"      {producto}: {cantidad}")
    print(f"   💵 Dinero: ${dinero}")


mostrar_inventario()
comprar("manzanas", 5)
vender("peras", 3)
mostrar_inventario()
print()

# 🎯 Contador con scope local
print("🎯 EJEMPLO 3 - CONTADOR LOCAL vs GLOBAL:")
print()


def ejemplo_scope_confuso():
    """Demuestra la diferencia entre local y global"""
    numero = 10  # Global

    def sumar_local():
        # Esta 'numero' es LOCAL y diferente
        numero = 5
        resultado = numero + 3
        print(f"      Local: numero = {numero}, resultado = {resultado}")

    def sumar_con_global():
        # Esta usa la 'numero' de la función externa
        resultado = numero + 3
        print(
            f"      Usando externa: numero = {numero}, resultado = {resultado}")

    def modificar_con_nonlocal():
        nonlocal numero
        numero += 5
        print(f"      Modificó externa: numero ahora es {numero}")

    print(f"   Número inicial: {numero}")
    sumar_local()
    print(f"   Después de sumar_local: {numero} (no cambió)")
    sumar_con_global()
    modificar_con_nonlocal()
    print(f"   Después de nonlocal: {numero} (cambió)")


ejemplo_scope_confuso()
print()

# 🔢 Generador de IDs
print("🔢 EJEMPLO 4 - GENERADOR DE IDs:")
print()


def crear_generador_id():
    """Función que genera IDs únicos"""
    id_actual = 0

    def generar_id():
        nonlocal id_actual
        id_actual += 1
        return f"ID-{id_actual:04d}"

    return generar_id


# Crear generador
generador = crear_generador_id()

print("   Generando IDs:")
for i in range(5):
    nuevo_id = generador()
    print(f"      Usuario {i+1}: {nuevo_id}")
print()

# 📊 Variables en bucles
print("📊 EJEMPLO 5 - SCOPE EN BUCLES:")
print()

total = 0  # Global


def sumar_numeros():
    global total
    numeros = [10, 20, 30, 40, 50]

    for num in numeros:
        # 'num' existe solo dentro del for
        total += num
        print(f"      Sumando {num} → Total: {total}")


print("   Suma acumulativa:")
sumar_numeros()
print(f"   Total final: {total}")
# print(num)  # ❌ ERROR! 'num' no existe fuera del for
print()

# 🎨 Clase con scope
print("🎨 EJEMPLO 6 - SCOPE EN CLASES:")
print()


class Contador:
    """Ejemplo de scope en clases"""
    contador_clase = 0  # Variable de clase (compartida)

    def __init__(self, nombre):
        self.nombre = nombre  # Variable de instancia
        self.contador_personal = 0  # Variable de instancia
        Contador.contador_clase += 1

    def incrementar(self):
        self.contador_personal += 1
        variable_local = "Solo existe en este método"
        print(f"      {self.nombre}: {self.contador_personal}")


c1 = Contador("Ana")
c2 = Contador("Luis")

print("   Contadores personales:")
c1.incrementar()
c1.incrementar()
c2.incrementar()
print(f"   Total de contadores creados: {Contador.contador_clase}")
print()

# 🎯 Closure (Clausura)
print("🎯 EJEMPLO 7 - CLOSURE (Clausura):")
print()


def crear_multiplicador(factor):
    """Función que retorna otra función"""

    def multiplicar(numero):
        # Recuerda el 'factor' de la función externa
        return numero * factor

    return multiplicar


# Crear multiplicadores diferentes
multiplicar_por_2 = crear_multiplicador(2)
multiplicar_por_5 = crear_multiplicador(5)
multiplicar_por_10 = crear_multiplicador(10)

print("   Multiplicadores creados:")
print(f"      5 × 2 = {multiplicar_por_2(5)}")
print(f"      5 × 5 = {multiplicar_por_5(5)}")
print(f"      5 × 10 = {multiplicar_por_10(5)}")
print()

# 🚦 Scope con condicionales
print("🚦 EJEMPLO 8 - SCOPE CON CONDICIONALES:")
print()


def ejemplo_if_scope():
    es_dia = True

    if es_dia:
        mensaje = "Buenos días"  # Se crea dentro del if
    else:
        mensaje = "Buenas noches"

    # PERO en Python, 'mensaje' existe fuera del if también
    print(f"   Mensaje: {mensaje}")
    # (Esto es diferente a otros lenguajes)


ejemplo_if_scope()
print()

# 🎪 Comparación completa
print("🎪 EJEMPLO 9 - COMPARACIÓN COMPLETA:")
print()

variable_global = "Global"


def funcion_nivel_1():
    variable_nivel_1 = "Enclosing"

    def funcion_nivel_2():
        variable_nivel_2 = "Local"

        print("   🔍 Búsqueda LEGB:")
        print(f"      L (Local): {variable_nivel_2}")
        print(f"      E (Enclosing): {variable_nivel_1}")
        print(f"      G (Global): {variable_global}")
        print(f"      B (Built-in): {len('Python')}")  # len es built-in

    funcion_nivel_2()


funcion_nivel_1()
print()

print("=" * 70)
print("🎉 ¡Ahora entiendes el SCOPE de variables! 🎉")
print("=" * 70)
print()
print("📌 RESUMEN:")
print("   LOCAL → Dentro de función (tu habitación)")
print("   GLOBAL → En todo el programa (la sala)")
print("   ENCLOSING → En función contenedora (casa dentro de casa)")
print("   BUILT-IN → Predefinidos de Python")
print()
print("🔑 PALABRAS CLAVE:")
print("   global → Modificar variable global")
print("   nonlocal → Modificar variable de función externa")
print()
print("📏 REGLA LEGB:")
print("   Python busca en orden: Local → Enclosing → Global → Built-in")
print()
print("💡 TIPS:")
print("   ✅ Preferir variables locales (más seguras)")
print("   ✅ Usar global solo cuando sea necesario")
print("   ✅ Nombres descriptivos para evitar confusión")
print("   ⚠️ Una variable local oculta una global del mismo nombre")
print("=" * 70)
