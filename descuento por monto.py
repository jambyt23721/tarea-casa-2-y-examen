monto = float(input("Ingrese el monto de la compra: "))
membresia = input("Tienes membresia (S/N): ")
if monto >= 100:
    descuento = monto * 0.10
    if membresia == "Si":
        descuento = descuento + (monto * 0.05)
    total = monto - descuento
    print(f"El monto de la compra es: {monto}")
    print(f"El descuento es: {descuento}")
    print(f"El total a pagar es: {total}")
else:
    print(f"Sin descuento. total a pagar es: {monto}")