"""
PYTHON DESDE CERO - LECCIÓN 7: SETS (CONJUNTOS)
================================================

🎯 ¿Qué es un SET (Conjunto)?
-----------------------------
Un set es como una BOLSA MÁGICA donde guardas cosas, pero tiene reglas especiales:

1. NO puede haber DUPLICADOS (elementos repetidos)
   - Si intentas meter 2 manzanas iguales, solo se guarda 1
   
2. NO tiene ORDEN (están mezclados)
   - No puedes decir "dame el primero" porque no hay orden

3. SÍ se puede MODIFICAR (agregar/quitar cosas)
   - Pero no puedes cambiar un elemento por otro

Ejemplo en la vida real:
- Una canasta de frutas sin repetir: {manzana, pera, uva}
- Los estudiantes únicos de una clase (sin duplicados)
- Las letras únicas de una palabra

Los sets se escriben con LLAVES { } y se separan con COMAS
"""

print("=" * 60)
print("🎓 LECCIÓN 7: SETS (CONJUNTOS) EN PYTHON")
print("=" * 60)
print()

# ============================================
# 1️⃣ CREAR SETS
# ============================================
print("=== 1. CÓMO CREAR SETS ===")
print()

# Set de frutas
frutas = {"manzana", "pera", "uva", "naranja"}
print("🍎 Set de frutas:", frutas)

# Set de números
numeros = {5, 10, 15, 20, 25}
print("🔢 Set de números:", numeros)

# ¡OJO! Los duplicados se eliminan automáticamente
numeros_con_duplicados = {1, 2, 3, 2, 1, 4, 3, 5}
print("❗ Con duplicados {1, 2, 3, 2, 1, 4, 3, 5}:")
print("   Se convierte en:", numeros_con_duplicados)
print("   (Los duplicados desaparecieron mágicamente)")
print()

# Set vacío (OJO: NO uses {}, eso es un diccionario)
set_vacio = set()  # ✅ Correcto
print("📭 Set vacío:", set_vacio, type(set_vacio))
print()

# Crear set desde una lista
lista = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
set_desde_lista = set(lista)
print("📝 Crear desde lista:", lista)
print("   Set resultante:", set_desde_lista)
print("   (Eliminó todos los duplicados)")
print()

# Crear set desde una cadena
texto = "Mississippi"
letras_unicas = set(texto.lower())
print(f"📄 Letras únicas en '{texto}':", letras_unicas)
print()

print("-" * 60)
print()


# ============================================
# 2️⃣ CARACTERÍSTICAS IMPORTANTES
# ============================================
print("=== 2. CARACTERÍSTICAS DE LOS SETS ===")
print()

print("🎯 REGLA 1: NO HAY DUPLICADOS")
colores = {"rojo", "azul", "rojo", "verde", "azul"}
print(f"   Intenté crear: {{'rojo', 'azul', 'rojo', 'verde', 'azul'}}")
print(f"   Resultado real: {colores}")
print()

print("🎯 REGLA 2: NO TIENEN ORDEN (ni índices)")
frutas = {"manzana", "pera", "uva"}
print(f"   Set: {frutas}")
print("   ❌ NO puedes hacer: frutas[0]")
print("   ❌ Daría ERROR porque no hay posiciones")
print()

print("🎯 REGLA 3: SON MODIFICABLES")
print("   ✅ Puedes agregar elementos")
print("   ✅ Puedes eliminar elementos")
print("   ❌ Pero NO puedes cambiar un elemento directamente")
print()

print("-" * 60)
print()


# ============================================
# 3️⃣ AGREGAR ELEMENTOS
# ============================================
print("=== 3. AGREGAR ELEMENTOS AL SET ===")
print()

# add() - Agregar un elemento
print("➕ ADD (Agregar un elemento):")
mascotas = {"perro", "gato"}
print(f"   Set original: {mascotas}")

mascotas.add("pájaro")
print(f"   .add('pájaro'): {mascotas}")

