# ==========================================================
# VARIABLES EN PYTHON
# ==========================================================
# Las variables en Python son contenedores que almacenan
# valores de cualquier tipo de dato.
#
# Python es un lenguaje de tipado:
# - Dinámico → el tipo se asigna en tiempo de ejecución
# - Fuerte   → no convierte tipos automáticamente
# ==========================================================


# ----------------------------------------------------------
# CREACIÓN DE VARIABLES
# ----------------------------------------------------------
# Las variables se crean asignando un valor a un nombre
# usando el operador de asignación '='

a = 10                 # int
b = 3.14               # float
c = "Hola, mundo!"     # str
d = True               # bool


# ----------------------------------------------------------
# NOMBRES DE VARIABLES
# ----------------------------------------------------------
# Reglas:
# - Deben comenzar con una letra o un guion bajo (_)
# - Pueden contener letras, números y guiones bajos
# - No pueden ser palabras reservadas de Python

# Ejemplos válidos:
mi_variable = 5
_variable2 = "Texto"
variable_3 = 3.14

# Ejemplos inválidos (NO ejecutar):
# 5variable = 5      # No puede comenzar con número
# variable- = 5      # No se permiten guiones
# for = 10           # Palabra reservada


# ----------------------------------------------------------
# USO DE VARIABLES
# ----------------------------------------------------------
# Python es de tipado dinámico:
# No es necesario declarar el tipo de dato explícitamente

x = 10
print(type(x))        # <class 'int'>

y = 3.14              # float
z = "Hola"            # str
w = True              # bool


# ----------------------------------------------------------
# CAMBIO DE TIPO DE DATO
# ----------------------------------------------------------
# Una variable puede cambiar de tipo durante la ejecución

x = "Ahora soy una cadena"
print(type(x))        # <class 'str'>


# ----------------------------------------------------------
# TIPADO FUERTE
# ----------------------------------------------------------
# Python NO realiza conversiones de tipo automáticamente

# Ejemplo:
# print("Edad: " + 25)   ❌ Error
# Solución:
# print("Edad: " + str(25))  ✅


# ----------------------------------------------------------
# f-strings (cadenas de formato)
# ----------------------------------------------------------
# Forma recomendada para mostrar variables dentro de texto
# Introducidas en Python 3.6
# Permiten insertar variables y expresiones de forma clara
# y legible usando llaves {} dentro de un string con prefijo f

# ----------------------------------------------------------
# Ejemplo básico
# ----------------------------------------------------------
nombre = "Ana"
edad = 25
print(f"Me llamo {nombre} y tengo {edad} años.")

# ----------------------------------------------------------
# Asignación múltiple de variables
# ----------------------------------------------------------
# Se pueden asignar varias variables en una sola línea
# usando comas, pero no es la forma más recomendable
# cuando el código crece, ya que puede afectar la legibilidad

mi_nombre, mi_edad = "Carlos", 30
print(f"Me llamo {mi_nombre} y tengo {mi_edad} años.")

# ----------------------------------------------------------
# Anotaciones de tipo (type hints)
# ----------------------------------------------------------
# Las anotaciones de tipo son solo una sugerencia
# para el programador, el editor o herramientas de análisis
# Python NO obliga a respetar el tipo indicado

is_user_logged_in: bool = False
print(f"User is logged in: {is_user_logged_in}")

# ----------------------------------------------------------
# Reasignación de la variable con otro tipo de dato
# ----------------------------------------------------------
# Aunque la variable fue anotada como bool,
# Python permite cambiar el tipo de dato en tiempo de ejecución
# Esto demuestra que Python es un lenguaje de tipado dinámico

is_user_logged_in = 43
print(f"User is logged in: {is_user_logged_in}")

# ----------------------------------------------------------
# Nota importante
# ----------------------------------------------------------
# Aunque Python lo permite, no es una buena práctica
# cambiar el tipo de una variable ya definida,
# ya que puede generar confusión y errores lógicos


# ----------------------------------------------------------
# CONVENCIÓN DE NOMBRES DE VARIABLES
# ----------------------------------------------------------
# snake_case → Convención recomendada en Python
mi_variable_ejemplo = 10

# camelCase → Usado en otros lenguajes (NO recomendado en Python)
miVariableEjemplo = 10

# PascalCase → Usado normalmente para nombres de clases
MiVariableEjemplo = 10


# ----------------------------------------------------------
# CONSTANTES EN PYTHON
# ----------------------------------------------------------
# Python no permite declarar constantes de forma nativa.
# Por convención, se usan nombres en MAYÚSCULAS para indicar
# que una variable NO debería modificarse.

PI = 3.14159
GRAVEDAD = 9.81
NOMBRE_APP = "MiAplicacion"


# ----------------------------------------------------------
# RESUMEN
# ----------------------------------------------------------
# - Las variables almacenan datos
# - Python es dinámico y de tipado fuerte
# - El tipo puede cambiar durante la ejecución
# - snake_case es la convención recomendada
# - Las constantes se indican con MAYÚSCULAS
# ==========================================================
