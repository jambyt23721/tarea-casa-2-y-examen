user_correcto = "admin"
password_correcta = "123456"
user_ingresado = input("Ingrese su usuario: ")
if user_ingresado == user_correcto:
    password_ingresada = input("Ingrese su contraseña: ")
    if password_ingresada == password_correcta:
        print("Acceso concedido.")
    else:
        print("Contraseña incorrecta. Acceso denegado.")
else:
    print("Usuario incorrecto. Acceso denegado.")