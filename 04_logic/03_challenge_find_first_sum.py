# ----------------------------------------------------------
# LIMPIAR LA CONSOLA (OPCIONAL)
# ----------------------------------------------------------
import os
os.system('clear')  # En Windows suele usarse 'cls'


# ==========================================================
# EJERCICIO: ENCONTRAR DOS NÚMEROS QUE SUMEN UN OBJETIVO
# ==========================================================
# Dado:
# - Una lista de números enteros
# - Un número objetivo (goal)
#
# Objetivo:
# - Encontrar los DOS PRIMEROS números de la lista
#   cuya suma sea igual a goal
# - Devolver sus índices
# - Si no existe una combinación válida, devolver None
#
# Ejemplo:
# nums = [4, 5, 6, 2]
# goal = 8
# Resultado esperado: [2, 3]  -> 6 + 2 = 8
# ==========================================================


def find_first_sum(nums, goal):
    """
    Busca los índices de los dos primeros elementos cuya
    suma sea igual al valor objetivo (goal).

    Parameters
    ----------
    nums : list[int]
        Lista de números enteros.
    goal : int
        Valor objetivo que deben sumar dos elementos.

    Returns
    -------
    list[int] | None
        - [i, j] si se encuentra una combinación válida
        - None si no existe ninguna combinación
    """

    # ------------------------------------------------------
    # BUCLE EXTERNO
    # ------------------------------------------------------
    # Recorre la lista tomando un elemento a la vez.
    # La variable 'i' representa el índice del PRIMER número.
    #
    # Ejemplo:
    # nums = [4, 5, 6, 2]
    #
    # Iteraciones del bucle externo:
    # i = 0 -> nums[i] = 4
    # i = 1 -> nums[i] = 5
    # i = 2 -> nums[i] = 6
    # i = 3 -> nums[i] = 2
    for i in range(len(nums)):

        # --------------------------------------------------
        # BUCLE INTERNO
        # --------------------------------------------------
        # Comienza desde i + 1 para:
        # - No repetir el mismo elemento (evitar i == j)
        # - No evaluar combinaciones duplicadas
        #
        # Ejemplo cuando i = 0:
        # j = 1 -> nums[j] = 5  -> 4 + 5
        # j = 2 -> nums[j] = 6  -> 4 + 6
        # j = 3 -> nums[j] = 2  -> 4 + 2
        #
        # Ejemplo cuando i = 2:
        # j = 3 -> nums[j] = 2  -> 6 + 2 ✔
        for j in range(i + 1, len(nums)):

            # ----------------------------------------------
            # COMPROBACIÓN DE LA SUMA
            # ----------------------------------------------
            # Si la suma de los valores en las posiciones
            # i y j es igual a goal, devolvemos los índices.
            if nums[i] + nums[j] == goal:
                return [i, j]

    # ------------------------------------------------------
    # Si el bucle termina y no se encontró ninguna combinación
    # válida, se devuelve None
    # ------------------------------------------------------
    return None


# ==========================================================
# PRUEBA DE LA FUNCIÓN
# ==========================================================
nums = [4, 5, 6, 2]
goal = 8

# ==========================================================
# EJERCICIO: ENCONTRAR DOS NÚMEROS QUE SUMEN UN OBJETIVO
# (SOLUCIÓN OPTIMIZADA CON DICCIONARIO)
# ==========================================================
# Esta versión utiliza un diccionario para reducir
# la complejidad del algoritmo.
#
# En lugar de comparar todos con todos (O(n²)),
# recorremos la lista una sola vez (O(n)).
# ==========================================================

def find_first_sum_dict(nums, goal):
    """
    Encuentra los índices del PRIMER par de números cuya
    suma sea igual al valor objetivo (goal), usando
    un diccionario para optimizar la búsqueda.

    Parameters
    ----------
    nums : list[int]
        Lista de números enteros.
    goal : int
        Valor objetivo que deben sumar dos elementos.

    Returns
    -------
    list[int] | None
        - [indice_1, indice_2] si se encuentra una combinación válida
        - None si no existe ninguna combinación
    """

    # ------------------------------------------------------
    # Diccionario auxiliar
    # ------------------------------------------------------
    # Guarda:
    #   clave   -> número ya visto
    #   valor   -> índice donde apareció
    #
    # Ejemplo:
    # seen = {4: 0, 5: 1}
    seen = {}

    # ------------------------------------------------------
    # Recorremos la lista UNA sola vez
    # ------------------------------------------------------
    for index, value in enumerate(nums):

        # Calculamos el complemento necesario
        # para llegar al objetivo
        complement = goal - value

        # ----------------------------------------------
        # ¿El complemento ya fue visto?
        # ----------------------------------------------
        if complement in seen:
            # Si existe, encontramos la suma
            # Devolvemos los índices
            return [seen[complement], index]

        # Si no existe, guardamos el número actual
        # junto con su índice
        seen[value] = index

    # Si termina el bucle sin encontrar combinación
    return None


# ==========================================================
# PRUEBA DE LA FUNCIÓN
# ==========================================================
numeros = [4, 5, 6, 2, 8, 3, 5, 7, 1]
objetivo = 8

print(find_first_sum_dict(numeros, objetivo))
