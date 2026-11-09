
print ("Este programa realiza una conversion de unidades de medicion (centimetros, metros,pies, pulgadas, yardas) , a partir de el ingreso de un valor")
cen = float (input("Ingrese el valor a convertir a centimetros "))
yar = cen/91.44
met = cen/100
pie= cen/30.48
pulg = cen/2.54

print ("Los resultados de las conversiones del valor indicado en centimetros fue de: ", cen )
print()
print ("metros: ", met)
print()
print ("pies: ", pie)
print()
print ("pulgadas: ",pulg)
print()
print ("Yardas: ", yar)