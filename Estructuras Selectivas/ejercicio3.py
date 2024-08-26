# Solicita al usuario que ingrese el monto total de la compra y lo convierte a un número decimal (float).
montoDeLaCompra = float(input("La Compra: "))

# Define el porcentaje de la inversión propia, que es del 55%.
porcentajeInversionPropia = 0.55

# Define el porcentaje del préstamo bancario, que es del 30%.
porcentajePrestamoBancario = 0.30

# Define el porcentaje del crédito al fabricante, que es del 15%.
porcentajeCreditoFabricante = 0.15

# Verifica si el monto de la compra es mayor a 500,000.
if montoDeLaCompra > 500000:
    # Si es mayor a 500,000, calcula la inversión propia como el 55% del monto de la compra.
    inversionPropia = montoDeLaCompra * porcentajeInversionPropia
    
    # Calcula el préstamo bancario como el 30% del monto de la compra.
    prestamoBancario = montoDeLaCompra * porcentajePrestamoBancario
    
    # Calcula el crédito al fabricante como el 15% del monto de la compra.
    creditoFabricante = montoDeLaCompra * porcentajeCreditoFabricante
else:
    # Si el monto de la compra es 500,000 o menos, toda la compra es cubierta por la inversión propia.
    inversionPropia = montoDeLaCompra
    prestamoBancario = 0
    creditoFabricante = 0

# Muestra el monto total de la compra.
print(f"Monto total de la compra: ${montoDeLaCompra:.2f}")
# Muestra la inversión propia con su porcentaje correspondiente.
print(f"Inversión propia: ${inversionPropia:.2f} ({porcentajeInversionPropia * 100:.0f}%)")

# Muestra el monto del préstamo bancario con su porcentaje correspondiente.
print(f"Préstamo bancario: ${prestamoBancario:.2f} ({porcentajePrestamoBancario * 100:.0f}%)")

# Muestra el monto del crédito al fabricante con su porcentaje correspondiente.
print(f"Crédito al fabricante: ${creditoFabricante:.2f} ({porcentajeCreditoFabricante * 100:.0f}%)")
