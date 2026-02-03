'''DICCIONARIOS EN PYTHON (dict)'''
# ----------------------------------------------------------
# LIMPIAR LA CONSOLA (OPCIONAL)
# ----------------------------------------------------------
import os
os.system('clear')  # En Windows suele usarse 'cls'


# ==========================================================
# DICCIONARIOS EN PYTHON (dict)
# ==========================================================
# Un diccionario es una estructura de datos que almacena
# información en pares:
#
#   clave -> valor
#
# Características:
# - Las claves son ÚNICAS
# - Los valores pueden repetirse
# - Son mutables (se pueden modificar)
# - Permiten estructuras anidadas
#
# Sintaxis:
# diccionario = {clave1: valor1, clave2: valor2, ...}
# ==========================================================


# ----------------------------------------------------------
# CREAR UN DICCIONARIO
# ----------------------------------------------------------
persona = {
    "nombre": "Victor",
    "apellido": "García",
    "edad": 23,
    "es_estudiante": True,
    "cursos": ["Python", "Java"],
    "calificaciones": [6, 7, 9, 8],
    "social": {
        "facebook": "@victorgarcia",
        "twitter": "@victorgarcia",
        "instagram": "@victorgarcia"
    }
}


# ==========================================================
# ACCEDER A LOS VALORES
# ==========================================================
# Se accede a los valores usando la clave
# diccionario["clave"]

print(persona["nombre"])
print(persona["apellido"])
print(persona["edad"])
print(persona["es_estudiante"])
print(persona["cursos"])
# Acceso a lista dentro del diccionario
print(persona["calificaciones"][1])
print(persona["social"]["facebook"])      # Acceso a diccionario anidado
print(persona["social"]["twitter"])
print(persona["social"]["instagram"])

print("\nDiccionario completo:")
print(persona)


# ==========================================================
# MODIFICAR VALORES
# ==========================================================
# Si la clave existe, se reemplaza el valor
persona["nombre"] = "Carlos"
persona["apellido"] = "García"
persona["edad"] = 24

print("\nCambiamos los valores:")
print(persona["nombre"])
print(persona["apellido"])
print(persona["edad"])
print(persona)


# ==========================================================
# ELIMINAR ELEMENTOS
# ==========================================================

# ----------------------------------------------------------
# USANDO del
# ----------------------------------------------------------
# del elimina el par clave-valor
# NO devuelve el valor eliminado
del persona["edad"]

print("\nEliminamos la edad con del:")
print(persona)


# ----------------------------------------------------------
# USANDO pop()
# ----------------------------------------------------------
# pop(clave):
# - Elimina el par clave-valor
# - DEVUELVE el valor eliminado
#
# Diferencia clave entre del y pop:
# - del: solo elimina
# - pop: elimina y devuelve el valor

apellido_eliminado = persona.pop("apellido")

print("\nEliminamos el apellido con pop():")
print("Valor eliminado:", apellido_eliminado)
print(persona)


# ==========================================================
# SOBRESCRIBIR / UNIR DICCIONARIOS CON update()
# ==========================================================
a = {"nombre": "Victor", "apellido": "García"}
b = {"nombre": "Carlos", "apellido": "García", "edad": 24}

print("\nDiccionarios originales:")
print("a:", a)
print("b:", b)


# ----------------------------------------------------------
# update()
# ----------------------------------------------------------
# update() copia los pares clave-valor del diccionario
# pasado como argumento dentro del diccionario original.
#
# FUNCIONAMIENTO:
# - Si la clave existe → se actualiza el valor
# - Si la clave NO existe → se agrega
#
# IMPORTANTE:
# a.update(b) modifica SOLAMENTE a
# b queda intacto

a.update(b)

print("\nDespués de a.update(b):")
print("a:", a)


# ==========================================================
# VERIFICAR SI UNA CLAVE EXISTE
# ==========================================================
# Se usa el operador in (verifica SOLO claves)

print("\nVer si una clave existe en persona:")
print("nombre" in persona)
print("apellido" in persona)
print("edad" in persona)


# ==========================================================
# MÉTODOS IMPORTANTES DE DICCIONARIOS
# ==========================================================

# ----------------------------------------------------------
# keys()
# ----------------------------------------------------------
# Devuelve un objeto con todas las claves
print("\nObtener todas las claves:")
print(persona.keys())


# ----------------------------------------------------------
# values()
# ----------------------------------------------------------
# Devuelve un objeto con todos los valores
print("\nObtener todos los valores:")
print(persona.values())


# ----------------------------------------------------------
# items()
# ----------------------------------------------------------
# Devuelve pares (clave, valor)
# Muy usado para recorrer diccionarios con for
print("\nObtener todos los pares clave-valor:")
print(persona.items())
