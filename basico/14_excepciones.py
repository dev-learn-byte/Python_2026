"""
PYTHON DESDE CERO - LECCIÓN 14: EXCEPCIONES (Manejo de Errores)
================================================================

🛡️ ¿Qué son las EXCEPCIONES?
----------------------------
Una excepción es un ERROR que puede ocurrir cuando tu programa se ejecuta.

METÁFORA: Plan de Respaldo 🎯
-----------------------------
Imagina que vas a una fiesta:

- PLAN A: Ir en bicicleta
- PLAN B: Si llueve, ir en bus (EXCEPCIÓN)
- PLAN C: Si no hay bus, llamar a mamá (OTRA EXCEPCIÓN)

En programación:
- TRY → Intentar hacer algo (plan A)
- EXCEPT → Si sale mal, hacer esto (plan B)
- FINALLY → Pase lo que pase, hacer esto (siempre)

Ejemplo en la vida real:
- Intentas abrir la puerta (TRY)
- Si está cerrada con llave, usas la llave (EXCEPT)
- Cierras la puerta al salir (FINALLY - siempre lo haces)

¿Por qué son importantes?
- ✅ Evitan que tu programa se "rompa"
- ✅ Muestran mensajes útiles al usuario
- ✅ Permiten recuperarse de errores
- ✅ Hacen tu código más robusto
"""

print("=" * 70)
print("🎓 LECCIÓN 14: EXCEPCIONES EN PYTHON")
print("=" * 70)
print()

# ============================================
# 1️⃣ ERRORES SIN MANEJO (El programa se rompe)
# ============================================
print("=== 1. ¿QUÉ PASA SIN MANEJO DE ERRORES? ===")
print()

print("❌ EJEMPLO 1 - División por cero (COMENTADO):")
print("   # resultado = 10 / 0  # Esto ROMPE el programa")
print("   # ZeroDivisionError: division by zero")
print()

print("❌ EJEMPLO 2 - Índice fuera de rango (COMENTADO):")
print("   # lista = [1, 2, 3]")
print("   # print(lista[10])  # Esto ROMPE el programa")
print("   # IndexError: list index out of range")
print()

print("❌ EJEMPLO 3 - Variable no existe (COMENTADO):")
print("   # print(variable_que_no_existe)  # ROMPE el programa")
print("   # NameError: name 'variable_que_no_existe' is not defined")
print()

print("💡 SIN MANEJO DE ERRORES:")
print("   El programa se DETIENE completamente")
print("   El usuario ve un mensaje feo y confuso")
print()

print("-" * 70)
print()


# ============================================
# 2️⃣ TRY-EXCEPT BÁSICO
# ============================================
print("=== 2. TRY-EXCEPT - MANEJAR ERRORES ===")
print()

print("🛡️ METÁFORA: Intentar abrir una puerta")
print("   TRY: Intenta abrir")
print("   EXCEPT: Si está cerrada, usa la llave")
print()

print("✅ EJEMPLO 1 - División segura:")
try:
    resultado = 10 / 2
    print(f"   ✅ División exitosa: 10 / 2 = {resultado}")
except ZeroDivisionError:
    print("   ❌ No se puede dividir por cero")
print()

print("✅ EJEMPLO 2 - División por cero (manejada):")
try:
    resultado = 10 / 0
    print(f"   Resultado: {resultado}")
except ZeroDivisionError:
    print("   ❌ Error: No puedes dividir por cero")
    print("   💡 Usaremos 0 como resultado")
    resultado = 0
print(f"   Continuamos con el programa... resultado = {resultado}")
print()

print("💡 ESTRUCTURA:")
print("   try:")
print("       # Código que puede fallar")
print("   except TipoDeError:")
print("       # Qué hacer si falla")
print()

print("-" * 70)
print()


# ============================================
# 3️⃣ MÚLTIPLES EXCEPT (Varios tipos de errores)
# ============================================
print("=== 3. MÚLTIPLES EXCEPT - DIFERENTES ERRORES ===")
print()

print("🎯 EJEMPLO - Calculadora segura:")


