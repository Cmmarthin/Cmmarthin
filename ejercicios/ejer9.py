# Incremento/decremento según paridad
#Si una variable n es par, suma 1. Si es impar, réstale 1. Imprime el nuevo valor.
n = 7
if n % 2 == 0:
    n += 1
else:
    n -= 1
print("Nuevo valor:", n)
