unidades = int(input("Ingresa las Unidades"))
precio = float(input("Ingresa el precio por unidad"))
pago = input("Metodo de pago (Efectivo/Tarjeta): ")

subtotal = unidades * precio

if unidades >= 10:
    subtotal = subtotal - (subtotal * 0.15)

elif unidades >= 5:
    subtotal = subtotal - (subtotal * 0.05)

    if pago == "Efectivo":
        subtotal += subtotal * 0.05

    elif pago == "Tarjeta":
        subtotal = subtotal

    else:
        print("Metodo de pago no valido")

        print("Total a pagar:", subtotal)