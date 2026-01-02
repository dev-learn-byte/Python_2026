"""
Decoradores en Python
Aprende a crear y usar decoradores
"""

import time
import functools

# ============================================
# 1. DECORADOR BÁSICO
# ============================================
print("=== DECORADOR BÁSICO ===")

def mi_decorador(func):
    """Decorador simple que envuelve una función"""
    def wrapper():
        print("Antes de ejecutar la función")
        func()
        print("Después de ejecutar la función")
    return wrapper

@mi_decorador
def saludar():
    print("¡Hola!")

saludar()

# ============================================
# 2. DECORADOR CON ARGUMENTOS
# ============================================
print("\n=== DECORADOR CON ARGUMENTOS ===")

def decorador_con_args(func):
    """Decorador que acepta funciones con argumentos"""
    def wrapper(*args, **kwargs):
        print(f"Argumentos: {args}, {kwargs}")
        resultado = func(*args, **kwargs)
        print(f"Resultado: {resultado}")
        return resultado
    return wrapper

@decorador_con_args
def sumar(a, b):
    return a + b

suma = sumar(5, 3)

# ============================================
# 3. DECORADOR PARA MEDIR TIEMPO
# ============================================
print("\n=== DECORADOR PARA MEDIR TIEMPO ===")

def medir_tiempo(func):
    """Decorador que mide el tiempo de ejecución"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        tiempo_total = fin - inicio
        print(f"{func.__name__} tardó {tiempo_total:.4f} segundos")
        return resultado
    return wrapper

@medir_tiempo
def calcular_suma(n):
    """Calcular la suma de números del 1 al n"""
    return sum(range(1, n + 1))

resultado = calcular_suma(1000000)
print(f"Suma total: {resultado}")

# ============================================
# 4. DECORADOR CON PARÁMETROS
# ============================================
print("\n=== DECORADOR CON PARÁMETROS ===")

def repetir(veces):
    """Decorador que repite la ejecución de una función"""
    def decorador(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(veces):
                print(f"Ejecución {i + 1}:")
                resultado = func(*args, **kwargs)
            return resultado
        return wrapper
    return decorador

@repetir(veces=3)
def saludar_nombre(nombre):
    print(f"  ¡Hola, {nombre}!")

saludar_nombre("Ana")

# ============================================
# 5. DECORADOR DE CACHE (MEMOIZACIÓN)
# ============================================
print("\n=== DECORADOR DE CACHE ===")

def cache(func):
    """Decorador que cachea resultados de funciones"""
    cache_dict = {}
    
    @functools.wraps(func)
    def wrapper(*args):
        if args in cache_dict:
            print(f"Retornando desde cache para {args}")
            return cache_dict[args]
        
        resultado = func(*args)
        cache_dict[args] = resultado
        return resultado
    
    return wrapper

@cache
def fibonacci(n):
    """Calcular Fibonacci (versión recursiva optimizada con cache)"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("Calculando Fibonacci(10):")
print(f"Resultado: {fibonacci(10)}")

print("\nCalculando Fibonacci(10) nuevamente:")
print(f"Resultado: {fibonacci(10)}")

# Python también incluye @functools.lru_cache
@functools.lru_cache(maxsize=128)
def fibonacci_lru(n):
    """Fibonacci con cache LRU de Python"""
    if n <= 1:
        return n
    return fibonacci_lru(n - 1) + fibonacci_lru(n - 2)

print(f"\nFibonacci(30) con LRU cache: {fibonacci_lru(30)}")
print(f"Info del cache: {fibonacci_lru.cache_info()}")

# ============================================
# 6. DECORADOR DE VALIDACIÓN
# ============================================
print("\n=== DECORADOR DE VALIDACIÓN ===")

