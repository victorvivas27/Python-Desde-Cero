'''Funcion es_palindromo()'''


def texto_sin_espacios(texto):
    '''Funcion texto_sin_espacios()'''
    nuevo_texto = ""
    for caracter in texto:
        if caracter != " ":
            nuevo_texto += caracter
    return nuevo_texto

def reves (texto):
    '''Funcion reves()'''
    texto_al_reves = ""
    for caracter in texto:
        texto_al_reves = caracter + texto_al_reves
    return texto_al_reves


def es_palindromo(texto):
    '''Funcion es_palindromo()'''
    texto = texto_sin_espacios(texto)
    texto_al_reves = reves(texto)
    return texto.lower() == texto_al_reves.lower()


print(es_palindromo("Amo la paloma"))
print(es_palindromo("Hola mundo python"))
