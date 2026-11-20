nota = float(input("Ingrese la nota del estudiante (0-100): "))
asistencia = float(input("Ingrese el % de asistencia: "))
if nota >= 60:
    if asistencia >= 75:
        print("El estudiante ha aprobado la materia.")
    else:
        print("El estudiante no ha aprobado la materia debido a la baja asistencia.")
else:
    print("El estudiante no ha aprobado la materia debido a la baja nota.")
    if asistencia >= 75:
        print("Reprobado por nota insuficiente.")
    else:
        print("Reprobado por nota insuficiente y baja asistencia.")
