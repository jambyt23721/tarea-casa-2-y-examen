monto = float(input("Ingrese el monto de la compra: "))
zona = input("Ingrese la zona de envío (Urbana, Rural): ")
if monto > 50:
    if zona.lower() == "urbana":
        costo_envio = 5
    elif zona.lower() == "rural":
        costo_envio = 10
    else:
        print("Zona de envío no válida.")
        costo_envio = 0
else:
    costo_envio = 0
print(f"El costo de envío es: ${costo_envio}")
print(f"El total a pagar es: ${monto + costo_envio}")