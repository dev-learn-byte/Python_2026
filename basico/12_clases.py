"""
PYTHON DESDE CERO - LECCIÓN 12: CLASES (POO - Programación Orientada a Objetos)
================================================================================

🏗️ ¿Qué son las CLASES?
------------------------
Una CLASE es como un MOLDE o una PLANTILLA para crear cosas.

Imagina:
- MOLDE DE GALLETAS → Clase
- GALLETAS que haces con el molde → Objetos

- PLANO DE CASA → Clase
- CASAS construidas con ese plano → Objetos

- FÁBRICA DE JUGUETES → Clase
- JUGUETES que salen de la fábrica → Objetos

En programación:
- CLASE = El molde/plantilla (RECETA)
- OBJETO = La cosa creada usando ese molde (LA GALLETA)

Una clase tiene:
1. ATRIBUTOS = Características (color, tamaño, nombre)
2. MÉTODOS = Acciones/comportamientos (caminar, saltar, comer)

Es como un personaje de videojuego:
- Atributos: vida, fuerza, velocidad
- Métodos: atacar(), defender(), correr()
"""

print("=" * 60)
print("🎓 LECCIÓN 12: CLASES EN PYTHON")
print("=" * 60)
print()

# ============================================
# 1️⃣ CREAR UNA CLASE SIMPLE
# ============================================
print("=== 1. CREAR UNA CLASE SIMPLE ===")
print()


class Perro:
    """Clase que representa un perro"""

    def ladrar(self):
        print("   🐕 ¡Guau guau!")

    def comer(self):
        print("   🍖 Ñam ñam...")


print("🎯 EJEMPLO 1 - Clase Perro:")
# Crear objetos (instancias)
mi_perro = Perro()
mi_perro.ladrar()
mi_perro.comer()
print()

otro_perro = Perro()
otro_perro.ladrar()
print()

print("💡 EXPLICACIÓN:")
print("   - class Perro: → Crear la clase (el molde)")
print("   - mi_perro = Perro() → Crear un objeto (usar el molde)")
print("   - mi_perro.ladrar() → Llamar a un método")
print()

print("-" * 60)
print()


# ============================================
# 2️⃣ CLASE CON __init__ (Constructor)
# ============================================
print("=== 2. CLASE CON __init__ (Constructor) ===")
print()


class Gato:
    """Clase que representa un gato"""

    def __init__(self, nombre, color):
        """Constructor - se ejecuta al crear el objeto"""
        self.nombre = nombre
        self.color = color

    def maullar(self):
        print(f"   🐱 {self.nombre}: ¡Miau!")

    def presentarse(self):
        print(f"   Soy {self.nombre} y soy de color {self.color}")


print("🎯 EJEMPLO - Gatos con características:")
gato1 = Gato("Whiskers", "naranja")
gato1.presentarse()
gato1.maullar()
print()

gato2 = Gato("Luna", "blanco")
gato2.presentarse()
gato2.maullar()
print()

print("💡 __init__ es el CONSTRUCTOR:")
print("   - Se ejecuta automáticamente al crear el objeto")
print("   - self.nombre = nombre → Guarda el nombre en el objeto")
print("   - self es como decir 'este objeto específico'")
print()

print("-" * 60)
print()


# ============================================
# 3️⃣ ATRIBUTOS Y MÉTODOS
# ============================================
print("=== 3. ATRIBUTOS Y MÉTODOS ===")
print()


class Estudiante:
    """Clase que representa un estudiante"""

    def __init__(self, nombre, edad, grado):
        # ATRIBUTOS (características)
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        self.calificaciones = []

    # MÉTODOS (acciones)
    def estudiar(self, materia):
        print(f"   📚 {self.nombre} está estudiando {materia}")

    def agregar_calificacion(self, nota):
        self.calificaciones.append(nota)
        print(f"   ✅ Nota agregada: {nota}")

    def calcular_promedio(self):
        if len(self.calificaciones) == 0:
            return 0
        return sum(self.calificaciones) / len(self.calificaciones)

    def mostrar_info(self):
        print(f"   Estudiante: {self.nombre}")
        print(f"   Edad: {self.edad} años")
        print(f"   Grado: {self.grado}")
        promedio = self.calcular_promedio()
        print(f"   Promedio: {promedio:.1f}")


