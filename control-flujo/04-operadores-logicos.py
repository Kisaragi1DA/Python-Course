# and, or, not

# and es un operador lógico que devuelve True si ambos operandos son True, de lo contrario devuelve False.
# or es un operador lógico que devuelve True si al menos uno de los operandos es True, de lo contrario devuelve False.
# not es un operador lógico que devuelve True si el operando es False, y devuelve False si el operando es True.

gas = False
encendido = False
edad = 18

if not gas and (encendido or edad > 17):
    print("El coche puede arrancar")
