supermercado = {}

print("Ingrese los productos y sus cantidades:")
while True:
    producto = input("Nombre del producto (Enter para finalizar): ")
    if producto == "":
        break
    cantidad = int(input("Cantidad: "))
    supermercado[producto] = cantidad
    
    x = int(input("\nIngrese un valor numérico X para multiplicar las cantidades: "))
    print("\nProductos y cantidades multiplicadas por X:")
    for producto, cantidad in supermercado.items():
        cantidad_multiplicada = cantidad * x
        print(producto, ":", cantidad_multiplicada)
