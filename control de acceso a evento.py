edad = int(input("Ingrese su edad: "))
documento = input("¿Tiene documento de identidad? (S/N): ")
if edad >= 18:
    if documento.upper() == "S":
        print("Puede ingresar al evento.")
    elif documento.upper() == "N":
        print("No puede ingresar al evento sin documento de identidad.")
    else:
        print("Rechazado eres Menor de edad.")