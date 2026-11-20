boleto = input("Ingrese el tipo de boleto (Económico/Ejecutivo): ")
peso = float(input("Ingrese el peso del equipaje en kg: "))
cobro_extra = 0.0
if boleto == "Económico":
    if peso > 20:
        cobro_extra = (peso - 20) * 10
elif boleto == "Ejecutivo":
    if peso > 30:
        cobro_extra = (peso - 30) * 15
        print(f"El cobro extra por equipaje es: ${cobro_extra:.2f}")