print("🎯 EJEMPLO - Estudiante:")
estudiante1 = Estudiante("Ana", 12, "7mo")
estudiante1.estudiar("Matemáticas")
estudiante1.agregar_calificacion(85)
estudiante1.agregar_calificacion(90)
estudiante1.agregar_calificacion(88)
estudiante1.mostrar_info()
print()

print("-" * 60)
print()


# ============================================
# 4️⃣ MÚLTIPLES OBJETOS
# ============================================
print("=== 4. CREAR MÚLTIPLES OBJETOS ===")
print()


class CuentaBancaria:
    """Clase que representa una cuenta bancaria"""

    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"   💰 Depósito: ${cantidad}")
        print(f"   💵 Nuevo saldo: ${self.saldo}")

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"   💸 Retiro: ${cantidad}")
            print(f"   💵 Nuevo saldo: ${self.saldo}")
        else:
            print(f"   ❌ Saldo insuficiente")

    def mostrar_saldo(self):
        print(f"   {self.titular}: ${self.saldo}")


print("🎯 EJEMPLO - Banco con varias cuentas:")
cuenta_ana = CuentaBancaria("Ana", 1000)
cuenta_luis = CuentaBancaria("Luis", 500)

print("Estado inicial:")
cuenta_ana.mostrar_saldo()
cuenta_luis.mostrar_saldo()
print()

print("Ana deposita $200:")
cuenta_ana.depositar(200)
print()

print("Luis retira $100:")
cuenta_luis.retirar(100)
print()

print("-" * 60)
print()


# ============================================
# 5️⃣ ATRIBUTOS DE CLASE vs INSTANCIA
# ============================================
print("=== 5. ATRIBUTOS DE CLASE vs INSTANCIA ===")
print()


class Videojuego:
    """Clase para personajes de videojuego"""

    # ATRIBUTO DE CLASE (compartido por todos)
    contador_personajes = 0
    juego = "Super Adventure"

    def __init__(self, nombre, nivel=1):
        # ATRIBUTOS DE INSTANCIA (únicos de cada objeto)
        self.nombre = nombre
        self.nivel = nivel
        self.vida = 100

        # Incrementar contador
        Videojuego.contador_personajes += 1

    def subir_nivel(self):
        self.nivel += 1
        print(f"   🎮 {self.nombre} subió al nivel {self.nivel}!")


print("🎯 EJEMPLO - Contador de personajes:")
print(f"   Juego: {Videojuego.juego}")
print(f"   Personajes creados: {Videojuego.contador_personajes}")
print()

personaje1 = Videojuego("Guerrero")
print(f"   Personajes creados: {Videojuego.contador_personajes}")

personaje2 = Videojuego("Mago")
print(f"   Personajes creados: {Videojuego.contador_personajes}")

personaje3 = Videojuego("Arquero")
print(f"   Personajes creados: {Videojuego.contador_personajes}")
print()

print("-" * 60)
print()


# ============================================
# 6️⃣ MÉTODO __str__ (Representación en texto)
# ============================================
print("=== 6. MÉTODO __str__ ===")
print()


class Libro:
    """Clase que representa un libro"""

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        """Cómo se muestra el objeto cuando lo imprimes"""
        return f"📖 '{self.titulo}' por {self.autor} ({self.paginas} págs)"


print("🎯 EJEMPLO - Imprimir objetos:")
libro1 = Libro("Python para Niños", "Jason Briggs", 350)
libro2 = Libro("El Principito", "Antoine de Saint-Exupéry", 96)

print(libro1)  # Usa __str__
print(libro2)
print()

print("-" * 60)
print()


# ============================================
# 7️⃣ HERENCIA (Una clase hereda de otra)
# ============================================
print("=== 7. HERENCIA - UNA CLASE HEREDA DE OTRA ===")
print()


class Animal:
    """Clase base - Animal"""

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hacer_sonido(self):
        print("   🔊 (Algún sonido)")

    def dormir(self):
        print(f"   💤 {self.nombre} está durmiendo... Zzz")


class Perro(Animal):
    """Perro hereda de Animal"""

    def hacer_sonido(self):
        print(f"   🐕 {self.nombre}: ¡Guau guau!")

    def traer_pelota(self):
        print(f"   🎾 {self.nombre} trae la pelota")


