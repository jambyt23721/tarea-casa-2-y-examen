cliente = input("Tipo de Cliente (residencial/comercial):")
kWh = float(input("Ingresa tu kWh consumidos:"))

if cliente == "residencial":
    if kWh <= 100:
        costo = kWh * 0.15
    else:
        costo = 100 *  0.15 + (kWh - 100) * 0.25

elif cliente == "comercial":
    if kWh <= 200:
        costo = kWh * 0.20
    else:
        costo = 200 * 0.20 + (kWh - 200) * 0.35

else:
    costo = 0
    print("Cliente no valido")

    print("Total a pagar:", costo)
