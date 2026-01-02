# ==========================================================
# FUNCIÓN print() EN PYTHON
# ==========================================================
# La función print() se utiliza para mostrar información
# en la consola (salida estándar).
#
# Es muy utilizada para:
# - Mostrar resultados
# - Depurar código
# - Interactuar con el usuario
# ==========================================================


# ----------------------------------------------------------
# IMPRIMIR TEXTO
# ----------------------------------------------------------
# Muestra el texto "Hola, mundo!" en la consola
print("Hola, mundo!")

# Se pueden usar comillas simples o dobles
print('Hola, mundo!')


# ----------------------------------------------------------
# IMPRIMIR MÚLTIPLES VALORES
# ----------------------------------------------------------
# Se pueden separar varios valores usando comas
# Python agrega un espacio automáticamente entre ellos
print("Hola", "mundo")


# ----------------------------------------------------------
# PARÁMETRO sep
# ----------------------------------------------------------
# Permite definir el separador entre los valores
print("Hola", "mundo", sep="*")     # Salida: Hola*mundo


# ----------------------------------------------------------
# SALTO DE LÍNEA POR DEFECTO
# ----------------------------------------------------------
# Por defecto, print() agrega un salto de línea al final
print("Hola, mundo!")
print("Esta es una nueva línea.")


# ----------------------------------------------------------
# PARÁMETRO end
# ----------------------------------------------------------
# El parámetro end permite cambiar el carácter final
# Por defecto es '\n' (salto de línea)
print("Hola, mundo!", end=" ")
print("Con espacio sigue en la misma línea.")


# ----------------------------------------------------------
# RESUMEN
# ----------------------------------------------------------
# print() → Muestra información en la consola
# sep     → Define el separador entre valores
# end     → Define cómo termina la impresión
#
# Valores por defecto:
# sep = " "
# end = "\n"
# ==========================================================
