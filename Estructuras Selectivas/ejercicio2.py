#DescuentoDeZapatillas
zapatillas = int(input("Digite el número de zapatillas compradas "))

# Verifica cuántas zapatillas se compraron y procede según el número.
if zapatillas == 1:
    # Solicita el costo de una zapatilla.
    zapatilla1 = int(input("Digite el costo de la zapatilla "))
    # El total es igual al costo de esa zapatilla.
    total = zapatilla1
elif zapatillas == 2:
    # Solicita el costo de cada una de las dos zapatillas.
    zapatilla1 = int(input("Digite el costo de la primera zapatilla "))
    zapatilla2 = int(input("Digite el costo de la segunda zapatilla "))
    # Suma los costos de las dos zapatillas para obtener el total.
    total = zapatilla1 + zapatilla2
elif zapatillas == 3:
    # Solicita el costo de cada una de las tres zapatillas.
    zapatilla1 = int(input("Digite el costo de la primera zapatilla "))
    zapatilla2 = int(input("Digite el costo de la segunda zapatilla "))
    zapatilla3 = int(input("Digite el costo de la tercera zapatilla "))
    # Suma los costos de las tres zapatillas para obtener el total.
    total = zapatilla1 + zapatilla2 + zapatilla3
elif zapatillas == 4:
    # Solicita el costo de cada una de las cuatro zapatillas.
    zapatilla1 = int(input("Digite el costo de la primera zapatilla "))
    zapatilla2 = int(input("Digite el costo de la segunda zapatilla "))
    zapatilla3 = int(input("Digite el costo de la tercera zapatilla "))
    zapatilla4 = int(input("Digite el costo de la cuarta zapatilla "))
    # Suma los costos de las cuatro zapatillas para obtener el total.
    total = zapatilla1 + zapatilla2 + zapatilla3 + zapatilla4
elif zapatillas == 5:
    # Solicita el costo de cada una de las cinco zapatillas.
    zapatilla1 = int(input("Digite el costo de la primera zapatilla "))
    zapatilla2 = int(input("Digite el costo de la segunda zapatilla "))
    zapatilla3 = int(input("Digite el costo de la tercera zapatilla "))
    zapatilla4 = int(input("Digite el costo de la cuarta zapatilla "))
    zapatilla5 = int(input("Digite el costo de la quinta zapatilla "))
    # Suma los costos de las cinco zapatillas para obtener el total.
    total = zapatilla1 + zapatilla2 + zapatilla3 + zapatilla4 + zapatilla5
else:
    # Si el número de zapatillas no es válido, muestra un mensaje.
    print("Digite otro número")

# Aplica un descuento dependiendo de la cantidad de zapatillas compradas.
if zapatillas >= 3:
    # Si se compraron 3 o más zapatillas, aplica un descuento del 20%.
    descuento = total * 0.20
else:
    # Si se compraron menos de 3 zapatillas, aplica un descuento del 10%.
    descuento = total * 0.10

# Calcula el total a pagar después de aplicar el descuento.
totalAPagar = total - descuento

# Muestra el total a pagar con el descuento aplicado.
print(f"Su total a pagar con el descuento aplicado es {totalAPagar}")
# Muestra el total original sin descuento.
print(f"Su total a pagar sin el descuento era de {total}")

# Muestra el monto del descuento aplicado.
print(f"Su descuento es de {descuento}")