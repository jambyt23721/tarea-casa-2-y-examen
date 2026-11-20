temp = float(input("Ingrese la temperatura en grados Celsius: "))
if temp < 0:
    print("El estado físico del agua es sólido (hielo).")
elif temp > 100:
    print("El estado físico del agua es gaseoso (vapor).")
else:
    print("El estado físico del agua es líquido (agua).")