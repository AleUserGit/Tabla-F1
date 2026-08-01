import json
from funciones import ingresar_n, armar_tabla, ordenar_tabla, sumar_puntos, nueva_carrera, armar_constructores, formato_pilotos, formato_constructores

try:
    with open("datos.json", "r") as archivo:
        wdc = json.load(archivo)
except FileNotFoundError:
    cantidad = ingresar_n()
    wdc = armar_tabla(cantidad)

print("--")


sigue = nueva_carrera()
while sigue:
    wdc = sumar_puntos(wdc)
    print("")
    sigue = nueva_carrera()

ordenar_tabla(wdc)
formato_pilotos(wdc)

print("--")

wcc = armar_constructores(wdc)
ordenar_tabla(wcc)
formato_constructores(wcc)

with open("datos.json", "w") as archivo:
    json.dump(wdc, archivo)