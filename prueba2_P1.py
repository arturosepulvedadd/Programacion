lista = []

while True:
    nota = float(input("Ingrese una nota (0 para finalizar): "))
    if nota == 0:
        break
        lista.append(nota)
        
cant_notas = len(lista)
print("Cantidad de notas: ", cant_notas)

if cant_notas > 0:
    promedio = sum(lista) / cant_notas
else:
    promedio = 0
    print("Promedio de notas: ", promedio)

notas_menores = 0

for nota in lista:
    if nota < 4.0:
        notas_menores = notas_menores + 1
        print("Cantidad de notas menores: ", notas_menores)      
        
notas_mayores = 0

for nota in lista:
    if nota >= 4.0:
        notas_mayores = notas_mayores + 1
        print("Cantidad de notas mayores: ", notas_mayores)             