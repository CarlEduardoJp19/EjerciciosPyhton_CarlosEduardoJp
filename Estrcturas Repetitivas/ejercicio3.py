#Variables

sumarCalificaciones = 0
maximaCalificaciones = 0
minimmaCalificaciones = 999
# Bucle que itera 20 veces para ingresar las calificaciones de 20 alumnos
for i in range (20):

    calificacion = int(input("Ingrese la calificacion del alumno: "))
    sumarCalificaciones += calificacion
    if calificacion > maximaCalificaciones:
        maximaCalificaciones = calificacion
    if calificacion < minimmaCalificaciones:
        minimmaCalificaciones = calificacion
#Calcula el promedio de las calificaciones
promedio = sumarCalificaciones / 20
#Imprimir resultados
print(f"El promedio de las calificaciones es: {promedio}")
print(f"La calificación más alta es: {maximaCalificaciones}")
print(f"La calificación más baja es: {minimmaCalificaciones}")
