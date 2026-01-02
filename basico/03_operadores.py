"""
PYTHON DESDE CERO - LECCIÓN 3: OPERADORES
==========================================

🎯 ¿Qué son los OPERADORES?
---------------------------
Los operadores son símbolos que le dicen a Python qué hacer con los datos.
Son como los botones de una calculadora: +, -, ×, ÷

Imagina que tienes bloques de LEGO y los operadores te dicen:
- Junta estos bloques (+)
- Separa estos bloques (-)
- Haz copias de estos bloques (*)
- Divide estos bloques entre amigos (/)
"""

print("=" * 50)
print("🎓 LECCIÓN 3: OPERADORES EN PYTHON")
print("=" * 50)
print()

# ============================================
# 1️⃣ OPERADORES ARITMÉTICOS (Matemáticas)
# ============================================
print("=== 1. OPERADORES ARITMÉTICOS ===")
print("(Son como hacer matemáticas en clase)")
print()

# ➕ SUMA - Juntar cosas
manzanas = 5
naranjas = 3
frutas_totales = manzanas + naranjas
print("➕ SUMA: Tengo", manzanas, "manzanas y", naranjas, "naranjas")
print("   En total tengo", frutas_totales, "frutas")
print()

# ➖ RESTA - Quitar cosas
dinero = 100
gasto = 35
dinero_restante = dinero - gasto
print("➖ RESTA: Tenía $", dinero, "y gasté $", gasto)
print("   Me quedan $", dinero_restante)
print()

# ✖️ MULTIPLICACIÓN - Repetir varias veces
cajas = 4
galletas_por_caja = 6
galletas_totales = cajas * galletas_por_caja
print("✖️ MULTIPLICACIÓN:", cajas, "cajas con",
      galletas_por_caja, "galletas cada una")
print("   Total:", galletas_totales, "galletas")
print()

# ➗ DIVISIÓN - Repartir entre varios
pizza_porciones = 12
amigos = 4
porciones_cada_uno = pizza_porciones / amigos
print("➗ DIVISIÓN: Hay", pizza_porciones, "porciones para", amigos, "amigos")
print("   Cada uno recibe", porciones_cada_uno, "porciones")
print()

# // DIVISIÓN ENTERA - División sin decimales
dulces = 10
niños = 3
dulces_por_niño = dulces // niños
print("// DIVISIÓN ENTERA:", dulces, "dulces entre", niños, "niños")
print("   Cada niño recibe", dulces_por_niño, "dulces completos")
print()

# % MÓDULO (RESIDUO) - Lo que sobra de una división
dulces_sobrantes = dulces % niños
print("% MÓDULO (lo que sobra):", dulces, "dulces entre", niños, "niños")
print("   Sobran", dulces_sobrantes, "dulces")
print()

# ** POTENCIA - Multiplicar un número por sí mismo varias veces
base = 2
exponente = 3
resultado = base ** exponente
print("** POTENCIA:", base, "elevado a", exponente)
print("   Es como decir:", base, "×", base, "×", base, "=", resultado)
print()

print("-" * 50)
print()


# ============================================
# 2️⃣ OPERADORES DE COMPARACIÓN
# ============================================
print("=== 2. OPERADORES DE COMPARACIÓN ===")
print("(Comparamos dos cosas y la respuesta es True o False)")
print()

mi_edad = 10
edad_hermano = 12

# == IGUAL A
print("== IGUAL A")
print("¿Tengo la misma edad que mi hermano?", mi_edad,
      "==", edad_hermano, "→", mi_edad == edad_hermano)
print()

# != DIFERENTE DE (NO IGUAL)
print("!= DIFERENTE DE")
print("¿Tengo diferente edad que mi hermano?", mi_edad,
      "!=", edad_hermano, "→", mi_edad != edad_hermano)
print()

# > MAYOR QUE
print("> MAYOR QUE")
print("¿Soy mayor que mi hermano?", mi_edad, ">",
      edad_hermano, "→", mi_edad > edad_hermano)
print()

# < MENOR QUE
print("< MENOR QUE")
print("¿Soy menor que mi hermano?", mi_edad, "<",
      edad_hermano, "→", mi_edad < edad_hermano)
print()

# >= MAYOR O IGUAL QUE
puntos_yo = 85
puntos_pasar = 80
print(">= MAYOR O IGUAL QUE")
print("¿Tengo suficientes puntos para pasar?", puntos_yo,
      ">=", puntos_pasar, "→", puntos_yo >= puntos_pasar)
print()

# <= MENOR O IGUAL QUE
temperatura = 25
temperatura_maxima = 30
print("<= MENOR O IGUAL QUE")
print("¿La temperatura está bien?", temperatura, "<=",
      temperatura_maxima, "→", temperatura <= temperatura_maxima)
print()

print("-" * 50)
print()


# ============================================
# 3️⃣ OPERADORES LÓGICOS
# ============================================
print("=== 3. OPERADORES LÓGICOS ===")
print("(Combinan condiciones - like making decisions)")
print()

# AND - Las DOS cosas deben ser verdad
tengo_dinero = True
tienda_abierta = True
puedo_comprar = tengo_dinero and tienda_abierta
print("🛒 AND (Y) - Las DOS condiciones deben ser verdad")
print("   ¿Tengo dinero?", tengo_dinero)
print("   ¿La tienda está abierta?", tienda_abierta)
print("   ¿Puedo comprar?", puedo_comprar)
print("   (Solo SI tengo dinero Y la tienda está abierta)")
print()

