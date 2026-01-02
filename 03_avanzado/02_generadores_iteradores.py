"""
Generadores e Iteradores en Python
Aprende sobre iteración avanzada y generadores
"""

import sys

# ============================================
# 1. ITERADORES BÁSICOS
# ============================================
print("=== ITERADORES BÁSICOS ===")

# Todos estos son iterables
lista = [1, 2, 3, 4, 5]
tupla = (10, 20, 30)
cadena = "Python"

print("Iterando sobre lista:")
for item in lista:
    print(f"  {item}")

# Crear un iterador manualmente
iterador = iter(lista)
print("\nUsando next():")
print(f"  Primero: {next(iterador)}")
print(f"  Segundo: {next(iterador)}")
print(f"  Tercero: {next(iterador)}")

# ============================================
# 2. CREAR UN ITERADOR PERSONALIZADO
# ============================================
print("\n=== ITERADOR PERSONALIZADO ===")

class ContadorHasta:
    """Iterador que cuenta hasta un número"""
    
    def __init__(self, maximo):
        self.maximo = maximo
        self.actual = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.actual < self.maximo:
            self.actual += 1
            return self.actual
        raise StopIteration

contador = ContadorHasta(5)
print("Contador hasta 5:")
for num in contador:
    print(f"  {num}")

# ============================================
# 3. GENERADORES CON YIELD
# ============================================
print("\n=== GENERADORES CON YIELD ===")

def generar_numeros(n):
    """Generador simple que produce números del 1 al n"""
    for i in range(1, n + 1):
        yield i

print("Generador de números del 1 al 5:")
for num in generar_numeros(5):
    print(f"  {num}")

# Los generadores son perezosos (lazy)
generador = generar_numeros(1000000)
print(f"\nTamaño del generador en memoria: {sys.getsizeof(generador)} bytes")
lista_grande = list(range(1, 1000001))
print(f"Tamaño de lista equivalente: {sys.getsizeof(lista_grande)} bytes")

# ============================================
# 4. GENERADORES CON MÚLTIPLES YIELDS
# ============================================
print("\n=== GENERADORES CON MÚLTIPLES YIELDS ===")

def fibonacci_gen(n):
    """Generador de números Fibonacci"""
    a, b = 0, 1
    contador = 0
    
    while contador < n:
        yield a
        a, b = b, a + b
        contador += 1

print("Primeros 10 números de Fibonacci:")
for num in fibonacci_gen(10):
    print(f"  {num}", end=" ")
print()

# ============================================
# 5. EXPRESIONES GENERADORAS
# ============================================
print("\n=== EXPRESIONES GENERADORAS ===")

# Similar a list comprehension pero con ()
cuadrados_gen = (x ** 2 for x in range(1, 6))
print("Cuadrados generados:")
for cuadrado in cuadrados_gen:
    print(f"  {cuadrado}")

# Más eficiente en memoria
suma_cuadrados = sum(x ** 2 for x in range(1, 1001))
print(f"\nSuma de cuadrados del 1 al 1000: {suma_cuadrados}")

# ============================================
# 6. GENERADORES PARA LEER ARCHIVOS GRANDES
# ============================================
print("\n=== GENERADORES PARA ARCHIVOS ===")

def leer_lineas_archivo(ruta):
    """Generador que lee un archivo línea por línea"""
    with open(ruta, 'r', encoding='utf-8') as f:
        for linea in f:
            yield linea.strip()

# Crear archivo de ejemplo
archivo_temp = "/tmp/archivo_grande.txt"
with open(archivo_temp, 'w', encoding='utf-8') as f:
    for i in range(1, 11):
        f.write(f"Línea {i}: Contenido de ejemplo\n")

print("Leyendo archivo con generador:")
for i, linea in enumerate(leer_lineas_archivo(archivo_temp), 1):
    if i <= 3:  # Solo mostrar primeras 3 líneas
        print(f"  {linea}")

# ============================================
# 7. YIELD FROM
# ============================================
print("\n=== YIELD FROM ===")

def generador_interno():
    """Generador interno"""
    yield 1
    yield 2
    yield 3

def generador_externo():
    """Generador que delega a otro generador"""
    yield "Inicio"
    yield from generador_interno()  # Delegar al generador interno
    yield "Fin"

print("Usando yield from:")
for valor in generador_externo():
    print(f"  {valor}")

# ============================================
# 8. GENERADORES INFINITOS
# ============================================
print("\n=== GENERADORES INFINITOS ===")

