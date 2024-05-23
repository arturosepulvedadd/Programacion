total_preguntas = int(input("Ingrese el total de preguntas realizadas: "))
preguntas_correctas = int(input("Ingrese la cantidad de preguntas contestadas correctamente: "))
porcentaje_correctas = (preguntas_correctas * 100) / total_preguntas
print("El postulante obtuvo un", porcentaje_correctas,"% de respuestas correctas")
nivel_obtenido = (porcentaje_correctas)
if porcentaje_correctas >= 95:
    print("Obtuvo el nivel máximo")
elif 70 <= porcentaje_correctas < 95:
    print("Obtuvo el nivel medio")
elif 40 <= porcentaje_correctas < 70:
    print("Obtuvo el nivel regular")
else:
    print("Está fuera de nivel")