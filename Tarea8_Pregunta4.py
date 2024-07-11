def sumatoria(numero):
    if numero == 0:
        return 0
    else:
        return numero + sumatoria(numero - 1)

# Acá se utiliza el programa para calcular la sumatoria de el número que se desee
# Por ejemplo:

numero = 10
resultado = sumatoria(numero)
print("La sumatoria de", numero, "es:", resultado)