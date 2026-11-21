origen = input("Escala origen (C/F/K): ")
valor = float(input("Ingresa la temperatura"))
destino = input("Escala destino (C/F/K): ")

if origen == "C":
    if valor >= -273.15:
        if destino == "F":
            resultado = (valor * 9 / 5) + 32
        elif destino == "K":
            resultado = valor + 273.15
        elif destino == "C":
            resultado = valor
        else:
            resultado = 0
            print("Escala destino no valida")

    else:
        resultado = 0
        print("Temperatura menor al cero absoluto")

elif origen == "F":
    if valor >= -459.67:
        if destino == "C":
            resultado = (valor - 32) * 5 / 9
        elif destino == "K":
            resultado = (valor + 459.67) * 5 / 9
        elif destino == "F":
            resultado = valor
        else:
            resultado = 0
            print("Escalada destino No valida")

    else:
        resultado = 0
        print("Temperatura menor al cero absoluto")

elif origen == "K":
    if valor >= 0:
        if destino == "C":
            resultado = valor - 273.15
        elif destino == "F":
            resultado = (valor * 9 / 5) - 459.67
        elif destino == "K":
            resultado = valor
        else:
            resultado = 0
            print("Escalada destino no valida.")

    else:
        resultado = 0
        print("Temperatura menor al cero absoluto")

else:
    resultado = 0
    print("Escala origen no valida.")

    print("Resultado", resultado)
