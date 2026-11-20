print("=== AVENTURA EN EL BOSQUE OSCURO ===")
print("Estás caminando por un bosque oscuro y encuentras dos objetos: un FÓSFORO y una LINTERNA.")

lvl1 = input("¿Con cuál te quedas? (FÓSFORO / LINTERNA): ")

if lvl1 == "FÓSFORO" or lvl1 == "FOSFORO" or lvl1 == "fósforo" or lvl1 == "fosforo" or lvl1 == "Fósforo" or lvl1 == "Fosforo":
    print("Coges el fósforo y lo enciendes. Por un instante, el bosque se ilumina... ¡y ves un gran oso grizzly! El fósforo se apaga.")
    
    lvl2 = input("¿Qué haces ahora? (CORRER / ESCONDERTE): ")
    
    if lvl2 == "ESCONDERTE" or lvl2 == "esconderte" or lvl2 == "Esconderte":
        print("Te escondes detrás de un árbol grueso. El oso olfatea el aire, pero sigue de largo. Ves una cabaña a lo lejos y un río.")
        
        lvl3 = input("¿Hacia dónde vas? (CABAÑA / RÍO): ")
        
        if lvl3 == "CABAÑA" or lvl3 == "CABANA" or lvl3 == "cabaña" or lvl3 == "cabana" or lvl3 == "Cabaña" or lvl3 == "Cabana":
            print("Llegas a la cabaña de madera. La puerta está entreabierta, pero también hay una ventana rota.")
            
            lvl4 = input("¿Por dónde entras? (PUERTA / VENTANA): ")
            
            if lvl4 == "PUERTA" or lvl4 == "puerta" or lvl4 == "Puerta":
                print("Entras en silencio. Sobre una mesa hay una radio vieja y un mapa.")
                
                lvl5 = input("¿Qué objeto revisas primero? (RADIO / MAPA): ")
                
                if lvl5 == "RADIO" or lvl5 == "radio" or lvl5 == "Radio":
                    print("Enciendes la radio y escuchas a un guardabosques pidiendo tu ubicación.")
                    
                    lvl6 = input("¿Le dices que estás en la CABAÑA o sales al SENDERO a buscarlo?: ")
                    
                    if lvl6 == "CABAÑA" or lvl6 == "CABANA" or lvl6 == "cabaña" or lvl6 == "cabana" or lvl6 == "Cabaña" or lvl6 == "Cabana":
                        print("¡FINAL FELIZ! Esperas seguro dentro y el guardabosques llega a rescatarte al amanecer.")
                    elif lvl6 == "SENDERO" or lvl6 == "sendero" or lvl6 == "Sendero":
                        print("¡FINAL INESPERADO! Al salir al sendero te vuelves a cruzar con el oso en la oscuridad. Fin del juego.")
                    else:
                        print("Opción no válida. Perdiste la señal de radio. Fin del juego.")
                        
                elif lvl5 == "MAPA" or lvl5 == "mapa" or lvl5 == "Mapa":
                    print("Mientras lees el mapa a oscuras, pisas una tabla floja y caes al sótano. Fin del juego.")
                else:
                    print("Opción no válida. Hiciste ruido y algo te atrapó. Fin del juego.")
                    
            elif lvl4 == "VENTANA" or lvl4 == "ventana" or lvl4 == "Ventana":
                print("Te cortas con los vidrios rotos y el ruido atrae a los lobos del bosque. Fin del juego.")
            else:
                print("Opción no válida. Fin del juego.")
                
        elif lvl3 == "RÍO" or lvl3 == "RIO" or lvl3 == "río" or lvl3 == "rio" or lvl3 == "Río" or lvl3 == "Rio":
            print("Intentas cruzar el río en la oscuridad, pero la corriente es muy fuerte. Fin del juego.")
        else:
            print("Opción no válida. Te perdiste entre la maleza. Fin del juego.")
            
    elif lvl2 == "CORRER" or lvl2 == "correr" or lvl2 == "Correr":
        print("El oso es mucho más rápido que tú y te alcanza en segundos. Fin del juego.")
    else:
        print("Opción no válida. Te quedaste paralizado y el oso te vio. Fin del juego.")

elif lvl1 == "LINTERNA" or lvl1 == "linterna" or lvl1 == "Linterna":
    print("Enciendes la linterna y ves un camino iluminado. De pronto, oyes algo entre los árboles.")
    
    lvl2_b = input("¿Qué decides hacer? (SEGUIR / APAGAR): ")
    
    if lvl2_b == "SEGUIR" or lvl2_b == "seguir" or lvl2_b == "Seguir":
        print("Sigues el camino iluminado sin detenerte y encuentras un puente colgante sobre un barranco.")
        
        lvl3_b = input("¿Qué haces? (CRUZAR / RODEAR): ")
        
        if lvl3_b == "CRUZAR" or lvl3_b == "cruzar" or lvl3_b == "Cruzar":
            print("Cruzas con cuidado el puente. Al otro lado ves una torre de vigilancia y una cueva.")
            
            lvl4_b = input("¿A dónde te diriges? (TORRE / CUEVA): ")
            
            if lvl4_b == "TORRE" or lvl4_b == "torre" or lvl4_b == "Torre":
                print("Subes las escaleras de la torre de vigilancia. Encuentras un panel eléctrico y una bengala.")
                
                lvl5_b = input("¿Qué usas para pedir ayuda? (PANEL / BENGALA): ")
                
                if lvl5_b == "BENGALA" or lvl5_b == "bengala" or lvl5_b == "Bengala":
                    print("Lanzas la bengala al cielo nocturno. Un helicóptero de rescate ve la luz roja y se acerca.")
                    
                    lvl6_b = input("¿Te quedas en el TECHO de la torre o bajas al CLARO del bosque para que aterrice?: ")
                    
                    if lvl6_b == "CLARO" or lvl6_b == "claro" or lvl6_b == "Claro":
                        print("¡FINAL HEROICO! El helicóptero aterriza en el claro y logras salir del bosque a salvo.")
                    elif lvl6_b == "TECHO" or lvl6_b == "techo" or lvl6_b == "Techo":
                        print("¡FINAL ACCIDENTADO! El viento de las hélices hace colapsar el techo viejo de la torre. Fin del juego.")
                    else:
                        print("Opción no válida. El helicóptero no te vio y se marchó. Fin del juego.")
                        
                elif lvl5_b == "PANEL" or lvl5_b == "panel" or lvl5_b == "Panel":
                    print("El panel eléctrico hace cortocircuito y te da una descarga. Fin del juego.")
                else:
                    print("Opción no válida. Fin del juego.")
                    
            elif lvl4_b == "CUEVA" or lvl4_b == "cueva" or lvl4_b == "Cueva":
                print("¡La cueva era la guarida del oso grizzly! Fin del juego.")
            else:
                print("Opción no válida. Fin del juego.")
                
        elif lvl3_b == "RODEAR" or lvl3_b == "rodear" or lvl3_b == "Rodear":
            print("Al intentar rodear el barranco en la oscuridad, resbalas por el borde. Fin del juego.")
        else:
            print("Opción no válida. Fin del juego.")
            
    elif lvl2_b == "APAGAR" or lvl2_b == "apagar" or lvl2_b == "Apagar":
        print("Apagas la linterna, tropiezas con una raíz y te golpeas la cabeza. Fin del juego.")
    else:
        print("Opción no válida. Fin del juego.")

else:
    print("Opción no válida. Intenta de nuevo escribiendo FÓSFORO o LINTERNA.")
