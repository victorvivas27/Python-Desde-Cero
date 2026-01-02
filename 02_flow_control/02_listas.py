# ==========================================================
# LISTAS EN PYTHON (list)
# ==========================================================
# Una lista es una colección:
# - Ordenada: mantiene el orden de inserción.
# - Mutable: se puede modificar (cambiar, agregar, borrar).
# - Heterogénea: puede contener distintos tipos de datos.
#
# Se define con corchetes [] y los elementos se separan por comas.
# ==========================================================


# ----------------------------------------------------------
# CREAR LISTAS
# ----------------------------------------------------------
mi_lista = [1, 2, 3, 2, 4, 6, 3]      # Lista de enteros (puede tener repetidos)
mi_lista2 = [1, 2.3, "hola"]          # Lista con tipos mezclados (int, float, str)
mi_lista3 = []                        # Lista vacía (en tu código decía "bacia", es "vacía")
mi_lista4 = [[1, 2], [3, 4]]          # Lista anidada (lista dentro de otra)
matrix = [                            # Ejemplo de matriz 3x3 usando lista de listas
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Lista 1:", mi_lista)
print("Lista 2:", mi_lista2)
print("Lista 3:", mi_lista3)
print("Lista 4:", mi_lista4)
print("Matriz:", matrix)


# ----------------------------------------------------------
# ACCEDER A ELEMENTOS (INDEXING)
# ----------------------------------------------------------
# Los índices en Python empiezan en 0:
# - índice 0 -> primer elemento
# - índice 1 -> segundo elemento
# - ...
#
# También se permiten índices negativos:
# - índice -1 -> último elemento
# - índice -2 -> anteúltimo, etc.
primer_elemento = mi_lista[0]     # Acceder al primer elemento
ultimo_elemento = mi_lista[-1]    # Acceder al último elemento

print("Primer elemento de mi_lista:", primer_elemento)
print("Último elemento de mi_lista:", ultimo_elemento)


# ----------------------------------------------------------
# ACCEDER A ELEMENTOS EN LISTAS ANIDADAS
# ----------------------------------------------------------
# mi_lista4 = [[1, 2], [3, 4]]
#             0       1
# mi_lista4[1] -> [3, 4]
# mi_lista4[1][0] -> 3
elemento_anidado = mi_lista4[1][0]
print("Elemento anidado de mi_lista4:", elemento_anidado)


# ==========================================================
# SLICING (REBANADO) DE LISTAS
# ==========================================================
# El slicing permite obtener una "sublista" usando rangos.
#
# Sintaxis:
# lista[inicio:fin:paso]
#
# - inicio: índice donde empieza (incluido)
# - fin:    índice donde termina (EXCLUÍDO)
# - paso:   cada cuántos elementos tomar
#
# Si omites inicio -> empieza desde 0
# Si omites fin    -> llega hasta el final
# ==========================================================

mi_lista = [1, 2, 3, 2, 4, 6, 3]


# ----------------------------------------------------------
# EJEMPLO: Desde el índice 2 hasta el índice 3 (excluye 3)
# ----------------------------------------------------------
# Esto NO son "los primeros tres".
# Es solo una porción: [mi_lista[2]]
# índice 2 -> 3
primeros_tres = mi_lista[2:3]
print("mi_lista[2:3] (solo un elemento):", primeros_tres)


# ----------------------------------------------------------
# PRIMEROS TRES ELEMENTOS
# ----------------------------------------------------------
primeros_tres = mi_lista[:3]   # índices 0,1,2
print("Primeros tres elementos de mi_lista:", primeros_tres)


# ----------------------------------------------------------
# ÚLTIMOS TRES ELEMENTOS
# ----------------------------------------------------------
ultimos_tres = mi_lista[-3:]   # toma los últimos 3
print("Últimos tres elementos de mi_lista:", ultimos_tres)


# ----------------------------------------------------------
# COPIA DE UNA LISTA CON SLICING
# ----------------------------------------------------------
# Esto crea una nueva lista con los mismos elementos.
copia_lista = mi_lista[:]
print("Copia de mi_lista:", copia_lista)


# ----------------------------------------------------------
# SLICING CON PASO (::)
# ----------------------------------------------------------
# mi_lista[::2] -> toma desde el inicio hasta el final, saltando de 2 en 2
# OJO: no significa "posiciones pares" del número, sino índices pares (0,2,4,...)
lista_paso_dos = mi_lista[::2]
print("Elementos de mi_lista con paso de 2:", lista_paso_dos)

# Paso 3: índices 0,3,6,...
lista_paso_tres = mi_lista[::3]
print("Elementos de mi_lista con paso de 3:", lista_paso_tres)


# ----------------------------------------------------------
# LISTA INVERTIDA CON SLICING
# ----------------------------------------------------------
# paso negativo (-1) recorre al revés
lista_invertida = mi_lista[::-1]
print("Lista invertida:", lista_invertida)


# ==========================================================
# MODIFICAR ELEMENTOS (MUTABILIDAD)
# ==========================================================
# Como la lista es mutable, puedes cambiar un elemento por índice.
# ==========================================================

mi_lista[0] = 10
print("Lista modificada:", mi_lista)

# Si intentas asignar a un índice que NO existe, da IndexError.
# mi_lista[10] = 20  # IndexError: list assignment index out of range


# ==========================================================
# AÑADIR ELEMENTOS A UNA LISTA
# ==========================================================
# Métodos comunes:
# - append(x): agrega x al final (1 solo elemento)
# - insert(i, x): inserta x en la posición i
# - extend(iterable): agrega varios elementos al final
# ==========================================================

mi_lista.append(7)                 # Agrega 7 al final
print("Lista con el elemento 7:", mi_lista)

mi_lista.insert(1, 5)              # Inserta 5 en el índice 1 (desplaza lo demás)
print("Lista con el elemento 5 en la posición 1:", mi_lista)

mi_lista.extend([8, 9])            # Agrega varios elementos
print("Lista con los elementos 8 y 9:", mi_lista)


# ==========================================================
# CONCATENAR LISTAS
# ==========================================================
# Dos formas comunes:
# 1) Nueva lista (menos eficiente si la haces muchas veces):
#    lista_nueva = lista_a + lista_b
#
# 2) Modificar la lista existente (más eficiente en general):
#    lista_a += lista_b
#    (equivalente a extend)
# ==========================================================

otra_lista = [10, 11, 12]

# Menos eficiente si se repite muchas veces, porque crea una lista nueva
lista_concatenada = mi_lista + otra_lista
print("Lista concatenada (crea nueva lista):", lista_concatenada)

# Más eficiente: modifica mi_lista directamente (como extend)
mi_lista += otra_lista
print("mi_lista después de concatenar otra_lista:", mi_lista)

#=========================================================
#Largo de una lista
#=========================================================
#La función len() devuelve el número de elementos en una lista.

print("Largo de mi_lista:", len(mi_lista))