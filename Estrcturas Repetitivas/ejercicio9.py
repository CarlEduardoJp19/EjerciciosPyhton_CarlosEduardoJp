#Caclular el promedio de edades de hombres, mujeres y de todo un grupo de alumnos

#variables
edadesDeHombres = 0
edadesDeMujeres = 0
totalHombres = 0
totalMujeres = 0
totalEdades = 0
totalAlumnos = 0
#Solicitar cantidad de alumnos
cantidadDeAlumnos = int(input("Ingrese la cantidad de alumnos "))
#Recolectar las edades de cada alumno
for i in range(cantidadDeAlumnos):
    edad = int(input(f"Ingrese la edad {i + 1}: "))
    genero = (input("Ingrese el genero (H si es hombre y F para mujer)").upper())
    #Acumular la edad total
    totalEdades += edad
    totalAlumnos +=1
    #Analizar que genero es y ir acumulando las edades de los alumnos
if genero == 'H':
    edadesDeHombres += edad
    totalAlumnos +=1
elif genero == 'F':
    edadesDeMujeres += edad
    totalAlumnos +=1
#Aqui se calcula los promedios de hombre, mujer y todos los alumnos
print("Este genero no fue reconocido de manera que se ignorara este alumno")
promedioHombres = edadesDeHombres / totalHombres if totalHombres > 0 else 0
promedioMujeres = edadesDeMujeres / totalMujeres if totalMujeres > 0 else 0
promedioTotalAlumnos = totalEdades / totalAlumnos if totalAlumnos > 0 else 0
#Resultados de los promedios 
print(f"El promedio de las edades de los hombres es: {edadesDeHombres}")
print(f"El promedio de las edades de las mujeres es: {edadesDeMujeres}")
print(f"El promedio de las edades de los alumnos es: {totalAlumnos}")
