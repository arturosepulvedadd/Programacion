def potencia(num, exp):
    
    if exp == 0:
        return 1
    elif exp == 1:
        return num
    else:
        return num * potencia(num, exp - 1)

base = int(input("Ingrese la base de la potencia a calcular: "))
exponente = int(input("Ingrese el exponente de la potencia a calcular: "))

obtencion = potencia(base, exponente)

print(f"El resultado de {base} elevado a {exponente} es {obtencion}")