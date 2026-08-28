import os, json

def archivo_existe(archivo):
    existe = False
    if os.path.exists(archivo + ".json"):
        existe = True
    return existe

def guardar_datos(configuracion, tabla_jugadores, tabla_equipos):
    datos_archivo = {
        "configuracion": configuracion,
        "tabla_jugadores": tabla_jugadores,
        "tabla_equipos": tabla_equipos
    }

    return datos_archivo

def guardar_archivo(nombre, datos):
    with open(nombre + ".json", "w") as archivo:
        json.dump(datos, archivo)

def cargar_archivo(nombre):
    with open(nombre + ".json", "r") as archivo:
        datos = json.load(archivo)

    return datos

def eliminar_archivo(nombre):
    os.remove(nombre + ".json")

def mostrar_archivos():
    archivos_json = []
    for i in os.listdir("."):
        if i.endswith(".json"):
            limpio, extension = os.path.splitext(i)
            archivos_json.append(limpio)

    return archivos_json