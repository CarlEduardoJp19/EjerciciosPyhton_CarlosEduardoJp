#Calcule el precio final de una compra
valor_delacompra= int (input("digite el valor de la compra: "))
valor_deldescuento= int (input("digite el descuento: "))

descuento = (valor_delacompra * valor_deldescuento) /100;
total = valor_delacompra-descuento;
print("La compra fue", valor_delacompra);
print("Con un descuento de", valor_deldescuento);
print("El valor final a pagar es", total);
