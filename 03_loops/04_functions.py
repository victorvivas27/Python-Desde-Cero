# ----------------------------------------------------------
# LIMPIAR LA CONSOLA (OPCIONAL)
# ----------------------------------------------------------
import os
os.system('clear')  # En Windows suele usarse 'cls'


# ==========================================================
# FUNCIONES EN PYTHON
# ==========================================================
# Una función es un bloque de código reutilizable.
#
# Se define con:
#   def nombre_funcion(...):
#
# Puede recibir datos de entrada (parámetros)
# y puede devolver un resultado con return.
#
# IMPORTANTE:
# - return es opcional: si no hay return, la función devuelve None
# - Los parámetros son los "nombres" que recibe la función
# - Los argumentos son los valores que le pasamos al llamarla
# ==========================================================


# ----------------------------------------------------------
# ESTRUCTURA GENERAL DE UNA FUNCIÓN
# ----------------------------------------------------------
"""
def nombre_de_la_funcion(parametro1, parametro2, ...):
    '''Docstring: explicación de lo que hace la función'''
    # cuerpo de la función
    return valor  # opcional
"""


# ==========================================================
# FUNCIÓN SIMPLE (SIN PARÁMETROS)
# ==========================================================
def saludar():
    """
    Imprime un saludo en la consola.
    No recibe parámetros y no devuelve valor (retorna None).
    """
    print("Hola, ¿cómo estás?")


# Para que se ejecute, hay que llamarla
saludar()


# ==========================================================
# FUNCIÓN CON PARÁMETROS
# ==========================================================
def saludar(nombre):
    """
    Imprime un saludo usando el nombre recibido.

    Parámetros:
        nombre (str): Nombre de la persona a saludar.

    Nota:
    - Parámetro: lo que acepta la función (nombre)
    - Argumento: lo que le pasamos al llamarla (ej: "Carlos")
    """
    print(f"Hola {nombre}, ¿cómo estás?")


saludar("Carlos")
saludar("Pedro")
saludar("Juan")


# ==========================================================
# FUNCIÓN QUE DEVUELVE UN VALOR (return)
# ==========================================================
def sumar(a, b):
    """
    Suma dos números y devuelve el resultado.

    Parámetros:
        a (int|float): primer número
        b (int|float): segundo número

    Retorna:
        int|float: suma de a + b
    """
    suma = a + b
    return suma


resultado = sumar(23, 34)
print("La suma es:", resultado)

# Ver documentación de una función:
# print(saludar.__doc__)
# help(saludar)


# ==========================================================
# PARÁMETROS POR DEFECTO (DEFAULT PARAMETERS)
# ==========================================================
# Si el usuario no pasa un argumento, se usa el valor por defecto.
# Reglas:
# - Los parámetros con valor por defecto deben ir al final.
# - Ej: def f(a, b=0): ✅
# - Ej: def f(a=0, b): ❌

def saludar(nombre="Desconocido", apellido=""):
    """
    Imprime un saludo con nombre y apellido.

    Parámetros:
        nombre (str): por defecto "Desconocido"
        apellido (str): por defecto ""

    Ejemplos:
        saludar() -> usa valores por defecto
        saludar("Carlos") -> reemplaza nombre, apellido queda ""
    """
    # Tip: agregamos un espacio si hay apellido para que no quede pegado
    espacio = " " if apellido else ""
    print(f"Hola {nombre}{espacio}{apellido}, ¿cómo estás?")


saludar()
saludar("Carlos")
saludar("Carlos", "García")


# ==========================================================
# ARGUMENTOS POR POSICIÓN (POSITIONAL ARGUMENTS)
# ==========================================================
# Python asigna los argumentos según el orden.

def persona(nombre, apellido, edad):
    """
    Imprime una descripción de la persona.

    Parámetros:
        nombre (str)
        apellido (str)
        edad (int)
    """
    print(f"Mi nombre es {nombre} {apellido} y tengo {edad} años")


persona("Carlos", "García", 25)

# OJO: si cambiás el orden, el programa "funciona" pero los datos quedan mal
persona(23, "García", "Carlos")   # Esto es un ejemplo de por qué conviene usar argumentos por clave


# ==========================================================
# ARGUMENTOS POR CLAVE (KEYWORD ARGUMENTS)
# ==========================================================
# Permiten pasar los valores indicando el nombre del parámetro.
# Ventajas:
# - No importa el orden
# - Es más legible
persona(edad=23, apellido="García", nombre="Carlos")


# ==========================================================
# *args (CANTIDAD VARIABLE DE ARGUMENTOS POR POSICIÓN)
# ==========================================================
# Permite recibir muchos argumentos sin saber cuántos serán.
# args llega como una tupla.

def restar_numeros(*args):
    """
    Resta todos los números recibidos.

    Ejemplo:
        restar_numeros(1,2,3) -> (((0-1)-2)-3) = -6

    Retorna:
        int|float: resultado final
    """
    restar = 0
    for numero in args:
        restar -= numero
    return restar


print(restar_numeros(1,2,3,4,5,6,7,8,9,10))


# ==========================================================
# **kwargs (CANTIDAD VARIABLE DE ARGUMENTOS CLAVE-VALOR)
# ==========================================================
# Recibe argumentos con nombre: clave=valor
# kwargs llega como un diccionario.

def mostrar_informacion_de(**kwargs):
    """
    Muestra información en formato clave: valor.

    Ejemplo:
        mostrar_informacion_de(nombre="Victor", edad=23)
    """
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")


print("\nArgumento de clave-valor variable")
mostrar_informacion_de(
    nombre="Victor",
    apellido="Garcia",
    edad=23
)

print("\nPuedes pasar cualquier argumento")
mostrar_informacion_de(
    nombre="Victor",
    apellido="Garcia",
    edad=23,
    pais="Colombia"
)
