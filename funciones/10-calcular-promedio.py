def calcular_media(*numeros):    
    if not numeros:        
        return 0    
    return sum(numeros) / len(numeros)

# Ejemplo de uso

print(calcular_media(1, 2, 3, 4, 5))  # Salida: 3.0