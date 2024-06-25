numeros = []

for x in range(10):
    numero = int(input("Ingrese diez números: "))
    numeros.append(numero)
    
    for x in range(9, -1, -1):
        print("\nLos números ingresados en orden inverso son: ")
        print(numeros[x])