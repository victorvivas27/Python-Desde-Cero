'''Documentacion depuracion'''


def largo_texto(texto):
    '''Funcion que devuelve el largo de un texto'''
    resultado = 0
    for _ in texto:
        resultado += 1
        return resultado


print("comienzo de la depuracion")
largo = largo_texto("Hola depurador")
print(largo)
print("fin de la depuracion")
