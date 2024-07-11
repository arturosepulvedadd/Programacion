def separar(lista):
    pares = []   
    impares = []  
    
    for num in lista:
        if num % 2 == 0:
            pares.append(num)   
        else:
            impares.append(num) 
    
    return pares, impares  

# Programa Principal
# Por ejemplo, ordenar la siguiente lista:

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pares, impares = separar(numeros)
print("Números pares:", pares)
print("Números impares:", impares)