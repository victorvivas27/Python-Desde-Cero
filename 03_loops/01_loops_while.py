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
contador = 0

while contador < 10:
    print("Contador sin break:", contador)
    contador += 1   # MUY IMPORTANTE
                    # Sin esto, el bucle sería infinito


# ==========================================================
# USO DE break
# ==========================================================
# break finaliza el bucle inmediatamente,
# sin importar si la condición sigue siendo True.

contador = 0

while True:  # Bucle infinito controlado con break
    print("Contador con break:", contador)
    contador += 1

    if contador == 5:
        break   # Sale del bucle cuando contador vale 5


# ==========================================================
# USO DE continue
# ==========================================================
# continue:
# - NO termina el bucle
# - Salta a la SIGUIENTE iteración
# - El código debajo de continue NO se ejecuta

contador = 0

while contador < 10:
    contador += 1

    # Si el número es par, salta a la siguiente vuelta
    if contador % 2 == 0:
        continue

    # Este print solo se ejecuta para números impares
    print("Contador con continue:", contador)


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

contador = 0

while contador < 10:
    print("Contador con else:", contador)
    contador += 1

    break   # Al usar break, el else NO se ejecuta
else:
    print("Bucle terminado correctamente")


# ----------------------------------------------------------
# EJEMPLO SIN break (else SÍ se ejecuta)
# ----------------------------------------------------------
contador = 0

while contador < 3:
    print("Contador:", contador)
    contador += 1
else:
    print("Bucle terminado sin interrupciones")


# ==========================================================
# VALIDAR DATOS DEL USUARIO CON while
# ==========================================================
# Pedir un número hasta que sea positivo

numero = -1

while numero < 0:
    numero = int(input("Ingresa un número: "))

    if numero < 0:
        print("El número debe ser positivo")

print(f"Gracias, el número ingresado es {numero}")


# ==========================================================
# MANEJO DE ERRORES (try / except) CON while
# ==========================================================
# ¿Qué pasa si el usuario ingresa una cadena (ej: 'hola')?
# int('hola') genera un ValueError
#
# Para evitar que el programa se rompa,
# usamos try / except.

numero = -1

while numero < 0:
    try:
        numero = int(input("Ingresa un número: "))

        if numero < 0:
            print("El número debe ser positivo")

    except:
        # Se ejecuta si ocurre un error (ej: letras)
        print("Entrada inválida. Debes ingresar un número.")

print(f"Gracias, el número ingresado es {numero}")
