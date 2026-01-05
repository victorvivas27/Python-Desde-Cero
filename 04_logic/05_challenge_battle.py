"""
Tienes dos listas de números, lista_a y lista_b, ambas de la misma longitud. 

Cada número en lista_a se "enfrenta" al número en la misma posición en lista_b.

- Si el número en lista_a es mayor, su valor se suma al siguiente número en lista_a.
- Si el número en lista_b es mayor, su valor se suma al siguiente número en lista_b.
- Si los dos números son iguales, ambos se eliminan y no afectan al siguiente par.

Debes simular estos enfrentamientos y devolver el resultado final:
- Si al final queda un número en lista_a, devuelve ese número seguido de la letra "lista_a" (por ejemplo, "3a").
- Si al final queda un número en lista_b, devuelve ese número seguido de la letra "lista_b" (por ejemplo, "2b").
- En caso de empate, devuelve la letra "x".

lista_a = [2, 4, 2]
lista_b = [3, 3, 4]

resultado = battle(lista_a, lista_b)  # -> "2b"

# Explicación:
# - 2 vs 3: gana 3 (+1)
# - 4 vs 3+1: empate
# - 2 vs 4: gana 4 (+2)
# Resultado: "2b"

lista_a = [4, 4, 4]
lista_b = [2, 8, 2]

resultado = battle(lista_a, lista_b)  # -> "x"

# Explicación:
# - 4 vs 2: gana 4 (+2)
# - 4+2 vs 8: gana 8 (+2)
# - 4 vs 2+2: empate
# Resultado: "x"
"""

from os import system
if system("clear") != 0: system("cls")

# Fuerza bruta: buscar la solución A SACO.
# Algoritmos ocultos o cálculos o fórmulas
# Programación dinámica: buscar una solución mas eficiente


# def battle(lista_a, lista_b):
#     puntos_a = sum(lista_a)
#     puntos_b = sum(lista_b)
#     return f"{puntos_a - puntos_b}lista_a" if puntos_a > puntos_b else f"{puntos_b - puntos_a}lista_b" if puntos_b > puntos_a else "x"


# lista_a = [4, 4, 4]
# lista_b = [2, 8, 2]
# winner = battle(lista_a, lista_b)
# print(winner)

def battle(lista_a, lista_b):
    """
    Simula una serie de enfrentamientos entre dos listas de números.

    En cada posición:
    - El número de lista_a se enfrenta al número de lista_b.
    - El mayor suma la diferencia al siguiente número de su propia lista.
    - Si ambos números son iguales, se eliminan y no afectan al siguiente par.

    Al finalizar:
    - Si queda un número ganador en lista_a → devuelve "<valor>lista_a"
    - Si queda un número ganador en lista_b → devuelve "<valor>lista_b"
    - Si hay empate total → devuelve "x"

    Parameters
    ----------
    lista_a : list[int]
        Lista de números del jugador A.
    lista_b : list[int]
        Lista de números del jugador B.

    Returns
    -------
    str
        Resultado final del enfrentamiento.
    """
    n = len(lista_a)

    for i in range(n):
        # EMPATE
        if lista_a[i] == lista_b[i]:
            lista_a[i] = 0
            lista_b[i] = 0
            continue

        # GANA LISTA A
        if lista_a[i] > lista_b[i]:
            diferencia = lista_a[i] - lista_b[i]
            lista_a[i] = 0
            lista_b[i] = 0

            if i + 1 < n:
                lista_a[i + 1] += diferencia
            else:
                return f"{diferencia}a"

        # GANA LISTA B
        else:
            diferencia = lista_b[i] - lista_a[i]
            lista_a[i] = 0
            lista_b[i] = 0

            if i + 1 < n:
                lista_b[i + 1] += diferencia
            else:
                return f"{diferencia}b"

    total_a = sum(lista_a)
    total_b = sum(lista_b)

    if total_a > total_b:
        return f"{total_a}a"
    elif total_b > total_a:
        return f"{total_b}b"
    else:
        return "x"
    
lista_a = [4, 4, 4,5]
lista_b = [2, 8, 2,3]
winner = battle(lista_a, lista_b)
print(winner)    