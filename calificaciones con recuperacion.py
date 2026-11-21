nota1 = float(input("Ingresa tu primera Nota"))
nota2 = float(input("Ingresa tu segunda nota"))

promedio = (nota1 + nota2) / 2

print("promedio", promedio)

if promedio >= 70:
    print("Aprobado!")
elif promedio >= 50:
    recuperacion = float(input("Ingresa la nota de recuperacion:"))

    if recuperacion >= 70:
        print("Aprobado con Recuperacion")
    else:
        print("Reprobado")

else:
    print("Reprobado Directamente")