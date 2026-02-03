'''Calculadora en Python'''

print("Bienvenido a la calculadora")
print("Para salir escribe 'salir'")
print("Las operaciones son: suma, resta, multiplica, divide")

RESULTADO = None

while True:

    # BLOQUE 1 – pedir el primer número (solo una vez)
    if RESULTADO is None:
        entrada = input("Ingrese número: ")
        if entrada.lower() == "salir":
            break
        RESULTADO = int(entrada)

    # BLOQUE 2 – pedir operación
    OPERACION = input("Ingrese operación: ")
    if OPERACION.lower() == "salir":
        break

    # BLOQUE 3 – pedir segundo número
    entrada = input("Ingrese número: ")
    if entrada.lower() == "salir":
        break
    NUMERO = int(entrada)

    # BLOQUE 4 – ejecutar operación
    if OPERACION == "suma":
        RESULTADO += NUMERO
    elif OPERACION == "resta":
        RESULTADO -= NUMERO
    elif OPERACION == "multiplica":
        RESULTADO *= NUMERO
    elif OPERACION == "divide":
        if NUMERO == 0:
            print("No se puede dividir por cero")
            continue
        RESULTADO /= NUMERO
    else:
        print("Operación no reconocida")
        continue

    # BLOQUE 5 – mostrar resultado
    print(f"El resultado es: {RESULTADO}")
