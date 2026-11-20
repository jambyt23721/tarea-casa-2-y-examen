num = int(input("Ingresa un numero entero:"))
if num >= 1 and num <= 100:
    if num % 10 == 0:
        if num > 50:
            print("Multiplo de 10 y mayor a 50")
        else:
            print("Multiplo de 10 pero menor o igual a 50")
    else:
        print("Esta en el rango pero no es multiplo de 10")

else:
    if num < 1:
        print("Fuera del rango. El numero es menor a 1")
    else:
        print("Fuera del rango. El numero es menor a 100")
        