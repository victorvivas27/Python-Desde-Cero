# ----------------------------------------------------------
# LIMPIAR LA CONSOLA (OPCIONAL)
# ----------------------------------------------------------
import os
os.system('clear')  # En Windows suele usarse 'cls'


# ==========================================================
# EJERCICIO: HUEVOS DE DINOSAURIOS CARNÍVOROS 🦖
# ==========================================================
# En este ejercicio:
# - Cada número representa la cantidad de huevos puestos
#   por un dinosaurio en Jurassic Park.
# - Los dinosaurios carnívoros (como el T-Rex) ponen
#   SIEMPRE una cantidad PAR de huevos.
#
# OBJETIVO:
# Crear una función que:
# - Reciba una lista de números enteros
# - Identifique cuáles son pares
# - Devuelva la suma total de esos números pares
# ==========================================================


def count_carnivore_dinosaur_eggs(eggs_list: list) -> int:
    """
    Calcula la cantidad total de huevos puestos por
    dinosaurios carnívoros (números pares).

    En el contexto de Jurassic Park:
    - Cada número de la lista representa huevos puestos
      por un dinosaurio.
    - Solo los dinosaurios carnívoros ponen una cantidad
      PAR de huevos.
    - Los valores impares se ignoran.

    Parameters
    ----------
    eggs_list : list[int]
        Lista de números enteros que representan la
        cantidad de huevos puestos por los dinosaurios.

    Returns
    -------
    int
        Suma total de los números pares encontrados
        en la lista.

    Examples
    --------
    >>> count_carnivore_dinosaur_eggs([3, 4, 7, 5, 8])
    12

    >>> count_carnivore_dinosaur_eggs([1, 3, 5])
    0

    >>> count_carnivore_dinosaur_eggs([])
    0
    """

    total_carnivores_eggs = 0

    for eggs in eggs_list:
        # Verificamos si el número es par
        if eggs % 2 == 0:
            total_carnivores_eggs += eggs

    return total_carnivores_eggs


# ==========================================================
# PRUEBA DE LA FUNCIÓN
# ==========================================================
eggs_list = [3, 4, 7, 5, 8]
print(count_carnivore_dinosaur_eggs(eggs_list))
