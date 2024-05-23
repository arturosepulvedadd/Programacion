nombre1 = input("Ingrese el nombre de la primera persona: ")
nombre2 = input("Ingrese el nombre de la segunda persona: ")
nombres_ordenados = sorted([nombre1, nombre2])
print("Nombres ordenados alfabéticamente:")
for nombre in nombres_ordenados:
    print(nombre)