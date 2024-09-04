#Solicitar al usuario el número para la tabla de multiplicar
numero = int(input("Ingrese el número para la tabla de multiplicar: "))
#Inicializar el múltiplo en 1
multiplo = 1
#Bucle para imprimir la tabla de multiplicar
while multiplo <= 10:
    ## Calcular el resultado de la multiplicación
    resultado = numero * multiplo
    #Imprimir el resultado
    print(f"{numero} x {multiplo} = {resultado}")
    #Uncrementa el multiplo
    multiplo +=1