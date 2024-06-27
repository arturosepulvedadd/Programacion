capitales = {}

for x in range(5):
    capital = input("Ingrese una capital a su elección (Debe ingresar 5): ")
    pais = input("Ingrese el país correspondiente a la capital: ")
    capitales[capital] = pais
    
turista = input("Ingrese el nombre de un turista: ")
capt_procedencia = input("Ingrese su capital de procedencia: ")

if capt_procedencia in capitales:
        pais = capitales[capt_procedencia]

print("El turista con el nombre", turista, "viene de la capital", capt_procedencia, "y su país es", pais)