def calculadora_segura(a, b, operacion):
    try:
        if operacion == "+":
            resultado = a + b
        elif operacion == "-":
            resultado = a - b
        elif operacion == "*":
            resultado = a * b
        elif operacion == "/":
            resultado = a / b
        else:
            resultado = "Operación no válida"

        print(f"   ✅ {a} {operacion} {b} = {resultado}")

    except ZeroDivisionError:
        print(f"   ❌ Error: No se puede dividir {a} entre 0")

    except TypeError:
        print(f"   ❌ Error: Los valores deben ser números")

    except Exception as e:
        print(f"   ❌ Error inesperado: {e}")


calculadora_segura(10, 2, "+")
calculadora_segura(10, 0, "/")
calculadora_segura(10, 2, "*")
print()

print("-" * 70)
print()


# ============================================
# 4️⃣ ELSE Y FINALLY
# ============================================
print("=== 4. ELSE Y FINALLY ===")
print()

print("🎯 EJEMPLO - Abrir archivo:")


def leer_numero():
    try:
        numero = int(input("   Ingresa un número: "))
    except ValueError:
        print("   ❌ Eso no es un número válido")
        numero = 0
    else:
        # Se ejecuta si NO hubo error
        print("   ✅ Número válido ingresado")
    finally:
        # SIEMPRE se ejecuta
        print("   🔒 Operación finalizada")

    return numero


# Ejemplo simulado (sin input real)
print("Simulación de lectura de número:")
try:
    numero = int("42")
    print(f"   Número leído: {numero}")
except ValueError:
    print("   ❌ Error al leer")
else:
    print("   ✅ Lectura exitosa")
finally:
    print("   🔒 Proceso completado")
print()

print("💡 ESTRUCTURA COMPLETA:")
print("   try:")
print("       # Intentar esto")
print("   except Error:")
print("       # Si falla, hacer esto")
print("   else:")
print("       # Si NO falla, hacer esto")
print("   finally:")
print("       # SIEMPRE hacer esto (pase lo que pase)")
print()

print("-" * 70)
print()


# ============================================
# 5️⃣ CAPTURAR EL ERROR (as e)
# ============================================
print("=== 5. CAPTURAR INFORMACIÓN DEL ERROR ===")
print()

print("🎯 EJEMPLO - Ver detalles del error:")


def dividir_con_info(a, b):
    try:
        resultado = a / b
        print(f"   ✅ Resultado: {resultado}")
    except ZeroDivisionError as error:
        print(f"   ❌ Error capturado: {error}")
        print(f"   ❌ Tipo de error: {type(error).__name__}")
    except Exception as error:
        print(f"   ❌ Error general: {error}")


dividir_con_info(10, 2)
dividir_con_info(10, 0)
print()

print("-" * 70)
print()


# ============================================
# 6️⃣ RAISE (Lanzar excepciones)
# ============================================
print("=== 6. RAISE - LANZAR TUS PROPIAS EXCEPCIONES ===")
print()

print("🎯 EJEMPLO - Validar edad:")


def verificar_edad(edad):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")
    elif edad > 150:
        raise ValueError("Esa edad no es realista")
    else:
        print(f"   ✅ Edad válida: {edad} años")


try:
    verificar_edad(25)
    verificar_edad(-5)
except ValueError as error:
    print(f"   ❌ Error: {error}")
print()

print("🎯 EJEMPLO 2 - Validar calificación:")


def registrar_calificacion(nota):
    if not (0 <= nota <= 100):
        raise ValueError(f"La nota {nota} debe estar entre 0 y 100")
    print(f"   ✅ Nota registrada: {nota}")


try:
    registrar_calificacion(85)
    registrar_calificacion(150)
except ValueError as error:
    print(f"   ❌ {error}")
print()

print("-" * 70)
print()


# ============================================
# 7️⃣ TIPOS COMUNES DE EXCEPCIONES
# ============================================
print("=== 7. TIPOS COMUNES DE EXCEPCIONES ===")
print()