mascotas.add("perro")  # Intentar agregar duplicado
print(f"   .add('perro'): {mascotas}")
print("   (No cambió porque 'perro' ya existe)")
print()

# update() - Agregar múltiples elementos
print("➕ UPDATE (Agregar varios elementos):")
colores = {"rojo", "azul"}
print(f"   Set original: {colores}")

colores.update({"verde", "amarillo", "morado"})
print(f"   .update({{'verde', 'amarillo', 'morado'}}): {colores}")

# También funciona con listas
colores.update(["naranja", "rosa"])
print(f"   .update(['naranja', 'rosa']): {colores}")
print()

print("-" * 60)
print()


# ============================================
# 4️⃣ ELIMINAR ELEMENTOS
# ============================================
print("=== 4. ELIMINAR ELEMENTOS DEL SET ===")
print()

# remove() - Eliminar (da error si no existe)
print("🗑️ REMOVE (Eliminar, da error si no existe):")
frutas = {"manzana", "pera", "uva", "naranja"}
print(f"   Set: {frutas}")

frutas.remove("pera")
print(f"   .remove('pera'): {frutas}")
print("   ⚠️ Si intentas .remove('kiwi') → ERROR (porque no existe)")
print()

# discard() - Eliminar (NO da error si no existe)
print("🗑️ DISCARD (Eliminar, NO da error si no existe):")
numeros = {1, 2, 3, 4, 5}
print(f"   Set: {numeros}")

numeros.discard(3)
print(f"   .discard(3): {numeros}")

numeros.discard(100)  # No existe, pero no da error
print(f"   .discard(100): {numeros}")
print("   (100 no existe, pero no causó error)")
print()

# pop() - Eliminar un elemento aleatorio
print("🎲 POP (Eliminar elemento aleatorio):")
letras = {"a", "b", "c", "d", "e"}
print(f"   Set original: {letras}")

eliminado = letras.pop()
print(f"   .pop() → Eliminó '{eliminado}'")
print(f"   Set ahora: {letras}")
print()

# clear() - Vaciar todo
print("🧹 CLEAR (Vaciar todo el set):")
basura = {1, 2, 3, 4, 5}
print(f"   Set: {basura}")
basura.clear()
print(f"   .clear(): {basura}")
print()

print("-" * 60)
print()


# ============================================
# 5️⃣ OPERACIONES DE BÚSQUEDA
# ============================================
print("=== 5. BUSCAR EN SETS ===")
print()

animales = {"perro", "gato", "conejo", "pájaro"}
print(f"🔍 Set de animales: {animales}")
print()

# in - Verificar si existe (SUPER RÁPIDO en sets)
print("✅ VERIFICAR SI EXISTE (in):")
print(f"   'gato' in animales → {'gato' in animales}")
print(f"   'león' in animales → {'león' in animales}")
print()

print("💡 Los sets son MUY RÁPIDOS para buscar")
print("   (Mucho más rápidos que las listas)")
print()

# Longitud
print(f"📏 CANTIDAD: len(animales) = {len(animales)}")
print()

print("-" * 60)
print()


# ============================================
# 6️⃣ OPERACIONES MATEMÁTICAS (¡Lo más cool!)
# ============================================
print("=== 6. OPERACIONES MATEMÁTICAS DE CONJUNTOS ===")
print()

# Datos de ejemplo
grupo_a = {"Ana", "Luis", "María", "Pedro"}
grupo_b = {"María", "Pedro", "Juan", "Sofia"}

print(f"👥 Grupo A: {grupo_a}")
print(f"👥 Grupo B: {grupo_b}")
print()

# UNIÓN - Todos los elementos (sin repetir)
print("➕ UNIÓN (Todos los elementos juntos):")
union = grupo_a | grupo_b  # También: grupo_a.union(grupo_b)
print(f"   A | B = {union}")
print("   (Todos los estudiantes de ambos grupos)")
print()

