def quitar_espacios(texto):
    texto_sin_espacios = ""
    for char in texto: 
        if char != " ":
            texto_sin_espacios += char
    return texto_sin_espacios

def texto_al_reves(texto):
    texto_reverso = ""
    for char in texto:
        texto_reverso = char + texto_reverso
    return texto_reverso

def es_palindromo(texto):
    texto = quitar_espacios(texto)
    texto_reverso = texto_al_reves(texto)
    return texto.lower() == texto_reverso.lower()

print(es_palindromo("Anita lava la tina"))
print(es_palindromo("Hola Mundo"))
print(es_palindromo("Reconocer"))