# Otro ejemplo de AND
hice_tarea = True
me_porte_bien = False
puedo_jugar = hice_tarea and me_porte_bien
print("🎮 AND - Otro ejemplo")
print("   ¿Hice mi tarea?", hice_tarea)
print("   ¿Me porté bien?", me_porte_bien)
print("   ¿Puedo jugar videojuegos?", puedo_jugar)
print("   (Necesito hacer AMBAS cosas)")
print()

# OR - Al menos UNA cosa debe ser verdad
es_sabado = False
es_domingo = True
es_fin_semana = es_sabado or es_domingo
print("🌞 OR (O) - Al menos UNA condición debe ser verdad")
print("   ¿Es sábado?", es_sabado)
print("   ¿Es domingo?", es_domingo)
print("   ¿Es fin de semana?", es_fin_semana)
print("   (Es fin de semana si es sábado O domingo)")
print()

# NOT - Invierte el valor (verdadero ↔ falso)
esta_lloviendo = False
puedo_salir = not esta_lloviendo
print("☀️ NOT (NO) - Invierte el valor")
print("   ¿Está lloviendo?", esta_lloviendo)
print("   ¿Puedo salir a jugar?", puedo_salir)
print("   (Puedo salir si NO está lloviendo)")
print()

print("-" * 50)
print()


# ============================================
# 4️⃣ OPERADORES DE ASIGNACIÓN
# ============================================
print("=== 4. OPERADORES DE ASIGNACIÓN ===")
print("(Formas rápidas de cambiar el valor de variables)")
print()

# = ASIGNACIÓN NORMAL
puntos = 0
print("= ASIGNACIÓN: puntos =", puntos)
print()

# += SUMAR Y ASIGNAR
puntos += 10  # Es lo mismo que: puntos = puntos + 10
print("+= SUMAR Y ASIGNAR: Gané 10 puntos")
print("   Ahora tengo", puntos, "puntos")
print()

puntos += 5
print("+= Gané 5 puntos más")
print("   Ahora tengo", puntos, "puntos")
print()

# -= RESTAR Y ASIGNAR
puntos -= 3  # Es lo mismo que: puntos = puntos - 3
print("-= RESTAR Y ASIGNAR: Perdí 3 puntos")
print("   Ahora tengo", puntos, "puntos")
print()

# *= MULTIPLICAR Y ASIGNAR
monedas = 5
print("Tengo", monedas, "monedas")
monedas *= 2  # Es lo mismo que: monedas = monedas * 2
print("*= MULTIPLICAR Y ASIGNAR: ¡Bonus! Se duplicaron")
print("   Ahora tengo", monedas, "monedas")
print()

# /= DIVIDIR Y ASIGNAR
dulces = 20
print("Tengo", dulces, "dulces")
dulces /= 4  # Es lo mismo que: dulces = dulces / 4
print("/= DIVIDIR Y ASIGNAR: Los repartí entre 4 personas")
print("   Me quedaron", dulces, "dulces")
print()

print("-" * 50)
print()


# ============================================
# 🎯 EJEMPLOS PRÁCTICOS DIVERTIDOS
# ============================================
print("=== 🎯 EJEMPLOS PRÁCTICOS ===")
print()

# 🎮 Juego de puntos
print("🎮 SISTEMA DE PUNTOS DE UN JUEGO:")
puntaje = 0
print("Inicio del juego:", puntaje)

puntaje += 100
print("¡Derrotaste un enemigo! +100 →", puntaje)

puntaje += 50
print("¡Recogiste una moneda! +50 →", puntaje)

puntaje *= 2
print("¡BONUS x2! →", puntaje)

puntaje -= 20
print("Te golpearon -20 →", puntaje)

print("Puntaje final:", puntaje)
print()

# 🎂 Verificar si puede entrar a una montaña rusa
print("🎢 MONTAÑA RUSA:")
altura = 145  # en centímetros
altura_minima = 140
edad = 12
edad_minima = 10

puede_subir = (altura >= altura_minima) and (edad >= edad_minima)
print("Altura del niño:", altura, "cm (mínimo:", altura_minima, "cm)")
print("Edad del niño:", edad, "años (mínimo:", edad_minima, "años)")
print("¿Puede subir a la montaña rusa?", puede_subir)
print()

# 🏆 Sistema de calificaciones
print("🏆 CALIFICACIONES:")
nota1 = 85
nota2 = 90
nota3 = 78

promedio = (nota1 + nota2 + nota3) / 3
aprobo = promedio >= 70
es_excelente = promedio >= 90

print("Notas:", nota1, ",", nota2, ",", nota3)
print("Promedio:", round(promedio, 2))  # round() redondea a 2 decimales
print("¿Aprobó?", aprobo, "(necesita al menos 70)")
print("¿Es excelente?", es_excelente, "(necesita al menos 90)")
print()

# 🍕 Calculadora de propinas
print("💰 CALCULADORA DE PROPINA:")
cuenta_restaurante = 150
porcentaje_propina = 10
propina = cuenta_restaurante * porcentaje_propina / 100
total = cuenta_restaurante + propina

print("Cuenta:", "$", cuenta_restaurante)
print("Propina (", porcentaje_propina, "%):", "$", propina)
print("Total a pagar:", "$", total)
print()

# 🎲 Par o impar
print("🎲 ¿PAR O IMPAR?")
numero = 17
es_par = (numero % 2) == 0  # Si el residuo de dividir entre 2 es 0, es par
es_impar = not es_par

print("Número:", numero)
print("¿Es par?", es_par)
print("¿Es impar?", es_impar)
print("(Truco: Si el residuo de dividir entre 2 es 0, es par)")
print()

print("=" * 50)
print("🎉 ¡Felicidades! Ya sabes usar operadores en Python 🎉")
print("=" * 50)