# INTERSECCIÓN - Solo los que están en ambos
print("🔗 INTERSECCIÓN (Solo los que están en ambos):")
interseccion = grupo_a & grupo_b  # También: grupo_a.intersection(grupo_b)
print(f"   A & B = {interseccion}")
print("   (Estudiantes que están en ambos grupos)")
print()

# DIFERENCIA - Los que están en A pero NO en B
print("➖ DIFERENCIA (En A pero NO en B):")
diferencia = grupo_a - grupo_b  # También: grupo_a.difference(grupo_b)
print(f"   A - B = {diferencia}")
print("   (Estudiantes solo en grupo A)")
print()

# DIFERENCIA SIMÉTRICA - Los que están en uno u otro, pero NO en ambos
print("⚡ DIFERENCIA SIMÉTRICA (En uno u otro, NO en ambos):")
# También: grupo_a.symmetric_difference(grupo_b)
dif_simetrica = grupo_a ^ grupo_b
print(f"   A ^ B = {dif_simetrica}")
print("   (Estudiantes en solo un grupo, no en ambos)")
print()

print("-" * 60)
print()


# ============================================
# 7️⃣ MÉTODOS DE COMPARACIÓN
# ============================================
print("=== 7. COMPARAR SETS ===")
print()

set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}
set_c = {1, 2, 3}

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")
print(f"Set C: {set_c}")
print()

# Subconjunto (subset)
print("📦 SUBCONJUNTO (¿A está contenido en B?):")
print(f"   A <= B → {set_a <= set_b}  (A es subconjunto de B)")
print(f"   B <= A → {set_b <= set_a}  (B NO es subconjunto de A)")
print()

# Superconjunto (superset)
print("📦 SUPERCONJUNTO (¿B contiene a A?):")
print(f"   B >= A → {set_b >= set_a}  (B es superconjunto de A)")
print()

# Igualdad
print("⚖️ IGUALDAD:")
print(f"   A == C → {set_a == set_c}  (A es igual a C)")
print(f"   A == B → {set_a == set_b}  (A NO es igual a B)")
print()

# Disjuntos (no tienen elementos en común)
print("🚫 DISJUNTOS (No tienen elementos comunes):")
set_x = {1, 2, 3}
set_y = {4, 5, 6}
set_z = {3, 4, 5}

print(f"   X: {set_x}, Y: {set_y}")
print(
    f"   X.isdisjoint(Y) → {set_x.isdisjoint(set_y)}  (No comparten elementos)")
print(f"   X.isdisjoint(Z) → {set_x.isdisjoint(set_z)}  (Comparten el 3)")
print()

print("-" * 60)
print()


# ============================================
# 8️⃣ RECORRER SETS
# ============================================
print("=== 8. RECORRER SETS ===")
print()

colores = {"rojo", "azul", "verde", "amarillo"}
print(f"🎨 Set de colores: {colores}")
print()

print("🔁 FOR LOOP:")
for color in colores:
    print(f"   Color: {color}")
print()

print("⚠️ RECUERDA: El orden puede variar cada vez que ejecutes")
print()

print("-" * 60)
print()


# ============================================
# 9️⃣ CONVERSIONES
# ============================================
print("=== 9. CONVERTIR SETS ===")
print()

# Set → Lista
print("📦 → 📝 SET A LISTA:")
set_numeros = {5, 2, 8, 1, 9}
lista_numeros = list(set_numeros)
print(f"   Set: {set_numeros}")
print(f"   Lista: {lista_numeros}")
print()

# Lista → Set (elimina duplicados)
print("📝 → 📦 LISTA A SET (Elimina duplicados):")
lista_con_duplicados = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
set_sin_duplicados = set(lista_con_duplicados)
print(f"   Lista con duplicados: {lista_con_duplicados}")
print(f"   Set sin duplicados: {set_sin_duplicados}")
print()

# Set → Tupla
print("📦 → 📦 SET A TUPLA:")
set_colores = {"rojo", "azul", "verde"}
tupla_colores = tuple(set_colores)
print(f"   Set: {set_colores}")
print(f"   Tupla: {tupla_colores}")
print()

