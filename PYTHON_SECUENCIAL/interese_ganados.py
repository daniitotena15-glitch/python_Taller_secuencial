
print("Este programa calcula el valor de interes y desceuntpos por ley que se dben hacer para el final inidcar cual es el total a pagar segun el sueldo ingresado")
canti= float (input("Por favor ingrese tu cantidad "))
interes= float(input("Por favor ingrese el porcentaje de interes "))
periodo = int (input("Por favor ingresar el periodo "))
valor_interes=(canti*interes*periodo)/360
impuesto= valor_interes*0.07
total_pagar = (canti+valor_interes)- impuesto
print("El valor del interes es : ", valor_interes)
print ()
print("La totalidad a recibir es : ", total_pagar)
