#Grupo de 23 estudiantes
#contadores para las diferentes variables
caliMenor50 = 0
caliEntre50Y70 = 0
caliEntre70Y80 = 0
caliMayorDe80 = 0
#Bucle que se repite 5 veces para solicitar las calificaciones de los estudiantes.
for i in range(5):
    caliDelEstudiante = float(input(f"Ingrese la calificacion del estudiante {i + 1}: "))
    #Condicional para verificar si es menor a 50.
    if caliDelEstudiante < 50:
        caliMenor50 +=1
    #Verifica si está entre 50 y 70, incluidos 50 pero no 70.
    elif 50 <= caliDelEstudiante < 70:
        caliEntre50Y70 +=1
    # Verifica si está entre 70 y 80, incluidos 70 pero no 80.
    elif 70 <= caliDelEstudiante < 80:
        caliEntre70Y80 +=1
    #En caso de que no entra en ninguno de los rangos anteriores, es mayor o igual a 80.
    else:
        caliMayorDe80 +=1
#los resultados de los contadores para cada variable
print(f"Las calificaciones menor a 50: {caliMenor50}: ")
print(f"Las calificaciones entre 50 y 70: {caliEntre50Y70}: ")
print(f"Las calificaciones entre 70 y 80: {caliEntre70Y80}: ")
print(f"Las calificaciones mayor de 80: {caliMayorDe80}: ")