print("-" * 60)
print()


# ============================================
# 🔟 FROZEN SETS (Sets inmutables)
# ============================================
print("=== 10. FROZEN SETS (Sets que no cambian) ===")
print()

print("❄️ FROZEN SET:")
frutas_normal = {"manzana", "pera", "uva"}
frutas_frozen = frozenset({"manzana", "pera", "uva"})

print(f"   Set normal: {frutas_normal} (tipo: {type(frutas_normal).__name__})")
print(f"   Frozen set: {frutas_frozen} (tipo: {type(frutas_frozen).__name__})")
print()

print("   ✅ Set normal: Puedes agregar/eliminar")
print("   ❌ Frozen set: NO puedes modificarlo")
print()

print("💡 ¿Para qué sirve?")
print("   - Se puede usar como llave en diccionarios")
print("   - Se puede poner dentro de otro set")
print()

print("-" * 60)
print()


# ============================================
# 🎯 EJEMPLOS PRÁCTICOS DIVERTIDOS
# ============================================
print("=== 🎯 EJEMPLOS PRÁCTICOS ===")
print()

# 📧 Eliminar emails duplicados
print("📧 ELIMINAR EMAILS DUPLICADOS:")
emails = ["ana@mail.com", "luis@mail.com",
          "ana@mail.com", "maria@mail.com", "luis@mail.com"]
print(f"   Emails originales: {emails}")
emails_unicos = list(set(emails))
print(f"   Emails únicos: {emails_unicos}")
print(f"   Eliminamos {len(emails) - len(emails_unicos)} duplicados")
print()

# 🎮 Jugadores en línea
print("🎮 JUGADORES EN LÍNEA:")
jugadores_servidor1 = {"ProGamer", "MasterX", "Champion", "NinjaKid"}
jugadores_servidor2 = {"MasterX", "LegendKing", "Champion", "DragonSlayer"}

print(f"   Servidor 1: {jugadores_servidor1}")
print(f"   Servidor 2: {jugadores_servidor2}")

todos = jugadores_servidor1 | jugadores_servidor2
print(f"   Todos los jugadores: {todos}")

en_ambos = jugadores_servidor1 & jugadores_servidor2
print(f"   En ambos servidores: {en_ambos}")

solo_servidor1 = jugadores_servidor1 - jugadores_servidor2
print(f"   Solo en servidor 1: {solo_servidor1}")
print()

# 📚 Materias de estudiantes
print("📚 MATERIAS QUE CURSARON:")
materias_juan = {"Matemáticas", "Ciencias", "Historia", "Arte"}
materias_maria = {"Matemáticas", "Música", "Historia", "Deportes"}

print(f"   Juan: {materias_juan}")
print(f"   María: {materias_maria}")

compartidas = materias_juan & materias_maria
print(f"   Materias compartidas: {compartidas}")

solo_juan = materias_juan - materias_maria
print(f"   Solo Juan cursó: {solo_juan}")

solo_maria = materias_maria - materias_juan
print(f"   Solo María cursó: {solo_maria}")
print()

# 🍕 Ingredientes de pizza
print("🍕 INGREDIENTES DISPONIBLES:")
pizza_margarita = {"queso", "tomate", "albahaca"}
pizza_pepperoni = {"queso", "tomate", "pepperoni"}
pizza_hawaiana = {"queso", "tomate", "piña", "jamón"}

todos_ingredientes = pizza_margarita | pizza_pepperoni | pizza_hawaiana
print(f"   Ingredientes necesarios: {todos_ingredientes}")

ingredientes_comunes = pizza_margarita & pizza_pepperoni & pizza_hawaiana
print(f"   En todas las pizzas: {ingredientes_comunes}")
print()

# 🎵 Géneros musicales favoritos
print("🎵 GUSTOS MUSICALES:")
gustos_ana = {"Pop", "Rock", "Jazz"}
gustos_luis = {"Rock", "Electrónica", "Hip Hop"}

