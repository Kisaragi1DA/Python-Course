saludo = 25

def saludar():
    global saludo
    saludo = "Hola Mundo"

def saludoCerdito():
    saludo = 24 
    print(saludo)

saludar()
print(saludo)
saludoCerdito()

# global saludo: permite modificar la variable global "saludo" dentro de la función "saludar()".
# No es recomendado usar variables globales, ya que puede generar confusión y errores en el código. Es mejor pasar variables como argumentos a las funciones o devolver valores desde ellas.
