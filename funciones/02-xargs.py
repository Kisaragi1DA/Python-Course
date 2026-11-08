def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)

suma(2,5,7)
suma(2,5)
suma(5,9,3,7)

# * sirve para pasar un número variable de argumentos a una función