def validar_positivo(func):
    """Decorador que valida que los argumentos sean positivos"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError(f"El argumento {arg} debe ser positivo")
        return func(*args, **kwargs)
    return wrapper

@validar_positivo
def calcular_raiz_cuadrada(numero):
    """Calcular raíz cuadrada"""
    return numero ** 0.5

print(f"Raíz cuadrada de 16: {calcular_raiz_cuadrada(16)}")

try:
    print(f"Raíz cuadrada de -4: {calcular_raiz_cuadrada(-4)}")
except ValueError as e:
    print(f"Error: {e}")

# ============================================
# 7. DECORADOR DE CLASE
# ============================================
print("\n=== DECORADOR DE CLASE ===")

def singleton(cls):
    """Decorador que implementa el patrón Singleton"""
    instancias = {}
    
    @functools.wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instancias:
            instancias[cls] = cls(*args, **kwargs)
        return instancias[cls]
    
    return get_instance

@singleton
class Configuracion:
    """Clase de configuración (solo puede haber una instancia)"""
    
    def __init__(self):
        self.ajustes = {}
    
    def set_ajuste(self, clave, valor):
        self.ajustes[clave] = valor
    
    def get_ajuste(self, clave):
        return self.ajustes.get(clave)

# Crear "dos" instancias
config1 = Configuracion()
config2 = Configuracion()

config1.set_ajuste("idioma", "español")

print(f"config1 idioma: {config1.get_ajuste('idioma')}")
print(f"config2 idioma: {config2.get_ajuste('idioma')}")
print(f"¿Son la misma instancia?: {config1 is config2}")

# ============================================
# 8. MÚLTIPLES DECORADORES
# ============================================
print("\n=== MÚLTIPLES DECORADORES ===")

def decorador_superior(func):
    """Decorador 1"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Decorador superior - antes")
        resultado = func(*args, **kwargs)
        print("Decorador superior - después")
        return resultado
    return wrapper

def decorador_inferior(func):
    """Decorador 2"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Decorador inferior - antes")
        resultado = func(*args, **kwargs)
        print("Decorador inferior - después")
        return resultado
    return wrapper

@decorador_superior
@decorador_inferior
def funcion_decorada():
    print("Función original")

funcion_decorada()

# ============================================
# 9. DECORADORES CON CLASES
# ============================================
print("\n=== DECORADORES CON CLASES ===")

class ContadorLlamadas:
    """Decorador implementado como clase"""
    
    def __init__(self, func):
        self.func = func
        self.llamadas = 0
    
    def __call__(self, *args, **kwargs):
        self.llamadas += 1
        print(f"Llamada #{self.llamadas} a {self.func.__name__}")
        return self.func(*args, **kwargs)

@ContadorLlamadas
def funcion_contada():
    print("  Ejecutando función...")

funcion_contada()
funcion_contada()
funcion_contada()

# ============================================
# 10. EJERCICIO PRÁCTICO
# ============================================
print("\n=== EJERCICIO: SISTEMA DE LOGGING ===")

def log_llamadas(nivel="INFO"):
    """Decorador para registrar llamadas a funciones"""
    def decorador(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{nivel}] {timestamp} - Llamando a {func.__name__}")
            print(f"  Args: {args}, Kwargs: {kwargs}")
            
            try:
                resultado = func(*args, **kwargs)
                print(f"[{nivel}] {timestamp} - {func.__name__} completado exitosamente")
                print(f"  Resultado: {resultado}")
                return resultado
            except Exception as e:
                print(f"[ERROR] {timestamp} - {func.__name__} falló con error: {e}")
                raise
        
        return wrapper
    return decorador

@log_llamadas(nivel="DEBUG")
def dividir(a, b):
    """Dividir dos números"""
    return a / b

print("División exitosa:")
dividir(10, 2)

print("\nDivisión con error:")
try:
    dividir(10, 0)
except ZeroDivisionError:
    print("División por cero capturada")

# Decorador de autenticación
def requiere_autenticacion(func):
    """Decorador que simula verificación de autenticación"""
    @functools.wraps(func)
    def wrapper(usuario, *args, **kwargs):
        if usuario.get("autenticado", False):
            return func(usuario, *args, **kwargs)
        else:
            return "Error: Usuario no autenticado"
    return wrapper

@requiere_autenticacion
def operacion_sensible(usuario, accion):
    """Operación que requiere autenticación"""
    return f"Usuario {usuario['nombre']} realizó: {accion}"

usuario_auth = {"nombre": "Admin", "autenticado": True}
usuario_no_auth = {"nombre": "Visitante", "autenticado": False}

print(f"\n{operacion_sensible(usuario_auth, 'Eliminar archivo')}")
print(f"{operacion_sensible(usuario_no_auth, 'Eliminar archivo')}")
