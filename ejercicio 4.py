sueldos_menores = 0
sueldos_mayores = 0
total_sueldos = 0
while True:
        sueldo = int(input("Ingrese el sueldo del empleado (-1 para terminar): "))
        if sueldo == -1:
            break
        total_sueldos += sueldo
        if 500000 <= sueldo <= 900000:
            sueldos_menores += 1
        elif sueldo > 900000:
            sueldos_mayores += 1
print("Empleados que ganan entre $500.000 y $900.000:", sueldos_menores)
print("Empleados que ganan más de $900.000:", sueldos_mayores)
print("La empresa gasta un total de $", total_sueldos, "en sueldos.")