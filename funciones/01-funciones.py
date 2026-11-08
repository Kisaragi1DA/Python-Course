# Argumentos y Parametros en Funciones 

def hola(nombre, apellido="Feliz"):
    print("Hola Mundo")
    print(f"Bienvenido {nombre} {apellido}")

hola("Darien", "Gonzalez")
hola("Packy") 

hola(apellido="Rojas", nombre="Darien") #Argumentos nombrados 
