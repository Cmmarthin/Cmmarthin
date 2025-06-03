#Ejercicio 9: Verificar si un número es múltiplo de otro
#Descripción: Pide dos números y determina si el primero es múltiplo del segundo.
a = int(input())
b = int(input())
print("Múltiplo" if b != 0 and a % b == 0 else "No es múltiplo")