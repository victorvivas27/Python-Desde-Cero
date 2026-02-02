'''Documentacion de bucles while en Python'''
# ----------------------------------------------------------
# LIMPIAR LA CONSOLA (OPCIONAL)
# ----------------------------------------------------------
import os
os.system('clear')  # En Windows suele usarse 'cls'


# ==========================================================
# BUCLE while
# ==========================================================
# El bucle while repite un bloque de código
# MIENTRAS una condición sea verdadera (True).
#
# Si la condición deja de cumplirse, el bucle termina.
# ==========================================================


# ----------------------------------------------------------
# ESTRUCTURA BÁSICA DE while
# ----------------------------------------------------------
# Sintaxis:
#
# while condición:
#     bloque de código
#
# IMPORTANTE:
# - La condición se evalúa ANTES de cada iteración
# - Python usa indentación para definir el bloque
# - Si la condición nunca se vuelve False → bucle infinito
# ----------------------------------------------------------


# ==========================================================
# EJEMPLO BÁSICO DE while
# ==========================================================
CONTADOR = 0
while CONTADOR < 10:
    print("Contador sin break:", CONTADOR)
    CONTADOR += 1   # MUY IMPORTANTE
                    # Sin esto, el bucle sería infinito


# ==========================================================
# USO DE break
# ==========================================================
# break finaliza el bucle inmediatamente,
# sin importar si la condición sigue siendo True.

CONTADOR = 0

while True:  # Bucle infinito controlado con break
    print("Contador con break:", CONTADOR)
    CONTADOR += 1

    if CONTADOR == 5:
        break   # Sale del bucle cuando CONTADOR vale 5


# ==========================================================
# USO DE continue
# ==========================================================
# continue:
# - NO termina el bucle
# - Salta a la SIGUIENTE iteración
# - El código debajo de continue NO se ejecuta

CONTADOR = 0

while CONTADOR < 10:
    CONTADOR += 1

    # Si el número es par, salta a la siguiente vuelta
    if CONTADOR % 2 == 0:
        continue

    # Este print solo se ejecuta para números impares
    print("Contador con continue:", CONTADOR)


# ----------------------------------------------------------
# ¿QUÉ HACE EXACTAMENTE continue?
# ----------------------------------------------------------
# Cuando Python encuentra continue:
# 1) Ignora el resto del código del bucle
# 2) Vuelve a evaluar la condición del while
# ----------------------------------------------------------


# ==========================================================
# BUCLE while CON else
# ==========================================================
# El bloque else se ejecuta SOLO SI:
# - El bucle termina normalmente
# - NO se ejecutó un break
#
# Si hay un break → el else NO se ejecuta
# ==========================================================

CONTENEDOR = 0

while CONTENEDOR < 10:
    print("Contador con else:", CONTENEDOR)
    CONTENEDOR += 1

    break   # Al usar break, el else NO se ejecuta
else:
    print("Bucle terminado correctamente")


# ----------------------------------------------------------
# EJEMPLO SIN break (else SÍ se ejecuta)
# ----------------------------------------------------------
CONTADOR = 0

# while CONTADOR < 3:
#     print("Contador:", CONTADOR)
#     CONTADOR += 1
# else :
#     print("Bucle terminado sin interrupciones")


# ==========================================================
# VALIDAR DATOS DEL USUARIO CON while
# ==========================================================
# Pedir un número hasta que sea positivo

NUMERO = -1

while NUMERO < 0:
    NUMERO = int(input("Ingresa un número: "))

    if NUMERO < 0:
        print("El número debe ser positivo")

print(f"Gracias, el número ingresado es {NUMERO}")


# ==========================================================
# MANEJO DE ERRORES (try / except) CON while
# ==========================================================
# ¿Qué pasa si el usuario ingresa una cadena (ej: 'hola')?
# int('hola') genera un ValueError
#
# Para evitar que el programa se rompa,
# usamos try / except.

NUMERO = -1

while NUMERO < 0:
    try:
        NUMERO = int(input("Ingresa un número: "))

        if NUMERO < 0:
            print("El número debe ser positivo")

    except ValueError:
        # Se ejecuta si ocurre un error (ej: letras)
        print("Entrada inválida. Debes ingresar un número.")

print(f"Gracias, el número ingresado es {NUMERO}")
