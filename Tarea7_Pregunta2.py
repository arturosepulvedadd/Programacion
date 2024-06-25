palabras = []

while True:
    palabra = input("Ingrese una palabra (presione enter para terminar): ")
    if palabra == "":
        break
    palabras.append(palabra)
    
    def contar_caracteres_a(palabra):
        contador = 0
        for letra in palabra:
             if letra == 'A' or letra == 'a':
                contador += 1
                return contador
    
    for palabra in palabras:
        cantidad_a = contar_caracteres_a(palabra)
        print("La palabra", palabra, "tiene", cantidad_a, "caracteres 'A' o 'a'")

