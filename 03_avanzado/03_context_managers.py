"""
Context Managers y Manejo Avanzado de Recursos
Aprende sobre gestión de recursos y context managers
"""

import contextlib
import time
import sqlite3

# ============================================
# 1. CONTEXT MANAGERS CON CLASES
# ============================================
print("=== CONTEXT MANAGERS CON CLASES ===")

class GestorArchivo:
    """Context manager para gestión de archivos"""
    
    def __init__(self, nombre_archivo, modo):
        self.nombre_archivo = nombre_archivo
        self.modo = modo
        self.archivo = None
    
    def __enter__(self):
        print(f"Abriendo archivo: {self.nombre_archivo}")
        self.archivo = open(self.nombre_archivo, self.modo, encoding='utf-8')
        return self.archivo
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Cerrando archivo: {self.nombre_archivo}")
        if self.archivo:
            self.archivo.close()
        
        # Si exc_type no es None, hubo una excepción
        if exc_type is not None:
            print(f"Se produjo una excepción: {exc_type.__name__}: {exc_val}")
        
        # Retornar False para propagar la excepción
        # Retornar True para suprimir la excepción
        return False

# Usar el context manager
with GestorArchivo("/tmp/test_cm.txt", "w") as f:
    f.write("Escribiendo con context manager\n")

print()

# ============================================
# 2. CONTEXT MANAGERS CON @contextmanager
# ============================================
print("=== CONTEXT MANAGERS CON DECORADOR ===")

@contextlib.contextmanager
def temporizador(nombre):
    """Context manager para medir tiempo de ejecución"""
    print(f"Iniciando: {nombre}")
    inicio = time.time()
    
    try:
        yield  # El código del with se ejecuta aquí
    finally:
        fin = time.time()
        print(f"Finalizando: {nombre}")
        print(f"Tiempo transcurrido: {fin - inicio:.4f} segundos")

# Usar el context manager
with temporizador("Operación de suma"):
    total = sum(range(1, 1000001))
    print(f"  Suma calculada: {total}")

print()

# ============================================
# 3. MÚLTIPLES CONTEXT MANAGERS
# ============================================
print("=== MÚLTIPLES CONTEXT MANAGERS ===")

# Forma tradicional (anidada)
print("Forma anidada:")
with open("/tmp/archivo1.txt", "w") as f1:
    with open("/tmp/archivo2.txt", "w") as f2:
        f1.write("Contenido archivo 1\n")
        f2.write("Contenido archivo 2\n")

# Forma moderna (Python 3.1+)
print("\nForma en una línea:")
with open("/tmp/archivo3.txt", "w") as f3, \
     open("/tmp/archivo4.txt", "w") as f4:
    f3.write("Contenido archivo 3\n")
    f4.write("Contenido archivo 4\n")

print("Archivos creados exitosamente")

# ============================================
# 4. CONTEXT MANAGER PARA BASE DE DATOS
# ============================================
print("\n=== CONTEXT MANAGER PARA BASE DE DATOS ===")

class ConexionDB:
    """Context manager para conexiones de base de datos"""
    
    def __init__(self, db_path):
        self.db_path = db_path
        self.conexion = None
        self.cursor = None
    
    def __enter__(self):
        print(f"Conectando a base de datos: {self.db_path}")
        self.conexion = sqlite3.connect(self.db_path)
        self.cursor = self.conexion.cursor()
        return self.cursor
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print("Commit de transacción")
            self.conexion.commit()
        else:
            print("Rollback de transacción")
            self.conexion.rollback()
        
        print("Cerrando conexión")
        self.conexion.close()
        return False

# Usar el context manager de DB
db_path = "/tmp/test.db"

