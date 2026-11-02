for numero in range(5):
    print(numero, numero * 'hola mundo')

# for es una estructura de control de flujo que nos permite iterar sobre una secuencia de elementos, como listas, tuplas, diccionarios, conjuntos o cadenas de texto. En este caso, estamos utilizando la función range() para generar una secuencia de números del 0 al 4 (5 no incluido) y luego imprimimos cada número junto con la cadena 'hola mundo' repetida ese número de veces.

buscar = 3 
for numero in range(5):
    print(numero)
    if numero == buscar: 
        print("encontrado", buscar)
        break 
else: 
    print("no encontre el numero")

for char in "hola mundo":
    print(char)