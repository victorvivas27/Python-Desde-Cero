#Una lista es una colección ordenada y mutable de elementos que pueden ser de diferentes tipos de datos.
#Se definen utilizando corchetes [] y los elementos están separados por comas.
#Crear una lista
mi_lista = [1, 2, 3,2,4,6,3,] #Lista de enteros
mi_lista2 = [1,2.3,"hola"] #Lista de diferentes tipos de datos
mi_lista3=[]#Lista bacia
mi_lista4=[[1,2], [3,4]] #Lista anidada o lista dentro de otra lista o multidimensional
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]
print("Lista 1:", mi_lista)
print("Lista 2:", mi_lista2)
print("Lista 3:", mi_lista3)
print("Lista 4:", mi_lista4)
print("Matriz:", matrix)
#Acceder a elementos de una lista
primer_elemento = mi_lista[0] #Acceder al primer elemento
ultimo_elemento = mi_lista[-1] #Acceder al último elemento
print("Primer elemento de mi_lista:", primer_elemento)
print("Último elemento de mi_lista:", ultimo_elemento)
#Aceder a elementos de una lista anidada
elemento_anidado = mi_lista4[1][0] #Acceder al primer
print("Elemento anidado de mi_lista4:", elemento_anidado)
# Slicing (rebanado) de listas
mi_lista = [1, 2, 3,2,4,6,3,]
#Desde el inicio hasta el índice 3 (excluyendo el índice 3)
primeros_tres = mi_lista[2:3] #Acceder a los primeros tres elementos
print("Primeros tres elementos de mi_lista:", primeros_tres)
#Desde el índice 3 hasta el final
primeros_tres = mi_lista[:3] #Acceder a los primeros tres elementos
ultimos_tres = mi_lista[-3:] #Acceder a los últimos tres elementos
print("Primeros tres elementos de mi_lista:", primeros_tres)
print("Últimos tres elementos de mi_lista:", ultimos_tres)
#Con : se hace una copia de la lista completa
copia_lista = mi_lista[:]
print("Copia de mi_lista:", copia_lista)

#Podemos usar :: para definir un paso en el slicing
#Desde el inicio hasta el final con un paso de 2
#Nos da paso a paso los elementos de la lista
#Aca en este ejemplo nos dara los elementos en las posiciones pares

lista_paso_dos = mi_lista[::2]
print("Elementos de mi_lista con paso de 2:", lista_paso_dos)

#Otros ejemplo de 3
lista_paso_tres = mi_lista[::3]
print("Elementos de mi_lista con paso de 3:", lista_paso_tres)

#Lista invertida con slicing
lista_invertida = mi_lista[::-1]
print("Lista invertida:", lista_invertida)

#Modificar elementos de una lista
#En la posición 0 de la lista, cambiar el valor a 10
mi_lista[0] = 10 #Cambiar el primer elemento a 10
print("Lista modificada:", mi_lista)

#Si ponemos el indice no existe nos dara un error IndexError
#mi_lista[10] = 20 #Esto dara un error

#Añadir elementos a una lista
mi_lista.append(7) #Añadir 7 al final de la lista
print("Lista con el elemento 7:", mi_lista) #Imprimir la lista
mi_lista.insert(1, 5) #Añadir 5 en la posición 1 de la lista
print("Lista con el elemento 5 en la posición 1:", mi_lista)    #Imprimir la lista
mi_lista.extend([8, 9]) #Añadir 8 y 9 al final de la lista
print("Lista con los elementos 8 y 9:", mi_lista) #Imprimir la lista

#Concatenar listas
#Esat forma es la menos eficiente,porque crea una nueva lista en memoria
otra_lista = [10, 11, 12]
lista_concatenada = mi_lista + otra_lista
print("Lista concatenada ,menos eficiente:", lista_concatenada)

#Forma más eficiente de concatenar listas
mi_lista += otra_lista
print("Lista mi_lista después de concatenar otra_lista:", mi_lista)

