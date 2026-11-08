def calcular_total_final(total_cuenta, porcentaje_descuento):
    descuento = total_cuenta * (porcentaje_descuento / 100)
    total_final = total_cuenta - descuento
    return total_final

# Ejemplo de uso
total = calcular_total_final(1000, 20)
print("Total final:", total)