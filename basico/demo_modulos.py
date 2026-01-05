"""
DEMO - Usando Módulos Personalizados
"""

from utilidades import saludar
from operaciones import sumar, multiplicar
import utilidades
import operaciones
print("=" * 60)
print("📦 DEMO DE MÓDULOS PERSONALIZADOS")
print("=" * 60)
print()

# Importar nuestros módulos personalizados

# Probar módulo operaciones
print("🔢 USANDO MÓDULO 'operaciones':")
print(f"   5 + 3 = {operaciones.sumar(5, 3)}")
print(f"   10 - 4 = {operaciones.restar(10, 4)}")
print(f"   6 × 7 = {operaciones.multiplicar(6, 7)}")
print(f"   20 ÷ 4 = {operaciones.dividir(20, 4)}")
print(f"   2^5 = {operaciones.potencia(2, 5)}")
print(f"   ¿8 es par? {operaciones.es_par(8)}")
print()

# Probar módulo utilidades
print("🛠️ USANDO MÓDULO 'utilidades':")
print(f"   {utilidades.saludar('Ana')}")
print(f"   {utilidades.despedirse('Luis')}")

notas = [85, 90, 88, 92]
print(f"   Promedio de {notas}: {utilidades.calcular_promedio(notas):.1f}")

texto = "Python es genial"
print(f"   Vocales en '{texto}': {utilidades.contar_vocales(texto)}")

palabra = "Hola"
print(f"   '{palabra}' invertido: {utilidades.invertir_texto(palabra)}")
print()

# Importar funciones específicas
print("📌 USANDO 'from ... import':")

print(f"   sumar(10, 20) = {sumar(10, 20)}")
print(f"   multiplicar(5, 6) = {multiplicar(5, 6)}")
print(f"   {saludar('Mundo')}")
print()

print("=" * 60)
print("✅ ¡Módulos personalizados funcionando!")
print("=" * 60)
