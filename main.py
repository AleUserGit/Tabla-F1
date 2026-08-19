from funciones import ingresar_n, tipo_jugador, tipo_equipo, armar_tabla, tabla_equipos, ordenar_tabla, formato_jugadores, formato_equipo
from funciones import agregar_puntos, sumar_puntos

#Ingresa datos básicos del programa -> Cantidad de equipos, categoría de jugadores y equipos
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
