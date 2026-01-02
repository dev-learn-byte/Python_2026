"""
Programación Orientada a Objetos (POO)
Aprende los conceptos fundamentales de POO en Python
"""

# ============================================
# 1. CLASES Y OBJETOS BÁSICOS
# ============================================
print("=== CLASES Y OBJETOS BÁSICOS ===")

class Persona:
    """Clase básica que representa una persona"""
    
    def __init__(self, nombre, edad):
        """Constructor de la clase"""
        self.nombre = nombre
        self.edad = edad
    
    def saludar(self):
        """Método de instancia"""
        return f"Hola, soy {self.nombre} y tengo {self.edad} años"

# Crear objetos (instancias)
persona1 = Persona("Juan", 25)
persona2 = Persona("María", 30)

print(persona1.saludar())
print(persona2.saludar())

# ============================================
# 2. ATRIBUTOS DE CLASE VS INSTANCIA
# ============================================
print("\n=== ATRIBUTOS DE CLASE VS INSTANCIA ===")

class Estudiante:
    """Clase con atributos de clase e instancia"""
    
    # Atributo de clase (compartido por todas las instancias)
    universidad = "Universidad Nacional"
    total_estudiantes = 0
    
    def __init__(self, nombre, carrera):
        # Atributos de instancia (únicos para cada instancia)
        self.nombre = nombre
        self.carrera = carrera
        Estudiante.total_estudiantes += 1
    
    def presentarse(self):
        return f"Soy {self.nombre}, estudio {self.carrera} en {self.universidad}"

est1 = Estudiante("Ana", "Ingeniería")
est2 = Estudiante("Carlos", "Medicina")

print(est1.presentarse())
print(est2.presentarse())
print(f"Total de estudiantes: {Estudiante.total_estudiantes}")

# ============================================
# 3. ENCAPSULACIÓN (PÚBLICO, PROTEGIDO, PRIVADO)
# ============================================
print("\n=== ENCAPSULACIÓN ===")

class CuentaBancaria:
    """Clase que demuestra encapsulación"""
    
    def __init__(self, titular, saldo_inicial):
        self.titular = titular          # Público
        self._saldo = saldo_inicial     # Protegido (por convención)
        self.__pin = "1234"             # Privado (name mangling)
    
    def depositar(self, cantidad):
        """Método público para depositar"""
        if cantidad > 0:
            self._saldo += cantidad
            return f"Depósito exitoso. Nuevo saldo: ${self._saldo}"
        return "Cantidad inválida"
    
    def retirar(self, cantidad, pin):
        """Método público para retirar"""
        if pin != self.__pin:
            return "PIN incorrecto"
        if cantidad > 0 and cantidad <= self._saldo:
            self._saldo -= cantidad
            return f"Retiro exitoso. Nuevo saldo: ${self._saldo}"
        return "Fondos insuficientes o cantidad inválida"
    
    def consultar_saldo(self):
        """Método público para consultar saldo"""
        return f"Saldo actual: ${self._saldo}"

cuenta = CuentaBancaria("Pedro", 1000)
print(cuenta.consultar_saldo())
print(cuenta.depositar(500))
print(cuenta.retirar(200, "1234"))

# ============================================
# 4. HERENCIA
# ============================================
print("\n=== HERENCIA ===")

class Animal:
    """Clase base (padre)"""
    
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie
    
    def hacer_sonido(self):
        return "Algún sonido"
    
    def describir(self):
        return f"{self.nombre} es un {self.especie}"

class Perro(Animal):
    """Clase derivada (hijo)"""
    
    def __init__(self, nombre, raza):
        super().__init__(nombre, "Perro")  # Llamar al constructor padre
        self.raza = raza
    
    def hacer_sonido(self):
        """Sobrescribir método del padre"""
        return "¡Guau guau!"
    
    def mover_cola(self):
        """Método propio de la clase Perro"""
        return f"{self.nombre} está moviendo la cola"

class Gato(Animal):
    """Otra clase derivada"""
    
    def __init__(self, nombre, color):
        super().__init__(nombre, "Gato")
        self.color = color
    
    def hacer_sonido(self):
        return "¡Miau!"

perro = Perro("Max", "Labrador")
gato = Gato("Mishi", "Naranja")

print(perro.describir())
print(perro.hacer_sonido())
print(perro.mover_cola())

print(gato.describir())
print(gato.hacer_sonido())