class Gato(Animal):
    """Gato hereda de Animal"""

    def hacer_sonido(self):
        print(f"   🐱 {self.nombre}: ¡Miau!")

    def trepar(self):
        print(f"   🌳 {self.nombre} trepa al árbol")


print("🎯 EJEMPLO - Herencia:")
mi_perro = Perro("Rex", 3)
mi_gato = Gato("Luna", 2)

print("Perro:")
mi_perro.hacer_sonido()  # Método de Perro
mi_perro.dormir()  # Método heredado de Animal
mi_perro.traer_pelota()  # Método de Perro
print()

print("Gato:")
mi_gato.hacer_sonido()  # Método de Gato
mi_gato.dormir()  # Método heredado de Animal
mi_gato.trepar()  # Método de Gato
print()

print("💡 HERENCIA:")
print("   - Perro hereda de Animal")
print("   - Tiene todos los métodos de Animal")
print("   - Puede agregar sus propios métodos")
print("   - Puede modificar métodos heredados")
print()

print("-" * 60)
print()


# ============================================
# 🎯 EJEMPLOS PRÁCTICOS DIVERTIDOS
# ============================================
print("=== 🎯 EJEMPLOS PRÁCTICOS ===")
print()

# 🚗 Clase Carro
print("🚗 CLASE CARRO:")


class Carro:
    def __init__(self, marca, modelo, año, color):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
        self.velocidad = 0
        self.encendido = False

    def encender(self):
        self.encendido = True
        print(f"   🔑 {self.marca} {self.modelo} encendido")

    def apagar(self):
        self.encendido = False
        self.velocidad = 0
        print(f"   🔴 {self.marca} {self.modelo} apagado")

    def acelerar(self, incremento):
        if self.encendido:
            self.velocidad += incremento
            print(f"   🏎️ Velocidad: {self.velocidad} km/h")
        else:
            print("   ⚠️ Primero enciende el carro")

    def frenar(self):
        self.velocidad = 0
        print(f"   🛑 Carro detenido")

    def __str__(self):
        return f"{self.color} {self.marca} {self.modelo} ({self.año})"


mi_carro = Carro("Toyota", "Corolla", 2024, "Rojo")
print(f"   Mi carro: {mi_carro}")
mi_carro.encender()
mi_carro.acelerar(50)
mi_carro.acelerar(30)
mi_carro.frenar()
mi_carro.apagar()
print()

# 🎮 Personaje de videojuego
print("🎮 PERSONAJE DE VIDEOJUEGO:")


class Personaje:
    def __init__(self, nombre, clase):
        self.nombre = nombre
        self.clase = clase
        self.nivel = 1
        self.vida = 100
        self.experiencia = 0
        self.inventario = []

    def atacar(self, enemigo):
        daño = 10 * self.nivel
        print(f"   ⚔️ {self.nombre} ataca a {enemigo}!")
        print(f"   💥 Daño: {daño}")
        return daño

    def ganar_experiencia(self, xp):
        self.experiencia += xp
        print(f"   ⭐ +{xp} XP (Total: {self.experiencia} XP)")

        # Subir de nivel cada 100 XP
        if self.experiencia >= 100 * self.nivel:
            self.subir_nivel()

    def subir_nivel(self):
        self.nivel += 1
        self.vida = 100
        print(f"   🎉 ¡Nivel {self.nivel} alcanzado!")
        print(f"   ❤️ Vida restaurada: {self.vida}")

    def recoger_item(self, item):
        self.inventario.append(item)
        print(f"   🎒 Recogiste: {item}")

    def mostrar_stats(self):
        print(f"   👤 {self.nombre} - {self.clase}")
        print(f"   ⭐ Nivel: {self.nivel}")
        print(f"   ❤️ Vida: {self.vida}")
        print(f"   📊 XP: {self.experiencia}")
        print(f"   🎒 Inventario: {self.inventario}")


heroe = Personaje("Arthas", "Guerrero")
heroe.mostrar_stats()
print()
heroe.atacar("Dragón")
heroe.ganar_experiencia(50)
heroe.recoger_item("Espada legendaria")
heroe.ganar_experiencia(60)
print()

# 📱 Smartphone
print("📱 SMARTPHONE:")


