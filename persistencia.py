import os, json

def archivo_existe(archivo):
    existe = False
    if os.path.exists(archivo):
        existe = True
    return existe

def guardar_archivo(nombre, cantidad, tipo_jugador, tipo_equipo, tabla_jugadores, tabla_equipos):
    with open(f"{nombre}.json", "w") as archivo:
        json.dump() 