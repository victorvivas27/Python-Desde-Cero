# ----------------------------------------------------------
# LIMPIAR LA CONSOLA (OPCIONAL)
# ----------------------------------------------------------
import os
os.system('clear')  # En Windows suele usarse 'cls'

# ==========================================================
# DICCIONARIOS EN PYTHON
# ==========================================================
# Los diccionarios son estructuras de datos
# que permiten almacenar datos en pares clave-valor.
#
# Los diccionarios se definen con:
#   diccionario = {clave1: valor1, clave2: valor2, ...}
# ==========================================================

persona = {
    "nombre": "Victor",
    "apellido": "García",
    "edad": 23,
    "es_estudiante": True,
    "cursos": ["Python", "Java"],
    "calificaciones":[6,7,9,8],
    "social":{
        "facebook": "@victorgarcia",
        "twitter": "@victorgarcia",
        "instagram": "@victorgarcia"
        
    }
}

#Para acceder a los valores
print(persona["nombre"])
print(persona["apellido"])
print(persona["edad"])
print(persona["es_estudiante"])
print(persona["cursos"])
print(persona["calificaciones"][1])
print(persona["social"]["facebook"])
print(persona["social"]["twitter"])
print(persona["social"]["instagram"])
print(persona)

#Cambiar valores
persona["nombre"] = "Carlos"
persona["apellido"] = "García"
persona["edad"] = 24

print("\nCambiamos los valores")
print(persona["nombre"])
print(persona["apellido"])
print(persona["edad"])
print(persona)

#Eliminar elementos
del persona["edad"]
print("\nEliminamos la edad")
print(persona)

#Usamos pop para eliminar 
#La diferncia entre pop y del es que pop devuelve el valor
#del elemento eliminado
#Ser mas explicativo  en este punto 
persona.pop("apellido")
print("\nEliminamos el apellido")
print(persona)

#Sobrescribir un diccionario
a = {"nombre": "Victor", "apellido": "García"}
b = {"nombre": "Carlos", "apellido": "García", "edad": 24}


print("\nDiccionarios originales a y b")
print(a)
print(b)

a.update(b)
print("\nSobreescribimos el diccionario")
print(a)
 #Como funciona update  se funciona  de  derecha a izquierda
 # si una clave  existe le cambia  el valor si la clave :valor no existe la agrega
 
 #Ver si una clave existe

print("\nVer si una clave existe")
print("nombre" in persona)
print("apellido" in persona)
print("edad" in persona)

#Optener todas las claves y valores
print("\nOptener todas las claves")
print(persona.keys())

print("\nOptener todos los valores")
print(persona.values())

#Para optener todos los pares clave-valor
print("\nOptener todos los pares clave-valor")
print(persona.items())