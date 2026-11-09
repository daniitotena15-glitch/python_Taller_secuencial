
import math
print("Este programa calcula y muestra las funciones basicas de cualquier numero que se ingrese al sistema")
num = float (input("Ingresa por favor el numero al cual quieres calcuar las funciones "))
seno = math.sin (num)
coseno = math.cos (num)
tangente = math.tan (num)
rz = math.sqrt(num)
log_natu = math.log (num)
log_diez = math.log10 (num)

print (f"El seno del numero ingresado es: {seno:.4f}")
print (f"El coseno del numero ingresado es: {coseno:.4f}")
print (f"El tangente del numero ingresado es: {tangente:.4f}")
print (f"La raiz del numero ingresado es: {rz:.4f}" )
print ("El logaritmo natural del numero ingresado es: ", log_natu )
print ("El logaritmo en base 10 del numero ingresado es: ", log_diez)

## Importante: el f en el print sirve para agregar variables de forma visual mejor y en llaves
'''adicional se puede modifcar la salida de decimales que se requieran o no mostrar todas'''
