dinero = float(input("Ingresar Cantidad de dinero:"))
opcion = int(input("Elige una opcion(1:Agua 1.50 / Jugo 2.50)"))
if opcion == 1:
    if dinero >= 1.50:
        cambio = dinero - 1.50
        print(f"Producto entregado tu cambio es {cambio}")
    else:
        faltante = 1.50 - dinero
        print(f"Saldo insuficiente. Te faltan {faltante}")
elif opcion == 2:
    if dinero >= 2.50:
        cambio = dinero - 2.50
        print(f"Producto entregado tu cambio es {cambio}")
    else:
        faltante2 = 2.50 - dinero
        print(f"Saldo Insuficiente. te faltan {faltante2}")
else:
    print("Opcion no valida.")