class Smartphone:
    def __init__(self, marca, modelo, bateria=100):
        self.marca = marca
        self.modelo = modelo
        self.bateria = bateria
        self.encendido = False
        self.apps = []

    def encender(self):
        if self.bateria > 0:
            self.encendido = True
            print(f"   📱 {self.marca} {self.modelo} encendido")
        else:
            print(f"   🔋 Batería agotada")

    def apagar(self):
        self.encendido = False
        print(f"   🌙 Teléfono apagado")

    def instalar_app(self, app):
        if app not in self.apps:
            self.apps.append(app)
            print(f"   📲 App instalada: {app}")
        else:
            print(f"   ℹ️ {app} ya está instalada")

    def usar_telefono(self, minutos):
        consumo = minutos * 2  # 2% por minuto
        self.bateria -= consumo
        if self.bateria < 0:
            self.bateria = 0
        print(f"   ⏱️ Usaste el teléfono {minutos} min")
        print(f"   🔋 Batería: {self.bateria}%")

    def cargar(self, porcentaje):
        self.bateria += porcentaje
        if self.bateria > 100:
            self.bateria = 100
        print(f"   ⚡ Cargando... Batería: {self.bateria}%")


telefono = Smartphone("iPhone", "15 Pro")
telefono.encender()
telefono.instalar_app("WhatsApp")
telefono.instalar_app("Instagram")
telefono.usar_telefono(10)
telefono.cargar(30)
print()

# 🏦 Sistema bancario mejorado
print("🏦 SISTEMA BANCARIO:")


class CuentaBancariaCompleta:
    def __init__(self, titular, numero_cuenta, saldo=0):
        self.titular = titular
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo
        self.historial = []

    def depositar(self, cantidad):
        self.saldo += cantidad
        self.historial.append(f"Depósito: +${cantidad}")
        print(f"   💰 Depósito exitoso: ${cantidad}")
        print(f"   💵 Saldo actual: ${self.saldo}")

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            self.historial.append(f"Retiro: -${cantidad}")
            print(f"   💸 Retiro exitoso: ${cantidad}")
            print(f"   💵 Saldo actual: ${self.saldo}")
        else:
            print(f"   ❌ Fondos insuficientes")

    def transferir(self, otra_cuenta, cantidad):
        if cantidad <= self.saldo:
            self.retirar(cantidad)
            otra_cuenta.depositar(cantidad)
            print(f"   💸 Transferencia exitosa a {otra_cuenta.titular}")
        else:
            print(f"   ❌ Fondos insuficientes para transferir")

    def ver_historial(self):
        print(f"   📋 Historial de {self.titular}:")
        for transaccion in self.historial:
            print(f"      - {transaccion}")


cuenta1 = CuentaBancariaCompleta("Ana", "001", 1000)
cuenta2 = CuentaBancariaCompleta("Luis", "002", 500)

cuenta1.depositar(200)
cuenta1.transferir(cuenta2, 300)
print()
cuenta1.ver_historial()
print()

# 🍕 Pizzería
print("🍕 PIZZERÍA:")


class Pizza:
    # Precios base
    PRECIO_BASE = {"Pequeña": 8, "Mediana": 12, "Grande": 16}
    PRECIO_INGREDIENTE = 2

    def __init__(self, tamaño, ingredientes=None):
        self.tamaño = tamaño
        self.ingredientes = ingredientes if ingredientes else [
            "Queso", "Tomate"]
        self.precio = self.calcular_precio()

    def agregar_ingrediente(self, ingrediente):
        if ingrediente not in self.ingredientes:
            self.ingredientes.append(ingrediente)
            self.precio = self.calcular_precio()
            print(f"   ✅ Agregado: {ingrediente}")

    def calcular_precio(self):
        precio_base = Pizza.PRECIO_BASE[self.tamaño]
        ingredientes_extra = len(self.ingredientes) - 2  # 2 básicos gratis
        if ingredientes_extra < 0:
            ingredientes_extra = 0
        return precio_base + (ingredientes_extra * Pizza.PRECIO_INGREDIENTE)

    def mostrar_orden(self):
        print(f"   🍕 Pizza {self.tamaño}")
        print(f"   🧀 Ingredientes: {', '.join(self.ingredientes)}")
        print(f"   💵 Precio: ${self.precio}")


