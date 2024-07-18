def digitos(num):
    
    numero_como_str = str(num)
    cantidad_digitos = len(numero_como_str)
    return cantidad_digitos

numero = input("Ingrese el número que desee (en palabra): ")

total_digitos = digitos(numero)

print(f"El número {numero} tiene {total_digitos} dígitos")