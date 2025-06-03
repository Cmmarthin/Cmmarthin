#Ejercicio 6: Calculadora simple
#Descripción: Realiza suma, resta, multiplicación y división con dos números ingresados por el
#usuario.

a = float(input())
b = float(input())
print(a + b)
print(a - b)
print(a * b)
print(a / b if b != 0 else "Error")