print("📋 ERRORES MÁS COMUNES:")
print()

# ValueError
print("1️⃣ ValueError - Valor incorrecto:")
try:
    numero = int("abc")
except ValueError:
    print("   ❌ No se puede convertir 'abc' a número")
print()

# TypeError
print("2️⃣ TypeError - Tipo de dato incorrecto:")
try:
    resultado = "5" + 5
except TypeError:
    print("   ❌ No se puede sumar texto con número")
print()

# IndexError
print("3️⃣ IndexError - Índice fuera de rango:")
try:
    lista = [1, 2, 3]
    valor = lista[10]
except IndexError:
    print("   ❌ La lista no tiene 11 elementos")
print()

# KeyError
print("4️⃣ KeyError - Llave no existe:")
try:
    diccionario = {"nombre": "Ana", "edad": 12}
    valor = diccionario["apellido"]
except KeyError:
    print("   ❌ La llave 'apellido' no existe")
print()

# AttributeError
print("5️⃣ AttributeError - Atributo no existe:")
try:
    lista = [1, 2, 3]
    lista.append_error(4)
except AttributeError:
    print("   ❌ El método 'append_error' no existe")
print()

print("-" * 70)
print()


# ============================================
# 🎯 EJEMPLOS PRÁCTICOS COMPLETOS
# ============================================
print("=== 🎯 EJEMPLOS PRÁCTICOS ===")
print()

# 📝 Validar entrada del usuario
print("📝 EJEMPLO 1 - VALIDAR ENTRADA:")


def pedir_numero_seguro(mensaje, minimo=0, maximo=100):
    """Pide un número al usuario con validación"""
    # Simulamos con un valor predefinido
    valor_simulado = "42"

    try:
        numero = int(valor_simulado)

        if numero < minimo or numero > maximo:
            raise ValueError(f"El número debe estar entre {minimo} y {maximo}")

        print(f"   ✅ Número válido: {numero}")
        return numero

    except ValueError as error:
        print(f"   ❌ Error: {error}")
        return None


pedir_numero_seguro("Ingresa tu edad", 0, 120)
print()

# 🔐 Sistema de login
print("🔐 EJEMPLO 2 - SISTEMA DE LOGIN:")

usuarios = {
    "ana": "1234",
    "luis": "5678"
}


def login(usuario, contraseña):
    try:
        if usuario not in usuarios:
            raise ValueError("Usuario no existe")

        if usuarios[usuario] != contraseña:
            raise ValueError("Contraseña incorrecta")

        print(f"   ✅ Bienvenido {usuario}!")
        return True

    except ValueError as error:
        print(f"   ❌ Error de login: {error}")
        return False


login("ana", "1234")
login("ana", "wrong")
login("pedro", "1234")
print()

# 🛒 Carrito de compras
print("🛒 EJEMPLO 3 - CARRITO DE COMPRAS:")


class CarritoCompras:
    def __init__(self):
        self.productos = {}
        self.dinero = 100

    def agregar_producto(self, nombre, precio, cantidad):
        try:
            if precio < 0:
                raise ValueError("El precio no puede ser negativo")

            if cantidad <= 0:
                raise ValueError("La cantidad debe ser mayor a 0")

            if nombre in self.productos:
                self.productos[nombre]["cantidad"] += cantidad
            else:
                self.productos[nombre] = {
                    "precio": precio, "cantidad": cantidad}

            print(f"   ✅ Agregado: {cantidad}x {nombre} (${precio} c/u)")

        except ValueError as error:
            print(f"   ❌ Error: {error}")

    def calcular_total(self):
        total = 0
        for producto, datos in self.productos.items():
            total += datos["precio"] * datos["cantidad"]
        return total

    def comprar(self):
        try:
            total = self.calcular_total()

            if total > self.dinero:
                raise ValueError(
                    f"Fondos insuficientes. Necesitas ${total} pero solo tienes ${self.dinero}")

            self.dinero -= total
            print(f"   ✅ Compra exitosa!")
            print(f"   💰 Total: ${total}")
            print(f"   💵 Dinero restante: ${self.dinero}")
            self.productos = {}

        except ValueError as error:
            print(f"   ❌ {error}")


