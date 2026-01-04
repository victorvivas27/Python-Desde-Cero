# ----------------------------------------------------------
# LIMPIAR LA CONSOLA (OPCIONAL)
# ----------------------------------------------------------
import os
os.system('clear')  # En Windows suele usarse 'cls'


# ==========================================================
# EJERCICIO: ¿ESTÁ EN EQUILIBRIO LA ALIANZA?
# ==========================================================
# En este ejercicio trabajamos con strings y funciones.
#
# Personajes:
# - Reed Richards (Mr. Fantastic)  -> letra "R"
# - Johnny Storm (Antorcha Humana) -> letra "J"
#
# Objetivo:
# Crear una función que:
# - Reciba un texto (string)
# - Cuente cuántas veces aparece "R" y "J"
# - Devuelva True si ambas cantidades son iguales
# - Devuelva False si son distintas
#
# CASO ESPECIAL:
# - Si no aparece ninguna "R" ni "J"
#   (0 == 0) → también devuelve True
# ==========================================================


# ----------------------------------------------------------
# FUNCIÓN check_is_balanced
# ----------------------------------------------------------
def check_is_balanced(text):
    """
    Determina si existe equilibrio entre las letras R y J
    dentro de un texto.

    Parámetros:
        text (str): cadena de texto a analizar

    Retorna:
        bool:
        - True  -> si la cantidad de 'R' y 'J' es igual
        - False -> si la cantidad es distinta
    """

    # Convertimos todo el texto a mayúsculas
    # para evitar problemas con r / R o j / J
    text = text.upper()

    # ------------------------------------------------------
    # CONTAR APARICIONES DE CADA LETRA
    # ------------------------------------------------------
    # count() cuenta cuántas veces aparece un carácter
    r_count = text.count("R")
    j_count = text.count("J")

    # Mostrar resultados (útil para debug o aprendizaje)
    print(f"R: {r_count}")
    print(f"J: {j_count}")

    # ------------------------------------------------------
    # COMPROBAR EQUILIBRIO
    # ------------------------------------------------------
    # - Si r_count == j_count → True
    # - Si son diferentes      → False
    #
    # Esto cubre también el caso:
    # r_count = 0 y j_count = 0
    return r_count == j_count


# ==========================================================
# PRUEBAS DE LA FUNCIÓN
# ==========================================================

print(check_is_balanced("rrrrrrrrjj"))      # False (8 R, 2 J)
print(check_is_balanced("rrrrjjjjjjjj"))    # False (4 R, 8 J)
print(check_is_balanced("rrjj"))            # True  (2 R, 2 J)
print(check_is_balanced("fgtbhydttd"))       # True  (0 R, 0 J)
