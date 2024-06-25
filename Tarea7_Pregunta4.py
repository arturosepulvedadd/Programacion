deudores = {
    "12345678-0": 3000,
    "12345679-1": 7000,
    "12345670-2": 12000,
    "12345677-3": 5000,
    "12345676-4": 10000
    }

while True:
    rut = input("\nIngrese el RUT del deudor para abonar (Enter para finalizar): ").strip()
    if rut == "":
        break
    
    if rut in deudores:
        monto_abono = float(input("Ingrese el monto del abono para", rut, ": "))
        deudores[rut] -= monto_abono
        
        if deudores[rut] <= 0:
            del deudores[rut]
            
            print("Abono realizado correctamente. Saldo restante para", rut, ":", deudores.get(rut, 0))
        else:
            print("No se encontró el RUT", rut, "en la lista de deudores")

print("\nDeudores restantes:")

for rut, saldo in deudores.items():
    print("RUT: ", rut, "- Saldo deuda:", saldo)
