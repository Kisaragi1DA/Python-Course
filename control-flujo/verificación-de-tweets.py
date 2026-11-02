print("Bienvenido a Twitter")

tw = ""
while tw != "salir":
    tw = input("Ingrese un tweet: ")
    if len(tw) > 20:
        print("Su tweet es demasiado largo. Ingrese un tweet de 20 caracteres o menos.")
    elif not tw:
            print("No puede enviar un tweet vacío. Ingrese un tweet de 20 caracteres o menos.")
    else:
        print("Tweet publicado: ") 
