#control 2 pregunta 2

nombres_con_a=[]
nombres_sin_a=[]

for i in range(7):
    nombre=(input("Ingrese un nombre: "))
    nombres_con_a.append(nombre)
    
for nombre in nombres_con_a:
    if nombre[-1] != "a":
        nombres_sin_a.append(nombre)

print("Lista de nombres resultante :",nombres_sin_a)