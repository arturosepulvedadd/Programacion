#control 2 pregunta 3

palabras=[]
while True:
    palabra=input("Ingrese una palabra (enter para finalizar): ")
    palabras.append(palabra)
    if palabra=="":
        break

for palabra in palabras:
            if len(palabra)<len(palabras):
                menor_caracter=len(palabra)

print("Caracteres: ",menor_caracter)