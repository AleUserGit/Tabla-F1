def ingresar_n():
    n = input("Ingrese la cantidad de equipos en competencia: ").strip()
    while not n.isdigit() or int(n) == 0:
        print("--")
        print("Error: se necesita un entero positivo")
        n = input("Ingrese la cantidad de equipos en competencia: ").strip()
    n = int(n)
    return n

def ingresar_piloto():
    piloto = input("Ingrese el apellido del piloto: ").capitalize().strip()
    while piloto == "":
        print("--")
        print("Error: el apellido no puede estar vacío")
        piloto = input("Ingrese el apellido del piloto: ").capitalize().strip()
    return piloto

def ingresar_equipo():
    equipo = input("Ingrese la escudería del piloto: ").strip()
    while equipo == "":
            print("--")
            print("Error: la escudería no puede estar vacía")
            equipo = input("Ingrese la escudería del piloto: ").strip()
    return equipo

def ingresar_puntos():
    puntos = input("Ingrese los puntos del piloto: ").strip()
    while not puntos.isdigit():
        print("--")
        print("Error: se necesita un entero positivo")
        puntos = input("Ingrese los puntos del piloto: ").strip()
    puntos = int(puntos)
    return puntos

def armar_tabla(n):
    tabla = []
    for i in range(n*2):
        fila = []
        piloto = ingresar_piloto()
        print("")
        equipo = ingresar_equipo()
        print("")
        fila.append(piloto)
        fila.append(0)
        fila.append(equipo)
        tabla.append(fila)
    return tabla

def armar_constructores( wdc):
    tabla = []
    for piloto in wdc:
        puntos = piloto[1]
        equipo = piloto[2]
        existe  = False

        for f in tabla:
            if f[0] == equipo:
                f[1] += puntos
                existe = True

        if not existe:
            tabla.append([equipo, puntos])
    return tabla

            
def formato_pilotos(tabla):
    puesto = 1
    print("")
    print(f"{'Puesto':<10}"
          f"{'Piloto':<15}"
          f"{'Puntos':<15}"
          f"{'Escuderia':<15}")
    
    print("")
    for i in range(len(tabla)):
        print(f"{puesto:<10}"
            f"{tabla[i][0]:<15}"
            f"{tabla[i][1]:<15}"
            f"{tabla[i][2]:<15}")
        puesto += 1
    print("") 

def formato_constructores(tabla):
    puesto = 1
    print("")
    print(f"{'Puesto':<10}"
          f"{'Constructor':<15}"
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

def nueva_carrera():
    nueva = input("Hay más puntos que agregar? (si/no) ").lower().strip()
    while nueva != "si" and nueva != "no":
        print("Error: responda con si o no")
        nueva = input("Hay más puntos que agregar? (si/no) ").lower().strip()
    if nueva == "si":
        return True
    else:
        return False

def si_suma():
    suma = input("El piloto sumó puntos? (si/no) ").lower().strip()
    while suma != "si" and suma != "no":
        print("Error: responda con si o no")
        suma = input("El piloto sumó puntos? (si/no) ").lower().strip()
    if suma == "si":
        return True
    else:
        return False
    

def sumar_puntos(wdc):
    for i in range(len(wdc)):
        print(wdc[i])
        if si_suma():
            puntos = ingresar_puntos()
            wdc[i][1] += puntos
    return wdc