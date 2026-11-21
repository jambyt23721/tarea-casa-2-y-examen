x = float(input("Ingresa X:"))
y = float(input("Ingresa Y:"))

if x == 0:
    if y == 0:
        print("Esta en el origen")
    else:
        print("Esta en el eje Y")
elif x > 0:
    if y > 0:
        print("Cuadrante I")
    elif y < 0:
        print("Cuadrante IV")
    else:
        print("Esta en el eje X")
else:
    if y > 0:
        print("Cuadrante III")
    else:
        print("Esta en el eje X")
        
