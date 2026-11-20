vehiculo = input("Tipo de Vehiculo: (Moto/Auto)")
horas = int(input("Cantidad de horas:"))
total = 0
if vehiculo == "moto":
    if horas <= 2:
        total = 2
    else:
        total = 2 + (horas - 2) * 1
elif vehiculo == "auto":
    if horas <= 2: 
     total = 4
else:
    total = 4 + (horas - 2) * 2
    print(f"Total a pagar por estacionamiento:{total}")