mi_pizza = Pizza("Grande")
mi_pizza.mostrar_orden()
print()
mi_pizza.agregar_ingrediente("Pepperoni")
mi_pizza.agregar_ingrediente("Champiñones")
mi_pizza.mostrar_orden()
print()

# 🎓 Sistema escolar
print("🎓 SISTEMA ESCOLAR:")


class EstudianteAvanzado:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        self.materias = {}

    def inscribir_materia(self, materia):
        if materia not in self.materias:
            self.materias[materia] = []
            print(f"   📚 {self.nombre} inscrito en {materia}")

    def agregar_nota(self, materia, nota):
        if materia in self.materias:
            self.materias[materia].append(nota)
            print(f"   ✅ Nota agregada en {materia}: {nota}")
        else:
            print(f"   ❌ No está inscrito en {materia}")

    def promedio_materia(self, materia):
        if materia in self.materias and self.materias[materia]:
            return sum(self.materias[materia]) / len(self.materias[materia])
        return 0

    def promedio_general(self):
        if not self.materias:
            return 0
        promedios = [self.promedio_materia(m) for m in self.materias]
        return sum(promedios) / len(promedios)

    def reporte(self):
        print(f"   📊 Reporte de {self.nombre}")
        print(f"   Edad: {self.edad} | Grado: {self.grado}")
        for materia, notas in self.materias.items():
            prom = self.promedio_materia(materia)
            print(f"      {materia}: {notas} → Promedio: {prom:.1f}")
        print(f"   🏆 Promedio General: {self.promedio_general():.1f}")


alumno = EstudianteAvanzado("María", 13, "8vo")
alumno.inscribir_materia("Matemáticas")
alumno.inscribir_materia("Ciencias")
alumno.agregar_nota("Matemáticas", 90)
alumno.agregar_nota("Matemáticas", 85)
alumno.agregar_nota("Ciencias", 95)
alumno.agregar_nota("Ciencias", 92)
print()
alumno.reporte()
print()

# 🎯 Juego de cartas
print("🎯 JUEGO DE CARTAS:")


class Carta:
    def __init__(self, valor, palo):
        self.valor = valor  # A, 2, 3, ..., 10, J, Q, K
        self.palo = palo    # ♠, ♥, ♦, ♣

    def __str__(self):
        return f"{self.valor}{self.palo}"


class Mazo:
    def __init__(self):
        valores = ['A', '2', '3', '4', '5', '6',
                   '7', '8', '9', '10', 'J', 'Q', 'K']
        palos = ['♠', '♥', '♦', '♣']
        self.cartas = [Carta(v, p) for p in palos for v in valores]

    def mostrar_cartas(self, cantidad=5):
        print(f"   🃏 Primeras {cantidad} cartas:")
        for i in range(min(cantidad, len(self.cartas))):
            print(f"      {self.cartas[i]}")


mazo = Mazo()
print(f"   Cartas en el mazo: {len(mazo.cartas)}")
mazo.mostrar_cartas()
print()

print("=" * 60)
print("🎉 ¡Felicidades! Ya dominas las Clases en Python 🎉")
print("=" * 60)
print()
print("📌 RESUMEN:")
print("   - CLASE = Molde/Plantilla")
print("   - OBJETO = Cosa creada con ese molde")
print("   - ATRIBUTOS = Características (self.nombre)")
print("   - MÉTODOS = Acciones (def accion(self):)")
print("   - __init__ = Constructor (se ejecuta al crear)")
print("   - self = Este objeto específico")
print("   - HERENCIA = Una clase hereda de otra")
print()
print("💡 CONCEPTOS CLAVE:")
print("   ✅ class MiClase: → Crear clase")
print("   ✅ objeto = MiClase() → Crear objeto")
print("   ✅ self.atributo → Atributo del objeto")
print("   ✅ def metodo(self): → Método del objeto")
print("   ✅ class Hijo(Padre): → Herencia")
print()
print("🎮 PIENSA EN CLASES COMO:")
print("   - Moldes de galletas 🍪")
print("   - Planos de casas 🏠")
print("   - Personajes de videojuegos 🎮")
print("   - Fábricas de objetos 🏭")
print("=" * 60)
