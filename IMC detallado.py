peso = float(input("Ingrese tu peso en kg:"))
altura = float(input("Ingresa tu altura en metros:"))
imc = peso / (altura ** 2)
print(f"tu IMC es: {imc}")
if imc < 18.5:
    print("Clasificacion bajo peso")
elif imc < 25:
    print("Clasificacion normal.")
else:
    if imc < 30:
        print("Clasificacion sobrepeso")
    else:
        print("Clasificacion Obesidad")