print(f"   Ana: {gustos_ana}")
print(f"   Luis: {gustos_luis}")

generos_comunes = gustos_ana & gustos_luis
print(f"   Les gusta a ambos: {generos_comunes}")

if generos_comunes:
    print(f"   ✅ ¡Tienen gustos en común!")
else:
    print(f"   ❌ No tienen gustos en común")
print()

# 📖 Palabras únicas en un texto
print("📖 CONTAR PALABRAS ÚNICAS:")
texto = "el gato y el perro juegan el gato corre y el perro ladra"
palabras = texto.split()
palabras_unicas = set(palabras)

print(f"   Texto: '{texto}'")
print(f"   Total palabras: {len(palabras)}")
print(f"   Palabras únicas: {palabras_unicas}")
print(f"   Cantidad única: {len(palabras_unicas)}")
print()

# 🎯 Tags/Etiquetas de artículos
print("🏷️ SISTEMA DE ETIQUETAS:")
articulo1_tags = {"python", "programación", "tutorial", "básico"}
articulo2_tags = {"python", "avanzado", "programación", "desarrollo"}

print(f"   Artículo 1: {articulo1_tags}")
print(f"   Artículo 2: {articulo2_tags}")

todas_tags = articulo1_tags | articulo2_tags
print(f"   Todas las tags: {todas_tags}")

tags_relacionadas = articulo1_tags & articulo2_tags
print(f"   Tags relacionadas: {tags_relacionadas}")
print()

# 🎲 Números ganadores de lotería
print("🎲 LOTERÍA - NÚMEROS ÚNICOS:")
numeros_jugador = {5, 12, 23, 34, 45, 5, 12}  # Intentó repetir
numeros_ganadores = {12, 23, 30, 45, 50}

print(f"   Mis números: {numeros_jugador}")
print(f"   Números ganadores: {numeros_ganadores}")

aciertos = numeros_jugador & numeros_ganadores
print(f"   ✅ Acerté: {aciertos}")
print(f"   Total aciertos: {len(aciertos)}")
print()

# 🎨 Mezclar paletas de colores
print("🎨 PALETAS DE COLORES:")
paleta_calida = {"rojo", "naranja", "amarillo"}
paleta_fria = {"azul", "verde", "morado"}

print(f"   Cálida: {paleta_calida}")
print(f"   Fría: {paleta_fria}")

colores_totales = paleta_calida | paleta_fria
print(f"   Todos los colores: {colores_totales}")

# Verificar que no se mezclan
no_mezclados = paleta_calida.isdisjoint(paleta_fria)
print(f"   ¿Son disjuntos? {no_mezclados} (No comparten colores)")
print()

# 📱 Contactos en múltiples redes sociales
print("📱 CONTACTOS EN REDES SOCIALES:")
contactos_facebook = {"Ana", "Luis", "María", "Pedro", "Juan"}
contactos_instagram = {"María", "Pedro", "Sofia", "Carlos"}
contactos_twitter = {"Luis", "Pedro", "Juan", "Diana"}

print(f"   Facebook: {contactos_facebook}")
print(f"   Instagram: {contactos_instagram}")
print(f"   Twitter: {contactos_twitter}")

en_todas_redes = contactos_facebook & contactos_instagram & contactos_twitter
print(f"   En todas las redes: {en_todas_redes}")

total_contactos = contactos_facebook | contactos_instagram | contactos_twitter
print(f"   Total de contactos únicos: {len(total_contactos)}")
print()

print("=" * 60)
print("🎉 ¡Felicidades! Ya dominas los Sets en Python 🎉")
print("=" * 60)
print()
print("📌 RESUMEN:")
print("   - Sets = Colecciones sin duplicados")
print("   - Se crean con llaves: {1, 2, 3}")
print("   - NO tienen orden ni índices")
print("   - Perfectos para eliminar duplicados")
print("   - Operaciones: unión (|), intersección (&), diferencia (-)")
print("   - Muy rápidos para buscar elementos")
print("=" * 60)
