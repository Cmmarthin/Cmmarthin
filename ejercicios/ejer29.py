#  Contraseña segura
password = "abc12345"
segura = len(password) > 8 and any(char.isdigit() for char in password)
print("Contraseña segura:", segura)
