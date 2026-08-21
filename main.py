from funciones import ingresar_n, tipo_jugador, tipo_equipo, armar_tabla, tabla_equipos, ordenar_tabla, formato_jugadores, formato_equipo
from funciones import agregar_puntos, sumar_puntos, elegir_opcion, archivo_existe

print("Iniciando Programa")
print("--")
print("Bienvenido al medidor de puntajes")
print("Seleccione una opción: ")
print("")

opcion = elegir_opcion()

if opcion == 1:
    print("")
    nombre = input("Ingrese el nombre del nuevo campeonato: ").strip()
    existe = archivo_existe(nombre + ".json")
    while existe:
        print("--")
        print(f"Error: ya existe un campeonato con el nombre {nombre}")
        nombre = input("Ingrese el nombre del nuevo campeonato: ").strip()
        existe = archivo_existe(nombre + ".json")

    cant = ingresar_n()
    tipo_j = tipo_jugador()
    tipo_e = tipo_equipo()

    tabla_ind = armar_tabla(cant, tipo_j, tipo_e)

    sigue = agregar_puntos()
    while sigue:
        sumar_puntos(tabla_ind, tipo_j)
        sigue = agregar_puntos()

    ordenar_tabla(tabla_ind)
    tabla_gru = tabla_equipos(tabla_ind)

    formato_jugadores(tabla_ind, tipo_j, tipo_e)
    formato_equipo(tabla_gru, tipo_e)
    
elif opcion == 2:
    print("")
    #Acá deberíamos poder mostrar los nombres de los archivos disponibles
    nombre = input("Ingrese el nombre del campeonato que desea reanudar: ").strip()
    existe = archivo_existe(nombre + ".json")
    while not existe:
        print("--")
        print(f"Error: no existe ningún campeonato con el nombre {nombre}")
        nombre = input("Ingrese el nombre del campeonato que desea reanudar: ").strip()
        existe = archivo_existe(nombre + ".json")

elif opcion == 3:
    print("")
    #Acá deberíamos poder mostrar los nombres de los archivos disponibles
    nombre = input("Ingrese el nombre del campeonato que desea eliminar: ").strip()
    existe = archivo_existe(nombre + ".json")
    while not existe:
        print("--")
        print(f"Error: no existe ningún campeonato con el nombre {nombre}")
        nombre = input("Ingrese el nombre del campeonato que desea eliminar: ").strip()
        existe = archivo_existe(nombre + ".json")
