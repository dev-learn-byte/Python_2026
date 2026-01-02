"""
Manejo de Archivos en Python
Aprende a leer y escribir archivos
"""

import os
import json

# ============================================
# 1. LEER ARCHIVOS DE TEXTO
# ============================================
print("=== LEER ARCHIVOS DE TEXTO ===")

# Crear un archivo de ejemplo
archivo_ejemplo = "/tmp/ejemplo.txt"
with open(archivo_ejemplo, "w", encoding="utf-8") as f:
    f.write("Primera línea\n")
    f.write("Segunda línea\n")
    f.write("Tercera línea\n")

# Leer todo el archivo
print("Leer todo el archivo:")
with open(archivo_ejemplo, "r", encoding="utf-8") as f:
    contenido = f.read()
    print(contenido)

# Leer línea por línea
print("Leer línea por línea:")
with open(archivo_ejemplo, "r", encoding="utf-8") as f:
    for numero, linea in enumerate(f, 1):
        print(f"  Línea {numero}: {linea.strip()}")

# Leer todas las líneas en una lista
print("\nLeer todas las líneas:")
with open(archivo_ejemplo, "r", encoding="utf-8") as f:
    lineas = f.readlines()
    print(f"  Total de líneas: {len(lineas)}")

# ============================================
# 2. ESCRIBIR ARCHIVOS DE TEXTO
# ============================================
print("\n=== ESCRIBIR ARCHIVOS DE TEXTO ===")

archivo_salida = "/tmp/salida.txt"

# Modo 'w' (write) - sobrescribe el archivo
with open(archivo_salida, "w", encoding="utf-8") as f:
    f.write("Escribiendo primera línea\n")
    f.write("Escribiendo segunda línea\n")

print("Archivo escrito en modo 'w'")

# Modo 'a' (append) - añade al final
with open(archivo_salida, "a", encoding="utf-8") as f:
    f.write("Añadiendo tercera línea\n")
    f.write("Añadiendo cuarta línea\n")

print("Líneas añadidas en modo 'a'")

# Leer y mostrar el contenido
with open(archivo_salida, "r", encoding="utf-8") as f:
    print("Contenido final:")
    print(f.read())

# ============================================
# 3. TRABAJAR CON RUTAS Y DIRECTORIOS
# ============================================
print("\n=== TRABAJAR CON RUTAS Y DIRECTORIOS ===")

# Crear directorio
directorio_temp = "/tmp/python_ejemplos"
if not os.path.exists(directorio_temp):
    os.makedirs(directorio_temp)
    print(f"Directorio creado: {directorio_temp}")

# Crear archivo en el directorio
archivo_en_dir = os.path.join(directorio_temp, "archivo.txt")
with open(archivo_en_dir, "w", encoding="utf-8") as f:
    f.write("Contenido del archivo en directorio\n")

# Listar archivos en directorio
print(f"\nArchivos en {directorio_temp}:")
for archivo in os.listdir(directorio_temp):
    ruta_completa = os.path.join(directorio_temp, archivo)
    print(f"  - {archivo} (tamaño: {os.path.getsize(ruta_completa)} bytes)")

# Información del archivo
print(f"\n¿El archivo existe?: {os.path.exists(archivo_en_dir)}")
print(f"¿Es un archivo?: {os.path.isfile(archivo_en_dir)}")
print(f"¿Es un directorio?: {os.path.isdir(archivo_en_dir)}")

# ============================================
# 4. TRABAJAR CON JSON
# ============================================
print("\n=== TRABAJAR CON JSON ===")

# Crear datos
datos = {
    "nombre": "Ana García",
    "edad": 28,
    "ciudad": "Madrid",
    "hobbies": ["lectura", "música", "viajes"],
    "activo": True
}

# Escribir JSON en archivo
archivo_json = "/tmp/datos.json"
with open(archivo_json, "w", encoding="utf-8") as f:
    json.dump(datos, f, indent=4, ensure_ascii=False)

print(f"Datos guardados en JSON")

# Leer JSON desde archivo
with open(archivo_json, "r", encoding="utf-8") as f:
    datos_leidos = json.load(f)

print(f"Datos leídos desde JSON:")
print(f"  Nombre: {datos_leidos['nombre']}")
print(f"  Edad: {datos_leidos['edad']}")
print(f"  Hobbies: {', '.join(datos_leidos['hobbies'])}")

# Convertir objeto a string JSON
json_string = json.dumps(datos, indent=2, ensure_ascii=False)
print(f"\nJSON como string:")
print(json_string)

