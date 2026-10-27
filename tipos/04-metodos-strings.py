animal = " cerDIto feliz "
print(animal.upper())  # Convierte a mayúsculas
print(animal.lower())  # Convierte a minúsculas
print(animal.strip().capitalize())  # Elimina espacios y convierte la primera letra a mayúscula
print(animal.title())  # Convierte la primera letra de cada palabra a mayúscula
print(animal.strip())  # Elimina espacios en blanco al inicio y al final
print(animal.lstrip())  # Elimina espacios en blanco al inicio
print(animal.rstrip())  # Elimina espacios en blanco al final
print(animal.find("DI"))  # Busca la posición de la subcadena "DI"
print(animal.replace("rDI", "di"))
print("rDI" in animal)  # Verifica si la subcadena "rDI" está en la cadena
print("rDI" not in animal) # Verifica si la subcadena "rDI" no está en la cadena
