def mostrar_menu():
    print("1. Ingresar un elemento a la lista")
    print("2. Modificar un elemento de la lista")
    print("3. Eliminar un elemento de la lista según el índice")
    print("4. Eliminar el último elemento de la lista")
    print("5. Buscar un elemento de la lista (devuelve el índice)")
    print("6. Mostrar todos los elementos de la lista")
    print("7. Salir")

def main():
    lista = []
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-7): ")
        
        if opcion == "1":
            lista.append(input("Ingrese el elemento a agregar a la lista: "))
            print("Elemento agregado a la lista.")
        elif opcion == "2":
            if lista:
                indice = int(input("Ingrese el índice del elemento a modificar: "))
                if 0 <= indice < len(lista):
                    lista[indice] = input("Ingrese el nuevo valor del elemento: ")
                    print("Elemento modificado.")
                else:
                    print("Índice fuera de rango.")
            else:
                print("La lista está vacía.")
        elif opcion == "3":
            if lista:
                indice = int(input("Ingrese el índice del elemento a eliminar: "))
                if 0 <= indice < len(lista):
                    print(f"Elemento '{lista.pop(indice)}' eliminado de la lista.")
                else:
                    print("Índice fuera de rango.")
            else:
                print("La lista está vacía.")
        elif opcion == "4":
            if lista:
                print(f"Elemento '{lista.pop()}' eliminado de la lista.")
            else:
                print("La lista está vacía.")
        elif opcion == "5":
            elemento = input("Ingrese el elemento a buscar: ")
            if elemento in lista:
                print(f"El elemento '{elemento}' se encuentra en el índice {lista.index(elemento)}.")
            else:
                print("El elemento no se encuentra en la lista.")
        elif opcion == "6":
            if lista:
                print("Elementos de la lista:")
                for indice, elemento in enumerate(lista):
                    print(f"{indice}: {elemento}")
            else:
                print("La lista está vacía.")
        elif opcion == "7":
            print("Salida")
            break
        else:
            print("Opción errónea")

