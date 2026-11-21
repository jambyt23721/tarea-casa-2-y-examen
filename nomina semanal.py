tarifa = float(input("Ingresa la tarifa Por horas"))
horas = float(input("Ingresa las horas trabajadas"))
turno = input("Turno (Diurno/nocturno):")

if horas <= 40:
    total = tarifa * horas

elif horas <= 50:
    total = tarifa * 40
    total += (horas - 40) * tarifa * 1.5

else:
    total = tarifa * 40
    total += 10 * tarifa * 1.5
    total += (horas - 50) * tarifa * 2

    if turno  == "nocturno":
        total *= 1.10

        print(f"Pago semanal:", total)