
import math
print ("Este programa calcula por medio de dos catetos de un triangulo su hipotenusa")
print()
cat1=float(input("Ingrese por favor el primer dato (Primer cateto) "))
cat2= float(input("Ingrese por favor el segundo dato (Segundo cateto) "))
hipo= math.sqrt (cat1**2+ cat2**2)
print ("La hipotenusa del triangulo es : ", hipo)