# ============================================
# 5. POLIMORFISMO
# ============================================
print("\n=== POLIMORFISMO ===")

def hacer_hablar_animal(animal):
    """Función que demuestra polimorfismo"""
    print(f"{animal.nombre} dice: {animal.hacer_sonido()}")

animales = [
    Perro("Rocky", "Pastor Alemán"),
    Gato("Luna", "Blanco"),
    Perro("Toby", "Chihuahua")
]

print("Los animales hablan:")
for animal in animales:
    hacer_hablar_animal(animal)

# ============================================
# 6. MÉTODOS ESPECIALES (MAGIC METHODS)
# ============================================
print("\n=== MÉTODOS ESPECIALES ===")

class Libro:
    """Clase que demuestra métodos especiales"""
    
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
    
    def __str__(self):
        """Representación en string para usuarios"""
        return f"'{self.titulo}' por {self.autor}"
    
    def __repr__(self):
        """Representación en string para desarrolladores"""
        return f"Libro('{self.titulo}', '{self.autor}', {self.paginas})"
    
    def __len__(self):
        """Retorna la longitud (páginas)"""
        return self.paginas
    
    def __eq__(self, otro):
        """Comparar libros por título"""
        return self.titulo == otro.titulo

libro1 = Libro("Don Quijote", "Cervantes", 863)
libro2 = Libro("Cien años de soledad", "García Márquez", 417)

print(f"Libro: {libro1}")
print(f"Representación: {repr(libro1)}")
print(f"Páginas: {len(libro1)}")
print(f"¿Son iguales libro1 y libro2?: {libro1 == libro2}")

# ============================================
# 7. PROPIEDADES (@property)
# ============================================
print("\n=== PROPIEDADES ===")

class Rectangulo:
    """Clase que demuestra el uso de propiedades"""
    
    def __init__(self, ancho, alto):
        self._ancho = ancho
        self._alto = alto
    
    @property
    def ancho(self):
        """Getter para ancho"""
        return self._ancho
    
    @ancho.setter
    def ancho(self, valor):
        """Setter para ancho con validación"""
        if valor > 0:
            self._ancho = valor
        else:
            raise ValueError("El ancho debe ser positivo")
    
    @property
    def area(self):
        """Propiedad calculada (solo lectura)"""
        return self._ancho * self._alto

rect = Rectangulo(5, 3)
print(f"Ancho: {rect.ancho}")
print(f"Área: {rect.area}")

rect.ancho = 10
print(f"Nuevo ancho: {rect.ancho}")
print(f"Nueva área: {rect.area}")

# ============================================
# 8. MÉTODOS ESTÁTICOS Y DE CLASE
# ============================================
print("\n=== MÉTODOS ESTÁTICOS Y DE CLASE ===")

class Calculadora:
    """Clase con métodos estáticos y de clase"""
    
    version = "1.0"
    
    @staticmethod
    def sumar(a, b):
        """Método estático (no necesita acceso a la instancia)"""
        return a + b
    
    @classmethod
    def obtener_version(cls):
        """Método de clase (accede a atributos de clase)"""
        return f"Calculadora versión {cls.version}"

print(f"Suma: {Calculadora.sumar(5, 3)}")
print(Calculadora.obtener_version())

# ============================================
# 9. EJERCICIO PRÁCTICO
# ============================================
print("\n=== EJERCICIO: SISTEMA DE VEHÍCULOS ===")

class Vehiculo:
    """Clase base para vehículos"""
    
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.encendido = False
    
    def encender(self):
        self.encendido = True
        return f"{self.marca} {self.modelo} encendido"
    
    def apagar(self):
        self.encendido = False
        return f"{self.marca} {self.modelo} apagado"

class Coche(Vehiculo):
    def __init__(self, marca, modelo, año, num_puertas):
        super().__init__(marca, modelo, año)
        self.num_puertas = num_puertas
    
    def describir(self):
        return f"Coche {self.marca} {self.modelo} ({self.año}) con {self.num_puertas} puertas"

class Moto(Vehiculo):
    def __init__(self, marca, modelo, año, tipo):
        super().__init__(marca, modelo, año)
        self.tipo = tipo
    
    def describir(self):
        return f"Moto {self.tipo} {self.marca} {self.modelo} ({self.año})"

coche = Coche("Toyota", "Corolla", 2020, 4)
moto = Moto("Honda", "CBR", 2021, "Deportiva")

print(coche.describir())
print(coche.encender())

print(moto.describir())
print(moto.encender())
