edad = int(input("Ingrese su edad: "))
dia = input("Ingrese el día de la semana (Lunes, Martes, Miércoles, Jueves, Viernes, Sábado, Domingo): ")
if edad < 12 or edad >= 65:
    tarifa = 5.00
else:
    tarifa = 10.00
    if dia == "Miércoles":
        tarifa = tarifa * 0.5
        print(f"Tarifa con descuento del 50% por ser miércoles: ${tarifa:.2f}")