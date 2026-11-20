ventas = float(input("Ingrese el monto de ventas del mes: "))
antiguedad = int(input("Ingrese la antigüedad del empleado en años: "))
if ventas > 5000:
    if antiguedad >= 5:
        bono = ventas * 0.08
        print(f"El empleado ha recibido un bono de ${bono:.2f} por sus ventas y antigüedad.")
    else:
        print("El empleado no cumple con los requisitos de antigüedad para recibir un bono.")
else:
    print("El empleado no ha alcanzado el umbral de ventas para recibir un bono.")