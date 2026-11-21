edad = int(input("Ingresa tu edad"))
ingreso = float(input("Ingresa tu ingreso Mensual"))
historial = input("Tienes historial limpio? (si/no):")

if edad > 21 and edad < 65:
    if ingreso >= 1500:
        if historial == "si":
            print("Credito Aprobado!.")
        else:
            print("Puedes Obtener credito con Aval")
    else:
        print("Ingreso insuficiente")
else:
    print("Edad no valida.")
