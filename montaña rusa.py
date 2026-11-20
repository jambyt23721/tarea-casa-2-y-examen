estatura = int(input("Ingresa tu Estatura en cm"))
if estatura >= 140:
    print("Acceso Permitido.")
elif estatura >= 120:
    adulto = input("Vienes acompañado de un  Adulto? (S/N):")
    if adulto == "S":
        print("Acceso Permitido Con Adulto")
    else:
        print("Acceso denegado. Requieres un Adulto.")
else:
    print("Acceso denegado estatura insuficiente.")
