def es_binario(var):
    
    for caracter in var:
        if caracter != "0" and caracter != "1":
            return False
        return True

texto = input("Ingrese un texto a su elección: ")

es_binaria = es_binario(texto)

if es_binaria:
    print(f"El término {texto} es una expresión binaria")
else:
    print(f"El término {texto} no es una expresión binaria")