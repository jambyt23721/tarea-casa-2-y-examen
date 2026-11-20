num = int(input("Ingrese un numero entero: "))
if num % 2 == 0:
    print(f"El número {num} es divisible entre 2.")
elif num % 3 == 0:
    print(f"El número {num} es divisible entre 3.")
elif num % 5 == 0:
    print(f"El número {num} es divisible entre 5.")
else:
    print(f"El número {num} no es divisible entre 2, 3 o 5.")