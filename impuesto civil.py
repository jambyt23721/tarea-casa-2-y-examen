estado = input("Estado civil (soltero/casado):")
ingreso = float(input("Ingrese su ingreso anual:"))

if estado == "soltero":
    if ingreso <= 20000:
        impuesto = ingreso * 0.10
    else:
        impuesto = ingreso * 0.20
elif estado == "casado":
    if ingreso <= 35000:
        impuesto = ingreso * 0.08
    else:
        impuesto = ingreso * 0.15
else:
    impuesto = 0
    print("Estado Civil no valido.")

    neto =  ingreso - impuesto

    print("impuesto", impuesto)
    print("ingreso neto", neto)