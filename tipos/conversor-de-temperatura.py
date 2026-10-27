n1 = input("Ingresa la temperatura en grados Celsius: ")

n1 = float(n1) 

Fahrenheit = (n1 * 9/5) + 32
Kelvin = n1 + 273.15

mensaje = f"""
La temperatura en grados Celsius es: {n1}°C
La temperatura en grados Fahrenheit es: {Fahrenheit}°F
La temperatura en grados Kelvin es: {Kelvin}K 
""" 

print(mensaje) 
