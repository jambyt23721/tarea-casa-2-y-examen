porcentaje = int(input("Ingrese el porcentaje de batería restante (0-100): "))
conectado = input("¿Está conectado a la corriente? (S/N): ")
if porcentaje < 20:
    if conectado.upper() == "S":
        print("La batería se está cargando.")
    else:
        print("Advertencia: La batería está baja. Conéctese a la corriente.")
elif porcentaje == 100:
    print("La batería está completamente cargada.")
    if  conectado.upper() == "S":
        print("Desconecte el cargador para evitar sobrecarga.")
    else:
        print("Puede usar el dispositivo normalmente")