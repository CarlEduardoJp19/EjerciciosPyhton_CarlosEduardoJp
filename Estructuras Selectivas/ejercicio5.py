# Define una función para calcular las pulsaciones basadas en el sexo y la edad.
def calcularPulsaciones(sexo, edad):
    # Convierte el sexo a minúsculas para hacer la comparación insensible a mayúsculas/minúsculas.
    if sexo.lower() == "femenino":
        # Calcula las pulsaciones para el sexo femenino utilizando la fórmula dada.
        pulsaciones = (220 - edad) / 10
    elif sexo.lower() == "masculino":
        # Calcula las pulsaciones para el sexo masculino utilizando la fórmula dada.
        pulsaciones = (210 - edad) / 10
    else:
        # Retorna un mensaje de error si el sexo no es válido.
        return "Sexo no válido. Por favor, ingresa 'femenino' o 'masculino'."
    
    # Retorna el número de pulsaciones calculado.
    return pulsaciones

# Solicita al usuario que ingrese el sexo (femenino/masculino).
sexo = input("Ingresa el sexo (femenino/masculino): ")

# Solicita al usuario que ingrese la edad y la convierte a un número entero.
edad = int(input("Ingresa la edad: "))

# Llama a la función calcularPulsaciones con el sexo y la edad ingresados por el usuario.
pulsaciones = calcularPulsaciones(sexo, edad)

# Imprime el número de pulsaciones por cada 10 segundos.
print(f"El número de pulsaciones por cada 10 segundos es: {pulsaciones}")