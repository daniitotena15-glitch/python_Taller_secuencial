
# Programa para practicar F-Strings

print("===== PRACTICA DE F-STRINGS =====")
print()

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
salario = float(input("Ingrese su salario: "))

print()

# 1. Mostrar variables dentro del texto
print(f"Hola {nombre}, tienes {edad} años.")

# 2. Mostrar una operación matemática
print(f"El próximo año tendrás {edad + 1} años.")

# 3. Mostrar decimales
print(f"Tu salario es: ${salario:.2f}")

# 4. Mostrar porcentaje
ahorro = 0.15
print(f"Tu porcentaje de ahorro es del {ahorro:.0%}")

# 5. Mostrar miles separados
print(f"Tu salario con separador de miles es: ${salario:,.2f}")

# 6. Mostrar nombre y valor de la variable
print(f"{salario=}")

# 7. Realizar cálculos dentro del print
salario_anual = salario * 12

print(f"Tu salario anual aproximado es: ${salario_anual:,.2f}")

# 8. Mezclar texto y cálculo
print(
    f"Si recibes un aumento del 10%, "
    f"tu nuevo salario será de ${salario * 1.10:,.2f}"
)

print()
print("===== FIN DEL PROGRAMA =====")