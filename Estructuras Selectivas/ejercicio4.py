#Supermercado
# Lista de descuentos por color de boleta.
descuentosBoletas = [
    {"color": "rojo", "descuento": 0.15},
    {"color": "verde", "descuento": 0.20}
]

# Solicita al usuario que ingrese el total de la compra y lo convierte a un número decimal (float).
totalCompra = float(input('Total de la compra: '))

# Solicita al usuario que ingrese el color de la boleta y lo convierte a minúsculas.
colorDeLaBoleta = input("Ingrese el color de la boleta (rojo, verde, otro color): ").strip().lower()

# Verifica el color de la boleta y asigna el porcentaje de descuento correspondiente.
if colorDeLaBoleta == 'rojo':
    # Si el color es rojo, asigna un descuento del 15%.
    porcentajeDelDescuento = 0.15
elif colorDeLaBoleta == 'verde':
    # Si el color es verde, asigna un descuento del 20%.
    porcentajeDelDescuento = 0.20
else:
    # Si el color no es rojo ni verde, no se aplica descuento.
    porcentajeDelDescuento = 0.00

# Calcula el valor del descuento basado en el porcentaje del descuento y el total de la compra.
descuento = totalCompra * porcentajeDelDescuento

# Calcula el total a pagar después de aplicar el descuento.
totalConDescuento = totalCompra - descuento

# Muestra el total de la compra.
print(f"Total de la compra: ${totalCompra:.2f}")
# Muestra el color de la boleta con la primera letra en mayúscula.
print(f"El color de la boleta: {colorDeLaBoleta.capitalize()}")

# Muestra el valor del descuento aplicado.
print(f"El valor del descuento: ${descuento:.2f}")

# Muestra el total a pagar con el descuento aplicado.
print(f"El total con descuento es: ${totalConDescuento:.2f}")