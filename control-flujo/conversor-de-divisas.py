print("Conversor de divisas")

# • 1 USD = 0.95 EUR • 1 USD = 20.28 MXN • 1 EUR = 21.36 MXN 

cambio =""
while True:
    if not cambio:
        cambio = input("Ingrese cantidad a convertir: ")
        if cambio.lower() == "salir":
            break
        cambio = float(cambio)
    op = input("Ingrese su divisa: ")
    if op.lower() == "salir":
        break

    if op.lower() == "mxn":
        resultado = {"USD": cambio / 20.28, "EUR": cambio / 21.36}
    elif op.lower() == "usd":
        resultado = {"MXN": cambio * 20.28, "EUR": cambio * 0.95}
    elif op.lower() == "eur":
        resultado = {"USD": cambio / 0.95, "MXN": cambio * 21.36}
    else: 
        print("Operación no válida")
        break

    print(f"Su conversion es: {resultado}")
