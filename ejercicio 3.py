#Crear una lista para almacenar las alturas
alturas = []
#Solicitar al usuario que ingrese las alturas
while True:
    altura = float(input("Ingrese la altura de la persona en metros (0 para finalizar): "))
    if altura == 0:
        break
    alturas.append(altura)
#Calcular la altura promedio
if len(alturas) > 0:
    promedio_alturas = sum(alturas) / len(alturas)
    print(f"La altura promedio de las personas ingresadas es:", promedio_alturas, "metros")
else:
    print("No se ingresaron datos")