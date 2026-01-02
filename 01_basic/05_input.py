# ==========================================================
# FUNCIÓN input()
# ==========================================================
# La función input() se utiliza para recibir datos ingresados
# por el usuario desde la consola.
#
# Características importantes:
# - Pausa la ejecución del programa
# - Espera que el usuario ingrese un valor
# - Finaliza cuando el usuario presiona Enter
#
# IMPORTANTE:
# - input() SIEMPRE devuelve una cadena de texto (str)
# ==========================================================


# ----------------------------------------------------------
# USO BÁSICO DE input()
# ----------------------------------------------------------
# Se puede usar input() sin parámetros.
# En este caso, el mensaje se muestra con print()

print("¿Cuál es tu nombre?")
nombre = input()  # El programa se detiene hasta que el usuario ingrese un dato
print("Hola", nombre)


# ----------------------------------------------------------
# input() CON MENSAJE DIRECTO
# ----------------------------------------------------------
# También se puede pasar el mensaje directamente
# como argumento de la función input()

edad = input("¿Cuántos años tienes?\n")
print("Tienes " + edad + " años.")


# ----------------------------------------------------------
# TIPO DE DATO DEVUELTO POR input()
# ----------------------------------------------------------
# Aunque el usuario ingrese números,
# input() SIEMPRE devuelve un string (str)

print(type(edad))  # <class 'str'>


# ----------------------------------------------------------
# CONVERSIÓN DE TIPO (CASTING)
# ----------------------------------------------------------
# Si se necesita trabajar con valores numéricos,
# es obligatorio convertir el string al tipo deseado

edad_num = int(edad)  # Convertir cadena a entero
print("El próximo año tendrás " + str(edad_num + 1) + " años.")

# Nota:
# - int() convierte a entero
# - str() convierte a cadena
# Python es de tipado fuerte, no convierte automáticamente


# ----------------------------------------------------------
# OBTENER MÚLTIPLES VALORES CON input() Y split()
# ----------------------------------------------------------
# La función split() divide una cadena en varias partes
# y devuelve una lista de valores.
#
# Parámetros de split():
# - Separador (opcional): por defecto es espacio
# - maxsplit (opcional): número máximo de divisiones

print("Obtener múltiples valores a la vez:")

nombre, apellido, edad = input(
    "Ingrese su nombre, apellido y edad: "
).split()

print("Nombre:", nombre)
print("Apellido:", apellido)
print("Edad:", edad)


# ----------------------------------------------------------
# POSIBLES ERRORES EN TIEMPO DE EJECUCIÓN
# ----------------------------------------------------------
# Si el usuario no ingresa la cantidad correcta de valores,
# Python lanzará un error en tiempo de ejecución (ValueError)
#
# Ejemplo de entrada incorrecta:
# Juan Perez
#
# El programa espera 3 valores y recibe solo 2
