#PromedioDe3notas 

# Solicita al usuario que ingrese la primera calificación y la convierte a un número entero.
calificacion1 = int(input("Digite la primera nota "))

# Solicita al usuario que ingrese la segunda calificación y la convierte a un número entero.
calificacion2 = int(input("Digite la segunda nota "))

# Solicita al usuario que ingrese la tercera calificación y la convierte a un número entero.
calificacion3 = int(input("Digite la tercera nota "))

# Calcula el promedio de las tres calificaciones sumándolas y dividiéndolas por 3.
total = (calificacion1 + calificacion2 + calificacion3) / 3

# Verifica si el promedio (total) es mayor o igual a 70.
if total >= 70:
    # Si el promedio es 70 o más, imprime que el usuario pudo aprobar la materia de algoritmia.
    print("Usted pudo aprobar algoritmia")
else:
    # Si el promedio es menor a 70, imprime que el usuario no aprobó la materia de algoritmia.
    print("Usted no ha aprobado algoritmia")