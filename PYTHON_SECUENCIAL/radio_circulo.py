
import math

print ("Este programa te ayudara a calcular el area y perimetro de un circulo, apartir del valor de un radio ")
radio = float(input("Ingrese por favor, el valor el radio "))
area = math.pi * (radio)**2
peri = 2*math.pi*radio
print ("El area del circulo es : ", area)
print ("El perimetro del circulo es : ", peri)