#  Validación compuesta múltiple
n = 6
valido = (n > 0) and ((n % 2 == 0) or (n % 3 == 0))
print("Cumple la condición:", valido)
