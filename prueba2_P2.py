cambio_usd = 950

lista = []

for x in range(10):
       precio_clp = int(input("Ingrese 10 precios en pesos chilenos: "))
       lista.append(precio_clp/cambio_usd) 
           
print("Precios convertidos a dolares respectivamente:", lista,)