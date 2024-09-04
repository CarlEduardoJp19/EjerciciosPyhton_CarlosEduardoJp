# Inicialización de contadores para los diferentes colores de calcomanía.
amarillo = 0  # Contador para los autos con calcomanía amarilla.
rosa = 0      # Contador para los autos con calcomanía rosa.
roja = 0      # Contador para los autos con calcomanía roja.
verde = 0     # Contador para los autos con calcomanía verde.
azul = 0      # Contador para los autos con calcomanía azul.

# Solicitar al usuario la cantidad de autos que ingresaron a la ciudad de Ibagué.
n = int(input("Ingrese la cantidad de autos que ingresaron a la ciudad de Ibagué: "))

# Bucle que se repite "n"  para ingresar el último dígito de la placa de cada auto.
for i in range(n):
    # Solicitar al usuario el último dígito de la placa del auto que esta conduciendo.
    digito = int(input(f"Ingrese el último dígito de la placa del auto {i + 1}: "))
    
    # Verificar el dígito y actualizar el contador del color correspondiente.
    if digito == 1 or digito == 2:
        amarillo += 1  # Si el dígito es 1 o 2, incrementa el contador de amarillo.
    elif digito == 3 or digito == 4:
        rosa += 1      # En caso de que el dígito es 3 o 4, incrementa el contador de rosa.
    elif digito == 5 or digito == 6:
        roja += 1      # En caso de que el dígito es 5 o 6, incrementa el contador de roja.
    elif digito == 7 or digito == 8:
        verde += 1     # En caso de que el dígito es 7 o 8, incrementa el contador de verde.
    elif digito == 9 or digito == 0:
        azul += 1      # En caso de que el dígito es 9 o 0, incrementa el contador de azul.
    else:
        # Imprime un mensaje de error si el dígito no está en el rango de 0 a 9.
        print("Número no válido, ingrese un número entre 0 y 9")

# Muestra el total de autos para cada color de calcomanía.
print("\nCantidad de autos por calcomanía de color:")
print(f"Amarillo: {amarillo}")  # Muestra cuántos autos tienen calcomanía amarilla en la ciudad de Ibagué.
print(f"Rosa: {rosa}")          # Muestra cuántos autos tienen calcomanía rosa en la ciudad de Ibagué.
print(f"Roja: {roja}")          # Muestra cuántos autos tienen calcomanía roja en la ciudad de Ibagué.
print(f"Verde: {verde}")        # Muestra cuántos autos tienen calcomanía verde en la ciudad de Ibagué.
print(f"Azul: {azul}")          # Muestra cuántos autos tienen calcomanía azul en la ciudad de Ibagué.