#Calcule sueldo total de un vendedor
nombre= input("digite su nombre: ") #
sueldo=int (input("digite el sueldo: ")) #
comision=int (input("digite la comision : ")) #
ventasrealizadas=int(input("digite las ventas realizadas: ")) #
comisiones= (ventasrealizadas/100) * comision; #
sueldo_final = comisiones + sueldo; #
print("Informe del vendedor:")
print("El nombre del vendedor", nombre); #
print("El sueldo del vendedor es", sueldo); #
print("La comisión del vendedor es", comisiones); #
print("Las ventas realizadas son", ventasrealizadas); #
print("Sueldo final es",sueldo_final); #