# ============================================
# 5. MANEJO DE EXCEPCIONES CON ARCHIVOS
# ============================================
print("\n=== MANEJO DE EXCEPCIONES ===")

def leer_archivo_seguro(ruta):
    """Leer archivo con manejo de excepciones"""
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return f"Error: El archivo '{ruta}' no existe"
    except PermissionError:
        return f"Error: No tienes permisos para leer '{ruta}'"
    except Exception as e:
        return f"Error inesperado: {e}"

# Intentar leer archivo que no existe
print(leer_archivo_seguro("/tmp/no_existe.txt"))

# Intentar leer archivo que sí existe
print(leer_archivo_seguro(archivo_ejemplo)[:50] + "...")

# ============================================
# 6. CONTEXT MANAGERS PERSONALIZADOS
# ============================================
print("\n=== CONTEXT MANAGERS ===")

class ManejadorArchivo:
    """Context manager personalizado para archivos"""
    
    def __init__(self, nombre_archivo, modo):
        self.nombre_archivo = nombre_archivo
        self.modo = modo
        self.archivo = None
    
    def __enter__(self):
        print(f"Abriendo archivo: {self.nombre_archivo}")
        self.archivo = open(self.nombre_archivo, self.modo, encoding="utf-8")
        return self.archivo
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Cerrando archivo: {self.nombre_archivo}")
        if self.archivo:
            self.archivo.close()

# Usar el context manager personalizado
with ManejadorArchivo("/tmp/test.txt", "w") as f:
    f.write("Usando context manager personalizado\n")

# ============================================
# 7. LECTURA Y ESCRITURA BINARIA
# ============================================
print("\n=== ARCHIVOS BINARIOS ===")

# Escribir datos binarios
archivo_binario = "/tmp/datos.bin"
datos_binarios = bytes([65, 66, 67, 68, 69])  # ABCDE en ASCII

with open(archivo_binario, "wb") as f:
    f.write(datos_binarios)

print("Datos binarios escritos")

# Leer datos binarios
with open(archivo_binario, "rb") as f:
    leidos = f.read()
    print(f"Datos binarios leídos: {leidos}")
    print(f"Como texto: {leidos.decode('ascii')}")

# ============================================
# 8. EJERCICIO PRÁCTICO
# ============================================
print("\n=== EJERCICIO: REGISTRO DE ESTUDIANTES ===")

class RegistroEstudiantes:
    """Sistema de registro de estudiantes con persistencia en JSON"""
    
    def __init__(self, archivo):
        self.archivo = archivo
        self.estudiantes = self.cargar_estudiantes()
    
    def cargar_estudiantes(self):
        """Cargar estudiantes desde archivo JSON"""
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return []
    
    def guardar_estudiantes(self):
        """Guardar estudiantes en archivo JSON"""
        with open(self.archivo, "w", encoding="utf-8") as f:
            json.dump(self.estudiantes, f, indent=2, ensure_ascii=False)
    
    def agregar_estudiante(self, nombre, edad, carrera):
        """Agregar nuevo estudiante"""
        estudiante = {
            "id": len(self.estudiantes) + 1,
            "nombre": nombre,
            "edad": edad,
            "carrera": carrera
        }
        self.estudiantes.append(estudiante)
        self.guardar_estudiantes()
        return estudiante
    
    def listar_estudiantes(self):
        """Listar todos los estudiantes"""
        return self.estudiantes
    
    def buscar_por_nombre(self, nombre):
        """Buscar estudiante por nombre"""
        return [e for e in self.estudiantes if nombre.lower() in e["nombre"].lower()]

# Usar el sistema de registro
registro = RegistroEstudiantes("/tmp/estudiantes.json")

# Agregar estudiantes
registro.agregar_estudiante("Juan Pérez", 20, "Ingeniería")
registro.agregar_estudiante("María López", 22, "Medicina")
registro.agregar_estudiante("Carlos García", 21, "Derecho")

print("Estudiantes registrados:")
for est in registro.listar_estudiantes():
    print(f"  ID: {est['id']}, Nombre: {est['nombre']}, Carrera: {est['carrera']}")

# Buscar estudiante
print("\nBuscar 'María':")
resultados = registro.buscar_por_nombre("María")
for est in resultados:
    print(f"  Encontrado: {est['nombre']} - {est['carrera']}")

print("\n✓ Los datos se han guardado en /tmp/estudiantes.json")
