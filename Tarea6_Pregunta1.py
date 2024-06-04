def contar_vocales_consonantes(palabra):
    contador_vocales = 0
    contador_consonantes = 0
    vocales = ['a', 'e', 'i', 'o', 'u']
    
    for letra in palabra:
        if letra in vocales:
            contador_vocales += 1
        elif letra.isalpha():
            contador_consonantes += 1
    
    return contador_vocales, contador_consonantes

palabras = []
    
while True:
    palabra = input("Ingrese cualquier palabra (presione Enter para finalizar): ")
    if palabra == "":
        break

    palabras.append(palabra)
    
for palabra in palabras:
    vocales, consonantes = contar_vocales_consonantes(palabra)
    print(f"La palabra '{palabra}' tiene {vocales} vocal(es) y {consonantes} consonante(s)")