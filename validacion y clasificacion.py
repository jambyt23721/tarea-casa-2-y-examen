l1 = float(input("Ingrese el primer lado: "))
l2 = float(input("Ingrese el segundo lado: "))
l3 = float(input("Ingrese el tercer lado: "))
if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    if l1 == l2 == l3:
        print("El triángulo es equilátero.")
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print("El triángulo es isósceles.")
    else:
        print("El triángulo es escaleno.")
else:
    print("Los valores ingresados no corresponden a un triángulo válido.")