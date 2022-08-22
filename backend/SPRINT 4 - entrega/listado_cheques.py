import os
from turtle import clear
from funciones import *

os.system('cls')
'''Función pedidoUsuario pregunta los datos al usuario'''
nombreArchivo, dni, tipoCheque, estadoCheque, strFechaInicio, strFechaFin, salida = pedidoUsuario()  

'''Función que entrega una lista a partir de leer el archivo csv'''
datos, cabecera = obtendatos(nombreArchivo) 

'''Selecciona cheques correspondientes a la consulta'''
cheques_dni = consulta(datos, dni, tipoCheque ,estadoCheque, strFechaInicio, strFechaFin)
if not(duplicadoError(datos, dni)):
    if salida == '2':
        salidaCsv(cheques_dni, cabecera)
    else:
        salidaPantalla(cheques_dni, cabecera)


    




