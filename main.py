from funciones import ingresar_n, tipo_jugador, tipo_equipo, armar_tabla, tabla_equipos, ordenar_tabla, formato_jugadores, formato_equipo
from funciones import agregar_puntos, sumar_puntos, elegir_opcion, validar_decision
from persistencia import archivo_existe, guardar_datos, guardar_archivo, mostrar_archivos, cargar_archivo, eliminar_archivo

print("Iniciando Programa")
print("--")
print("Bienvenido al medidor de puntajes")
print("Seleccione una opción: ")
print("")

opcion = elegir_opcion()

if opcion == 1:
    print("")
    nombre = input("Ingrese el nombre del nuevo campeonato: ").strip()
    existe = archivo_existe(nombre)
    while existe:
        print("--")
        print(f"Error: ya existe un campeonato con el nombre {nombre}")
        nombre = input("Ingrese el nombre del nuevo campeonato: ").strip()
        existe = archivo_existe(nombre)

    cant = ingresar_n()
    tipo_j = tipo_jugador()
    tipo_e = tipo_equipo()
    config = {
        "categoria_jugador": tipo_j,
        "categoria_equipo": tipo_e,
        "cantidad_equipos": cant
        }

    tabla_ind = armar_tabla(cant, tipo_j, tipo_e)

    sigue = agregar_puntos()
    while sigue:
        sumar_puntos(tabla_ind, tipo_j)
        sigue = agregar_puntos()

    ordenar_tabla(tabla_ind)
    tabla_gru = tabla_equipos(tabla_ind)

    datos = guardar_datos(config, tabla_ind, tabla_gru)

    print("")
    formato_jugadores(tabla_ind, tipo_j, tipo_e)
    formato_equipo(tabla_gru, tipo_e)

    guardar_archivo(nombre, datos)
    
elif opcion == 2:
    print("")
    archivos = mostrar_archivos()
    print("Campeonatos Guardados:")
    for i in archivos:
        print("")
        print(i)
    
    nombre = input("Ingrese el nombre del campeonato que desea reanudar: ").strip()
    existe = archivo_existe(nombre)
    while not existe:
        print("--")
        print(f"Error: no existe ningún campeonato con el nombre {nombre}")
        print("")
        for i in archivos:
            print(i)
        print("")
        nombre = input("Ingrese el nombre del campeonato que desea reanudar: ").strip()
        existe = archivo_existe(nombre)

    datos = cargar_archivo(nombre)
    tipo_j = datos["configuracion"]["categoria_jugador"]
    tipo_e = datos["configuracion"]["categoria_equipo"]
    cant = datos["configuracion"]["cantidad_equipos"]
    tabla_ind = datos["tabla_jugadores"]
    tabla_gru = datos["tabla_equipos"]

    print("")
    formato_jugadores(tabla_ind, tipo_j, tipo_e)
    formato_equipo(tabla_gru, tipo_e)

    sigue = agregar_puntos()
    while sigue:
        sumar_puntos(tabla_ind, tipo_j)
        sigue = agregar_puntos()

    cambios = validar_decision()
    if cambios:
        ordenar_tabla(tabla_ind)
        tabla_gru = tabla_equipos(tabla_ind)
        config = {
            "categoria_jugador": tipo_j,
            "categoria_equipo": tipo_e,
            "cantidad_equipos": cant
            }
        datos = guardar_datos(config, tabla_ind, tabla_gru)

        guardar_archivo(nombre, datos)
        print("")
        formato_jugadores(tabla_ind, tipo_j, tipo_e)
        formato_equipo(tabla_gru, tipo_e)

elif opcion == 3:
    print("")
    archivos = mostrar_archivos()
    print("Campeonatos Guardados:")
    for i in archivos:
        print("")
        print(i)

    print("")
    nombre = input("Ingrese el nombre del campeonato que desea eliminar: ").strip()
    existe = archivo_existe(nombre)
    while not existe:
        print("--")
        print(f"Error: no existe ningún campeonato con el nombre {nombre}")
        nombre = input("Ingrese el nombre del campeonato que desea eliminar: ").strip()
        existe = archivo_existe(nombre)

    cambios = validar_decision()
    if cambios:
        eliminar_archivo(nombre)
        archivos = mostrar_archivos()
        print("Campeonatos Guardados:")
        for i in archivos:
            print("")
            print(i)
    else:
        print("Eliminación Cancelada")

else:
    print("")
    print("No se realizaron acciones")

print("")
print("PROGRAMA FINALIZADO")