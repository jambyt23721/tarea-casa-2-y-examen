edad = int(input("Ingrese su edad: "))
if edad >= 18:
    teorico = input("¿Tiene licencia de conducir teórica? (S/N): ")
    if teorico == "S":
        print("Puede obtener la licencia de conducir práctica.")
        practico  = input("¿Ha aprobado el examen práctico? (S/N): ")
        if practico == "S":
            print("¡Felicidades! Ha obtenido la licencia de conducir.")
        else:
            print("No ha aprobado el examen práctico. No puede obtener la licencia de conducir.")
    else:
        print("No tiene licencia de conducir teórica. No puede obtener la licencia de conducir práctica.")
else:
    print("No tiene la edad mínima para obtener una licencia de conducir.")