def area_circulo(radio):
    pi = 3.14159
    area = pi * radio ** 2
    return area

# Programa Principal:

radio_circulo = 5
area_del_circulo = area_circulo(radio_circulo)
print("El área del círculo con radio", radio_circulo, "es:", area_del_circulo)