with ConexionDB(db_path) as cursor:
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY,
            nombre TEXT,
            edad INTEGER
        )
    """)
    cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", 
                   ("Juan", 25))

print("Datos insertados en la base de datos\n")

# ============================================
# 5. CONTEXT MANAGER REUTILIZABLE
# ============================================
print("=== CONTEXT MANAGER REUTILIZABLE ===")

@contextlib.contextmanager
def cambiar_directorio(nuevo_dir):
    """Context manager para cambiar temporalmente de directorio"""
    import os
    dir_anterior = os.getcwd()
    
    try:
        print(f"Cambiando de {dir_anterior} a {nuevo_dir}")
        os.chdir(nuevo_dir)
        yield
    finally:
        print(f"Regresando a {dir_anterior}")
        os.chdir(dir_anterior)

# Usar el context manager
import os
print(f"Directorio actual: {os.getcwd()}")

with cambiar_directorio("/tmp"):
    print(f"Dentro del with: {os.getcwd()}")

print(f"Después del with: {os.getcwd()}")

print()

# ============================================
# 6. SUPPRESS - SUPRIMIR EXCEPCIONES
# ============================================
print("=== SUPRIMIR EXCEPCIONES ===")

import os

# Sin suppress
print("Sin suppress:")
try:
    os.remove("/tmp/archivo_inexistente.txt")
except FileNotFoundError:
    print("  Archivo no encontrado (excepción capturada)")

# Con suppress
print("\nCon suppress:")
with contextlib.suppress(FileNotFoundError):
    os.remove("/tmp/archivo_inexistente.txt")
    print("  Esta línea se ejecuta si no hay error")
print("  Continúa la ejecución sin error")

print()

# ============================================
# 7. CONTEXT MANAGER CON RECURSOS PERSONALIZADOS
# ============================================
print("=== GESTOR DE RECURSOS PERSONALIZADO ===")

class GestorRecurso:
    """Simula gestión de un recurso (conexión, archivo, etc.)"""
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.activo = False
    
    def adquirir(self):
        """Adquirir el recurso"""
        print(f"Adquiriendo recurso: {self.nombre}")
        self.activo = True
    
    def liberar(self):
        """Liberar el recurso"""
        print(f"Liberando recurso: {self.nombre}")
        self.activo = False
    
    def usar(self):
        """Usar el recurso"""
        if not self.activo:
            raise RuntimeError("El recurso no está activo")
        print(f"Usando recurso: {self.nombre}")

@contextlib.contextmanager
def usar_recurso(nombre):
    """Context manager para gestionar el recurso"""
    recurso = GestorRecurso(nombre)
    recurso.adquirir()
    
    try:
        yield recurso
    finally:
        recurso.liberar()

# Usar el context manager
with usar_recurso("Conexión API") as recurso:
    recurso.usar()

print()

# ============================================
# 8. REDIRECT STDOUT/STDERR
# ============================================
print("=== REDIRIGIR SALIDA ===")

import io

# Capturar stdout
print("Capturando stdout:")
f = io.StringIO()
with contextlib.redirect_stdout(f):
    print("Este mensaje va al StringIO")
    print("Este también")

capturado = f.getvalue()
print(f"Contenido capturado:\n{capturado}")

# ============================================
# 9. CLOSING - CERRAR OBJETOS
# ============================================
print("=== CLOSING ===")

class Conexion:
    """Simula una conexión que necesita ser cerrada"""
    
    def __init__(self, nombre):
        self.nombre = nombre
        print(f"Conexión abierta: {nombre}")
    
    def close(self):
        print(f"Conexión cerrada: {self.nombre}")
    
    def enviar(self, datos):
        print(f"Enviando datos: {datos}")

# Usar closing
with contextlib.closing(Conexion("API REST")) as conn:
    conn.enviar("Datos importantes")

print()

# ============================================
# 10. EJERCICIO PRÁCTICO
# ============================================
print("=== EJERCICIO: SISTEMA DE TRANSACCIONES ===")

class SistemaTransaccional:
    """Sistema que gestiona transacciones con rollback automático"""
    
    def __init__(self):
        self.datos = {}
        self.respaldo = None
    
    def __enter__(self):
        print("Iniciando transacción")
        # Hacer respaldo del estado actual
        self.respaldo = self.datos.copy()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print("Commit exitoso")
            self.respaldo = None
            return True
        else:
            print(f"Error detectado: {exc_val}")
            print("Haciendo rollback")
            # Restaurar datos del respaldo
            self.datos = self.respaldo
            self.respaldo = None
            # Retornar True para suprimir la excepción
            return True
    
    def agregar(self, clave, valor):
        """Agregar dato"""
        self.datos[clave] = valor
        print(f"  Agregado: {clave} = {valor}")
    
    def mostrar(self):
        """Mostrar todos los datos"""
        print(f"  Datos: {self.datos}")

sistema = SistemaTransaccional()

# Transacción exitosa
print("\n1. Transacción exitosa:")
with sistema as trans:
    trans.agregar("usuario1", "Juan")
    trans.agregar("usuario2", "María")

sistema.mostrar()

# Transacción con error
print("\n2. Transacción con error:")
try:
    with sistema as trans:
        trans.agregar("usuario3", "Pedro")
        trans.mostrar()
        # Simular un error
        raise ValueError("Error simulado en la transacción")
        trans.agregar("usuario4", "Ana")  # No se ejecutará
except:
    pass

print("\nDatos después del rollback:")
sistema.mostrar()

# ============================================
# 11. CONTEXT MANAGER ANIDADOS PERSONALIZADOS
# ============================================
print("\n=== CONTEXT MANAGERS ANIDADOS ===")

@contextlib.contextmanager
def logger(nombre):
    """Context manager para logging"""
    print(f"[LOG] Iniciando: {nombre}")
    try:
        yield nombre
    finally:
        print(f"[LOG] Finalizando: {nombre}")

# Usar múltiples context managers anidados
with logger("Operación principal"):
    print("  Ejecutando operación principal")
    
    with logger("Sub-operación 1"):
        print("    Ejecutando sub-operación 1")
    
    with logger("Sub-operación 2"):
        print("    Ejecutando sub-operación 2")

print("\n✓ Gestión de recursos completada")