carrito = CarritoCompras()
carrito.agregar_producto("Manzana", 2, 5)
carrito.agregar_producto("Pan", 3, 2)
carrito.comprar()
print()

# 📊 Calcular promedio seguro
print("📊 EJEMPLO 4 - CALCULAR PROMEDIO SEGURO:")


def calcular_promedio_seguro(calificaciones):
    try:
        if not calificaciones:
            raise ValueError("La lista está vacía")

        # Verificar que todos sean números
        for nota in calificaciones:
            if not isinstance(nota, (int, float)):
                raise TypeError(f"'{nota}' no es un número")

            if nota < 0 or nota > 100:
                raise ValueError(f"La nota {nota} debe estar entre 0 y 100")

        promedio = sum(calificaciones) / len(calificaciones)
        print(f"   ✅ Promedio: {promedio:.1f}")
        return promedio

    except ValueError as error:
        print(f"   ❌ Error de valor: {error}")
        return None

    except TypeError as error:
        print(f"   ❌ Error de tipo: {error}")
        return None

    except Exception as error:
        print(f"   ❌ Error inesperado: {error}")
        return None


calcular_promedio_seguro([85, 90, 88, 92])
calcular_promedio_seguro([])
calcular_promedio_seguro([85, "noventa", 88])
calcular_promedio_seguro([85, 120, 88])
print()

# 🎮 Juego con vidas
print("🎮 EJEMPLO 5 - JUEGO CON VIDAS:")


class Jugador:
    def __init__(self, nombre, vidas=3):
        self.nombre = nombre
        self.vidas = vidas
        self.puntos = 0

    def perder_vida(self):
        try:
            if self.vidas <= 0:
                raise ValueError("Game Over - No quedan vidas")

            self.vidas -= 1
            print(f"   💔 {self.nombre} perdió una vida. Vidas: {self.vidas}")

            if self.vidas == 0:
                raise ValueError("Game Over")

        except ValueError as error:
            print(f"   ❌ {error}")
            raise

    def ganar_puntos(self, puntos):
        try:
            if puntos < 0:
                raise ValueError("Los puntos no pueden ser negativos")

            self.puntos += puntos
            print(f"   ⭐ +{puntos} puntos! Total: {self.puntos}")

        except ValueError as error:
            print(f"   ❌ {error}")


jugador = Jugador("Ana")
jugador.ganar_puntos(100)
jugador.perder_vida()
jugador.ganar_puntos(50)
print()

# 📁 Leer archivo (simulado)
print("📁 EJEMPLO 6 - LEER ARCHIVO (simulado):")


def leer_configuracion(archivo):
    try:
        # Simulamos que el archivo no existe
        if archivo == "config_no_existe.txt":
            raise FileNotFoundError(f"El archivo '{archivo}' no existe")

        # Simulamos lectura exitosa
        print(f"   ✅ Archivo '{archivo}' leído correctamente")
        return {"idioma": "español", "volumen": 80}

    except FileNotFoundError as error:
        print(f"   ❌ {error}")
        print(f"   💡 Usando configuración por defecto")
        return {"idioma": "español", "volumen": 50}

    finally:
        print(f"   🔒 Proceso de lectura finalizado")


config1 = leer_configuracion("config.txt")
print(f"   Configuración: {config1}")
print()

config2 = leer_configuracion("config_no_existe.txt")
print(f"   Configuración: {config2}")
print()

# 🎯 Validador de datos
print("🎯 EJEMPLO 7 - VALIDADOR DE DATOS:")


