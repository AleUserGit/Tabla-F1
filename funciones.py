def ingresar_n():
    n = input("Ingrese la cantidad de equipos en competencia: ").strip()
    while not n.isdigit() or int(n) == 0:
        print("--")
        print("Error: se necesita un entero positivo")
        n = input("Ingrese la cantidad de equipos en competencia: ").strip()
    n = int(n)
    return n

def tipo_jugador():
    jugador = input("Ingrese el tipo de jugador: ").capitalize().strip()
    while jugador == "":
        print("--")
        print("Error: no puede estar vacío")
        jugador = input("Ingrese el tipo de jugador: ").capitalize().strip()
    return jugador

def tipo_equipo():
    equipo = input("Ingrese el tipo de equipo: ").capitalize().strip()
    while equipo == "":
        print("--")
        print("Error: no puede estar vacío")
        equipo = input("Ingrese el tipo de equipo: ").capitalize().strip()
    return equipo

def ingresar_jugador(categoria_jugador):
    categoria_jugador = categoria_jugador.lower()
    nombre = input(f"Ingrese el nombre del {categoria_jugador}: ").capitalize().strip()
    while nombre == "":
        print("--")
        print("Error: el nombre no puede estar vacío")
        nombre = input(f"Ingrese el nombre del {categoria_jugador}: ").capitalize().strip()
    return nombre

def ingresar_equipo(categoria_equipo, categoria_jugador):
    categoria_jugador, categoria_equipo = categoria_jugador.lower(), categoria_equipo.lower()
    equipo = input(f"Ingrese el {categoria_equipo} del {categoria_jugador}: ").capitalize().strip()
    while equipo == "":
            print("--")
            print("Error: el nombre no puede estar vacío")
            equipo = input(f"Ingrese el {categoria_equipo} del {categoria_jugador}: ").capitalize().strip()
    return equipo

def ingresar_puntos(categoria_jugador):
    categoria_jugador = categoria_jugador.lower()
    puntos = input(f"Ingrese los puntos del {categoria_jugador}: ").strip()
    while not puntos.isdigit():
        print("--")
        print("Error: se necesita un entero positivo")
        puntos = input(f"Ingrese los puntos del {categoria_jugador}: ").strip()
    puntos = int(puntos)
    return puntos

def armar_tabla(n, categoria_jugador, categoria_equipo):
    tabla = []
    for i in range(n*2):
        fila = []
        jugador = ingresar_jugador(categoria_jugador)
        print("")
        equipo = ingresar_equipo(categoria_equipo, categoria_jugador)
        print("")
        fila.append(jugador)
        fila.append(0)
        fila.append(equipo)
        tabla.append(fila)
    return tabla

def tabla_equipos(tabla_jugador):
    tabla = []
    for jugador in tabla_jugador:
        puntos = jugador[1]
        equipo = jugador[2]
        existe  = False

        for f in tabla:
            if f[0] == equipo:
                f[1] += puntos
                existe = True

        if not existe:
            tabla.append([equipo, puntos])
    return tabla

            
def formato_jugadores(tabla, categoria_jugador, categoria_equipo):
    puesto = 1
    print("")
    print(f"{'Puesto':<10}"
          f"{f'{categoria_jugador}':<15}"
          f"{'Puntos':<15}"
          f"{f'{categoria_equipo}':<15}")
    
    print("")
    for i in range(len(tabla)):
        print(f"{puesto:<10}"
            f"{tabla[i][0]:<15}"
            f"{tabla[i][1]:<15}"
            f"{tabla[i][2]:<15}")
        puesto += 1
    print("") 

def formato_equipo(tabla, categoria_equipo):
    puesto = 1
    print("")
    print(f"{'Puesto':<10}"
          f"{f'{categoria_equipo}':<15}"
          f"{'Puntos':<15}")
    
    print("")
    for i in range(len(tabla)):
        print(f"{puesto:<10}"
            f"{tabla[i][0]:<20}"
            f"{tabla[i][1]:<15}")
        puesto += 1
    print("") 

def ordenar_tabla(tabla):
    for i in range(len(tabla)):
        for j in range(len(tabla) -1 - i):
            punto_actual = tabla[j][1]
            punto_sigue = tabla[j+1][1]

            if punto_actual < punto_sigue:
                tabla[j], tabla[j+1] = tabla[j+1], tabla[j]
        
    return tabla

def agregar_puntos():
    nueva = input("Hay más puntos que agregar? (si/no) ").lower().strip()
    while nueva != "si" and nueva != "no":
        print("Error: responda con si o no")
        nueva = input("Hay más puntos que agregar? (si/no) ").lower().strip()
    if nueva == "si":
        return True
    else:
        return False

def si_suma(nombre):
    suma = input(f"{nombre} sumó puntos? (si/no) ").lower().strip()
    while suma != "si" and suma != "no":
        print("Error: responda con si o no")
        suma = input(f"{nombre} sumó puntos? (si/no) ").lower().strip()
    if suma == "si":
        return True
    else:
        return False
    

def sumar_puntos(tabla_jugador, categoria_jugador):
    for i in range(len(tabla_jugador)):
        print(tabla_jugador[i])
        if si_suma(tabla_jugador[i][0]):
            puntos = ingresar_puntos(categoria_jugador)
            tabla_jugador[i][1] += puntos
    return tabla_jugador

def menu():
    print("1 - Nuevo Campeonato")
    print("2 - Cargar Campeonato")
    print("3 - Eliminar Campeonato")
    print("4 - Salir")

def elegir_opcion():
    menu()
    print("")
    opcion = input("")
    while not opcion.isdigit() or not (0 < int(opcion) < 5):
        print("--")
        print("Error: la opción seleccionada no es válida")
        opcion = input("")
    opcion = int(opcion)
    return opcion

def validar_si_no(validar):
    if validar != "si" and validar != "no":
        return False
    return True

def validar_decision():
    print("¿Desea guardar los cambios?")
    cambios = input("(si / no): ").lower().strip()
    valido = validar_si_no(cambios)
    while not valido:
        print("--")
        print("Error: responda con sí o no")
        print("¿Desea guardar los cambios?")
        cambios = input("(si / no): ").lower().strip()
        valido = validar_si_no(cambios)

    if cambios == "si":
        return True
    else:
        return False