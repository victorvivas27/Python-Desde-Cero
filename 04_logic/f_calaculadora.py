'''Calculadora en Python'''


print("Bienvenido a la calculadora")
print("Para salir escribe 'salir'")
print("Las operaciones son: suma, resta, multiplica, divide")

resultado = None

while True:

    # BLOQUE 1 – pedir el primer número (solo una vez)
    if resultado is None:
        entrada = input("Ingrese número: ")
        if entrada.lower() == "salir":
            break
        resultado = int(entrada)

    # BLOQUE 2 – pedir operación
    operacion = input("Ingrese operación: ")
    if operacion.lower() == "salir":
        break

    # BLOQUE 3 – pedir segundo número
    entrada = input("Ingrese número: ")
    if entrada.lower() == "salir":
        break
    numero = int(entrada)

    # BLOQUE 4 – ejecutar operación
    if operacion == "suma":
        resultado += numero
    elif operacion == "resta":
        resultado -= numero
    elif operacion == "multiplica":
        resultado *= numero
    elif operacion == "divide":
        if numero == 0:
            print("No se puede dividir por cero")
            continue
        resultado /= numero
    else:
        print("Operación no reconocida")
        continue

    # BLOQUE 5 – mostrar resultado
    print(f"El resultado es: {resultado}")
