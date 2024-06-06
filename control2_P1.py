#control 2 pregunta 1

puntajes_diarios = []

for dia in range(1, 16):
    puntaje = int(input(f"Ingrese el puntaje del día {dia}: "))
    puntajes_diarios.append(puntaje)

contador_menor_70 = 0

for puntaje in puntajes_diarios:
    if puntaje < 70:
        contador_menor_70 += 1

print("Días con puntaje menor a 70:")
contador_dia = 1
while contador_menor_70 > 0:
    if puntajes_diarios[contador_dia - 1] < 70:
        print(f"Día {contador_dia}")
        contador_menor_70 -= 1
    contador_dia += 1

print("Días con puntaje igual o mayor a 70:")
while contador_dia <= 15:
    if puntajes_diarios[contador_dia - 1] >= 70:
        print(f"Día {contador_dia}")
    contador_dia += 1