def validar_usuario(datos):
    errores = []

    try:
        # Validar nombre
        if "nombre" not in datos:
            errores.append("Falta el nombre")
        elif len(datos["nombre"]) < 3:
            errores.append("El nombre debe tener al menos 3 caracteres")

        # Validar edad
        if "edad" not in datos:
            errores.append("Falta la edad")
        elif not isinstance(datos["edad"], int):
            errores.append("La edad debe ser un número")
        elif datos["edad"] < 0 or datos["edad"] > 120:
            errores.append("La edad debe estar entre 0 y 120")

        # Validar email
        if "email" not in datos:
            errores.append("Falta el email")
        elif "@" not in datos["email"]:
            errores.append("Email inválido")

        if errores:
            raise ValueError("Datos inválidos")

        print(f"   ✅ Usuario válido: {datos['nombre']}")
        return True

    except ValueError:
        print(f"   ❌ Errores encontrados:")
        for error in errores:
            print(f"      - {error}")
        return False


validar_usuario({"nombre": "Ana", "edad": 12, "email": "ana@mail.com"})
validar_usuario({"nombre": "Lu", "edad": -5})
print()

# 💳 Procesar pago
print("💳 EJEMPLO 8 - PROCESAR PAGO:")


def procesar_pago(monto, metodo):
    try:
        if monto <= 0:
            raise ValueError("El monto debe ser mayor a 0")

        if metodo not in ["tarjeta", "efectivo", "transferencia"]:
            raise ValueError(f"Método de pago '{metodo}' no válido")

        print(f"   💰 Procesando pago de ${monto} por {metodo}")

        # Simulamos diferentes casos
        if metodo == "tarjeta" and monto > 1000:
            raise ValueError("Límite de tarjeta excedido")

        print(f"   ✅ Pago exitoso!")
        return True

    except ValueError as error:
        print(f"   ❌ Error en el pago: {error}")
        return False

    finally:
        print(f"   📄 Recibo generado")


procesar_pago(50, "efectivo")
print()
procesar_pago(1500, "tarjeta")
print()

# 🔒 Crear contraseña segura
print("🔒 EJEMPLO 9 - VALIDAR CONTRASEÑA:")


def validar_contraseña(password):
    try:
        if len(password) < 8:
            raise ValueError("La contraseña debe tener al menos 8 caracteres")

        if password.isalpha():
            raise ValueError("La contraseña debe contener números")

        if password.isdigit():
            raise ValueError("La contraseña debe contener letras")

        if password.islower():
            raise ValueError("La contraseña debe contener mayúsculas")

        print(f"   ✅ Contraseña segura")
        return True

    except ValueError as error:
        print(f"   ❌ {error}")
        return False


validar_contraseña("Python2026")
validar_contraseña("python")
validar_contraseña("12345678")
print()

print("=" * 70)
print("🎉 ¡Felicidades! Ya dominas el Manejo de Excepciones 🎉")
print("=" * 70)
print()
print("📌 RESUMEN:")
print("   try → Intenta hacer esto")
print("   except TipoError → Si falla, haz esto")
print("   else → Si NO falla, haz esto (opcional)")
print("   finally → SIEMPRE haz esto (opcional)")
print("   raise → Lanza tu propia excepción")
print()
print("🔑 EXCEPCIONES COMUNES:")
print("   ValueError → Valor incorrecto")
print("   TypeError → Tipo de dato incorrecto")
print("   ZeroDivisionError → División por cero")
print("   IndexError → Índice fuera de rango")
print("   KeyError → Llave no existe en diccionario")
print("   FileNotFoundError → Archivo no existe")
print("   AttributeError → Atributo no existe")
print()
print("💡 BUENAS PRÁCTICAS:")
print("   ✅ Captura errores específicos (no solo Exception)")
print("   ✅ Muestra mensajes útiles al usuario")
print("   ✅ Registra errores para debugging")
print("   ✅ No dejes bloques except vacíos")
print("   ✅ Usa finally para liberar recursos")
print()
print("🎯 CUÁNDO USAR:")
print("   - Entrada de usuario (puede ser incorrecta)")
print("   - Operaciones con archivos")
print("   - Conversiones de tipos")
print("   - Operaciones matemáticas (división, etc)")
print("   - Acceso a datos (listas, diccionarios)")
print("=" * 70)
print()
print("🎊 ¡HAS COMPLETADO LO BÁSICO DE PYTHON! 🎊")
print("=" * 70)
