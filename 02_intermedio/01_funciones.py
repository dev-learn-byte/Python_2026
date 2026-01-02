"""
Funciones en Python
Aprende a crear y usar funciones
"""

# ============================================
# 1. FUNCIONES BÁSICAS
# ============================================
print("=== FUNCIONES BÁSICAS ===")

def saludar():
    """Función simple sin parámetros"""
    print("¡Hola, mundo!")

saludar()

# Función con parámetros
def saludar_persona(nombre):
    """Función con un parámetro"""
    print(f"¡Hola, {nombre}!")

saludar_persona("Ana")

# Función con retorno
def sumar(a, b):
    """Función que retorna un valor"""
    return a + b

resultado = sumar(5, 3)
print(f"5 + 3 = {resultado}")

# ============================================
# 2. PARÁMETROS POR DEFECTO
# ============================================
print("\n=== PARÁMETROS POR DEFECTO ===")

def saludar_con_titulo(nombre, titulo="Sr./Sra."):
    """Función con parámetro por defecto"""
    return f"¡Hola, {titulo} {nombre}!"

print(saludar_con_titulo("García"))
print(saludar_con_titulo("González", "Dr."))

# ============================================
# 3. ARGUMENTOS POSICIONALES Y NOMBRADOS
# ============================================
print("\n=== ARGUMENTOS POSICIONALES Y NOMBRADOS ===")

def describir_persona(nombre, edad, ciudad):
    """Función con múltiples parámetros"""
    return f"{nombre} tiene {edad} años y vive en {ciudad}"

# Argumentos posicionales
print(describir_persona("Juan", 25, "Madrid"))

# Argumentos nombrados (keywords)
print(describir_persona(edad=30, nombre="María", ciudad="Barcelona"))

# ============================================
# 4. *ARGS - ARGUMENTOS VARIABLES
# ============================================
print("\n=== *ARGS - ARGUMENTOS VARIABLES ===")

def sumar_varios(*numeros):
    """Función que acepta cualquier cantidad de argumentos"""
    total = sum(numeros)
    return total

print(f"Suma de 1, 2, 3: {sumar_varios(1, 2, 3)}")
print(f"Suma de 1, 2, 3, 4, 5: {sumar_varios(1, 2, 3, 4, 5)}")

# ============================================
# 5. **KWARGS - ARGUMENTOS CON NOMBRE VARIABLES
# ============================================
print("\n=== **KWARGS - ARGUMENTOS CON NOMBRE VARIABLES ===")

def mostrar_info(**datos):
    """Función que acepta argumentos nombrados variables"""
    for clave, valor in datos.items():
        print(f"  {clave}: {valor}")

print("Información de persona:")
mostrar_info(nombre="Pedro", edad=35, profesion="Ingeniero")

# ============================================
# 6. FUNCIONES LAMBDA (ANÓNIMAS)
# ============================================
print("\n=== FUNCIONES LAMBDA ===")

# Función lambda simple
cuadrado = lambda x: x ** 2
print(f"Cuadrado de 5: {cuadrado(5)}")

# Lambda con múltiples parámetros
sumar = lambda a, b: a + b
print(f"Suma de 3 y 7: {sumar(3, 7)}")

# Lambda con map()
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x ** 2, numeros))
print(f"Números: {numeros}")
print(f"Cuadrados: {cuadrados}")

# Lambda con filter()
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f"Números pares: {pares}")

# ============================================
# 7. SCOPE (ÁMBITO) DE VARIABLES
# ============================================
print("\n=== SCOPE DE VARIABLES ===")

x = 10  # Variable global

def funcion_scope():
    """Demostración de scope local y global"""
    y = 5  # Variable local
    print(f"Dentro de la función - x: {x}, y: {y}")

funcion_scope()
print(f"Fuera de la función - x: {x}")

# Modificar variable global
contador = 0

def incrementar():
    """Modificar variable global"""
    global contador
    contador += 1
    return contador

print(f"Contador inicial: {contador}")
print(f"Después de incrementar: {incrementar()}")
print(f"Después de incrementar: {incrementar()}")

# ============================================
# 8. DOCSTRINGS
# ============================================
print("\n=== DOCSTRINGS ===")

def calcular_area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo.
    
    Args:
        base (float): La base del rectángulo
        altura (float): La altura del rectángulo
    
    Returns:
        float: El área del rectángulo
    
    Example:
        >>> calcular_area_rectangulo(5, 3)
        15
    """
    return base * altura

area = calcular_area_rectangulo(5, 3)
print(f"Área del rectángulo: {area}")
print(f"\nDocstring de la función:\n{calcular_area_rectangulo.__doc__}")

# ============================================
# 9. FUNCIONES RECURSIVAS
# ============================================
print("\n=== FUNCIONES RECURSIVAS ===")

def factorial(n):
    """Calcular factorial de forma recursiva"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

numero = 5
print(f"Factorial de {numero}: {factorial(numero)}")

# Fibonacci recursivo
def fibonacci(n):
    """Calcular n-ésimo número de Fibonacci"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(f"Primeros 10 números de Fibonacci:")
print([fibonacci(i) for i in range(10)])

# ============================================
# 10. EJERCICIO PRÁCTICO
# ============================================
print("\n=== EJERCICIO: CALCULADORA AVANZADA ===")

def calculadora(operacion, *numeros):
    """
    Calculadora que realiza operaciones sobre múltiples números
    
    Args:
        operacion (str): 'suma', 'resta', 'multiplicacion', 'promedio'
        *numeros: Números sobre los que operar
    
    Returns:
        float: Resultado de la operación
    """
    if not numeros:
        return 0
    
    if operacion == "suma":
        return sum(numeros)
    elif operacion == "resta":
        resultado = numeros[0]
        for num in numeros[1:]:
            resultado -= num
        return resultado
    elif operacion == "multiplicacion":
        resultado = 1
        for num in numeros:
            resultado *= num
        return resultado
    elif operacion == "promedio":
        return sum(numeros) / len(numeros)
    else:
        return "Operación no válida"

print(f"Suma de 1, 2, 3, 4, 5: {calculadora('suma', 1, 2, 3, 4, 5)}")
print(f"Promedio de 10, 20, 30: {calculadora('promedio', 10, 20, 30)}")
print(f"Multiplicación de 2, 3, 4: {calculadora('multiplicacion', 2, 3, 4)}")
