pin = 1234
saldo = 1000

clave = int(input("Ingresa tu PIN"))

if clave == pin:
    opcion = int(input("1. Consultar Saldo 2. Retirar Dinero"))

    if opcion == 1:
        print(f"Tu saldo es:{saldo}")
    elif opcion == 2:
        retiro = int(input("Cuanto desea retirar?:"))

        if retiro > 0:
            if retiro % 10 == 0:
                if retiro <= saldo:
                    saldo -= retiro
                    print("Retiro Exitoso")
                    print("Saldo Actualizado", saldo)
                else:
                    print("Saldo insuficiente")
            else:
                print("El retiro debe ser multiplo de 10")
        else:
            print("cantidad no valida")
    else:
        print("Opcion no valida")
else:
    print("PIN incorrecto.")

        


                