def contador_infinito(inicio=0):
    """Generador que cuenta infinitamente"""
    n = inicio
    while True:
        yield n
        n += 1

print("Primeros 10 números del contador infinito:")
contador = contador_infinito(1)
for i in range(10):
    print(f"  {next(contador)}", end=" ")
print()

# ============================================
# 9. ITERTOOLS - ITERADORES AVANZADOS
# ============================================
print("\n=== ITERTOOLS ===")

import itertools

# count - contador infinito
print("itertools.count (primeros 5):")
for i, num in enumerate(itertools.count(10, 2)):
    if i >= 5:
        break
    print(f"  {num}", end=" ")
print()

# cycle - cicla infinitamente sobre un iterable
print("\nitertools.cycle (primeros 10):")
ciclo = itertools.cycle(['A', 'B', 'C'])
for i in range(10):
    print(f"  {next(ciclo)}", end=" ")
print()

# chain - encadena iterables
print("\nitertools.chain:")
lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
for item in itertools.chain(lista1, lista2):
    print(f"  {item}", end=" ")
print()

# combinations - combinaciones
print("\nitertools.combinations:")
for combo in itertools.combinations([1, 2, 3, 4], 2):
    print(f"  {combo}")

# permutations - permutaciones
print("\nitertools.permutations:")
for perm in itertools.permutations([1, 2, 3], 2):
    print(f"  {perm}")

# ============================================
# 10. GENERADORES CON SEND()
# ============================================
print("\n=== GENERADORES CON SEND() ===")

def generador_interactivo():
    """Generador que puede recibir valores"""
    print("Generador iniciado")
    
    while True:
        valor = yield  # Recibir valor
        if valor is None:
            break
        print(f"  Recibido: {valor}")
        yield f"Procesado: {valor}"

gen = generador_interactivo()
next(gen)  # Iniciar el generador

print("Enviando valores al generador:")
print(gen.send("Hola"))
next(gen)
print(gen.send(42))
next(gen)
print(gen.send("Python"))

# ============================================
# 11. EJERCICIO PRÁCTICO
# ============================================
print("\n=== EJERCICIO: PROCESAMIENTO DE DATOS ===")

def leer_numeros(archivo):
    """Generador que lee números de un archivo"""
    with open(archivo, 'r') as f:
        for linea in f:
            try:
                yield float(linea.strip())
            except ValueError:
                continue

def filtrar_pares(numeros):
    """Generador que filtra números pares"""
    for num in numeros:
        if num % 2 == 0:
            yield num

def calcular_cuadrados(numeros):
    """Generador que calcula cuadrados"""
    for num in numeros:
        yield num ** 2

# Crear archivo con números
archivo_numeros = "/tmp/numeros.txt"
with open(archivo_numeros, 'w') as f:
    for i in range(1, 21):
        f.write(f"{i}\n")

print("Pipeline de procesamiento de datos:")

# Pipeline de generadores (muy eficiente en memoria)
numeros = leer_numeros(archivo_numeros)
pares = filtrar_pares(numeros)
cuadrados = calcular_cuadrados(pares)

print("Cuadrados de números pares:")
for i, resultado in enumerate(cuadrados):
    print(f"  {resultado}", end=" ")
    if (i + 1) % 5 == 0:
        print()

# ============================================
# 12. GENERADOR PARA DATOS EN LOTES
# ============================================
print("\n\n=== GENERADOR DE LOTES ===")

def generar_lotes(iterable, tamaño_lote):
    """Generador que divide datos en lotes"""
    lote = []
    for item in iterable:
        lote.append(item)
        if len(lote) == tamaño_lote:
            yield lote
            lote = []
    
    if lote:  # Yield del último lote si no está vacío
        yield lote

datos = range(1, 23)
print("Procesando datos en lotes de 5:")
for i, lote in enumerate(generar_lotes(datos, 5), 1):
    print(f"  Lote {i}: {lote}")

# ============================================
# 13. GENERADOR RECURSIVO
# ============================================
print("\n=== GENERADOR RECURSIVO ===")

def recorrer_anidado(estructura):
    """Generador recursivo para recorrer estructuras anidadas"""
    if isinstance(estructura, list):
        for item in estructura:
            yield from recorrer_anidado(item)
    else:
        yield estructura

estructura_compleja = [1, [2, 3, [4, 5]], 6, [7, [8, 9]]]
print(f"Estructura: {estructura_compleja}")
print("Elementos aplanados:")
for elemento in recorrer_anidado(estructura_compleja):
    print(f"  {elemento}", end=" ")
print()
