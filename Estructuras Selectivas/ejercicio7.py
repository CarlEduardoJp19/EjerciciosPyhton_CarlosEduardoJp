def calcularTotalLlantas(cantidad):
    """
    Calcula el total a pagar según la cantidad de llantas compradas.
    
    Parámetros:
        cantidad (int): Número de llantas a comprar.
        
    Retorna:
        int: Total a pagar por las llantas.
    """
    # Define el precio por llanta según la cantidad comprada.
    if cantidad < 5:
        # Si la cantidad es menor a 5, el precio por llanta es 300,000.
        precioPorLlanta = 300000
    elif 5 <= cantidad <= 10:
        # Si la cantidad está entre 5 y 10, el precio por llanta es 250,000.
        precioPorLlanta = 250000
    else:
        # Si la cantidad es mayor a 10, el precio por llanta es 200,000.
        precioPorLlanta = 200000
        
    # Calcula el total a pagar multiplicando la cantidad por el precio por llanta.
    total = cantidad * precioPorLlanta
    
    # Retorna el total a pagar.
    return total

# Solicita al usuario la cantidad de llantas a comprar.
try:
    cantidadLlantas = int(input("Ingrese la cantidad de llantas a comprar: "))
    
    # Verifica si la cantidad de llantas es positiva.
    if cantidadLlantas <= 0:
        print("La cantidad de llantas debe ser un número positivo.")
    else:
        # Llama a la función calcularTotalLlantas con la cantidad ingresada.
        totalAPagar = calcularTotalLlantas(cantidadLlantas)
        
        # Muestra el total a pagar, formateado con comas para miles.
        print(f"El total a pagar por {cantidadLlantas} llanta(s) es: ${totalAPagar:,}")
except ValueError:
    # Maneja el caso en que el usuario ingresa un valor que no puede convertirse a entero.
    print("Por favor, ingrese un número válido para la cantidad de llantas.")