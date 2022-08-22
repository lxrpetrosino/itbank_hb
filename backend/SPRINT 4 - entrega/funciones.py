import sys
import csv
from datetime import datetime

'''índices de columnas del archivo para su búsqueda'''
INDICE_NroCheque = 0
INDICE_CodigoBanco = 1
INDICE_CodigoScurusal = 2
INDICE_NumeroCuentaOrigen = 3
INDICE_NumeroCuentaDestino = 4
INDICE_Valor = 5
INDICE_FechaOrigen = 6
INDICE_FechaPago = 7
INDICE_DNI = 8
INDICE_Tipo = 9
INDICE_Estado = 10


def obtendatos(nombreArchivo):
    with open(nombreArchivo) as archivo:
        lector = csv.reader(archivo)
        datos = list(lector)

    cabecera = datos[0]

    return datos, cabecera 
''' La función devuelve una lista de listas a partir del archivo, 
"cabera" es una lista aparte con la primer fila de datos. '''

def fecha2timestamp(value:str) -> int:
    dt=datetime.strptime(value,'%d-%m-%Y')
    return int(dt.timestamp())
''' Convierte la fecha de formato str en timestamp '''

def duplicadoError(listaCheques, dni):
    errorNroCheque=False
    for i in range(1,len(listaCheques)):
        for j in range(i+1,len(listaCheques)):
            if listaCheques[i][0]==listaCheques[j][0]:
                if listaCheques[i][3]==listaCheques[j][3]:
                    if dni == listaCheques[i][8]:
                        print('\n*** ERROR: Nro Cheque:',listaCheques[i][0],' de cuenta origen ',listaCheques[i][3],' se encuentra repetido. Datos no válidos***')
                        errorNroCheque=True
    return errorNroCheque

''' Retorna un error de ser que se encuntre un cheque con número repetido y cuenta de origen con número repetido '''


def consulta(datos, DNI, tipoCheques, estadoCheques, strFechaInicio, strFechaFin):

    fechaInicio = str(fecha2timestamp(strFechaInicio))
    fechaFin = str(fecha2timestamp(strFechaFin))

    if tipoCheques == 'DEPOSITADO':
        INDICE_fecha = INDICE_FechaPago
    else:
        INDICE_fecha = INDICE_FechaOrigen
    #selecciona la columna de fechas que va a ser usada en la consulta

    cheques_dni=[]
    for i in datos:
        if (i[INDICE_fecha]>=fechaInicio) and (i[INDICE_fecha]<=fechaFin):
            if i[INDICE_DNI]==DNI: 
                if (tipoCheques==i[INDICE_Tipo]):
                    if (estadoCheques==i[INDICE_Estado]) or (estadoCheques=='TODOS'):
                        cheques_dni.append(i)
    return cheques_dni


def pedidoUsuario():
    print("   * Valor por defecto: 'file.csv' *")
    print("->")
    nombreArchivo = str(input("Ingrese el nombre del archivo: "))
    if nombreArchivo == '':
        nombreArchivo = 'file.csv'
    
    dniNoValido = True
    print("\n->")
    while dniNoValido:
        dni = str(input("Ingrese el DNI a consultar: "))
        if dni.isnumeric() and (len(dni) == 7 or len(dni) == 8):
            dniNoValido = False
        else:
            dniNoValido = True
            print('*** Por favor, ingrese de nuevo. \nEl DNI debe tener entre 7 y 8 dígitos ***')


    tipoChequeNoValido = True
    print("\n->")
    while tipoChequeNoValido:
        opcion = str(input("Tipos de cheque: \n 1. Emitido\n 2. Depositado\n Ingrese el Tipo de cheque a consultar: "))
        if opcion == '1':
            tipoCheque = "EMITIDO"
            tipoChequeNoValido = False
            print(tipoCheque)
        elif opcion == '2':
            tipoCheque = "DEPOSITADO"
            tipoChequeNoValido = False
            print(tipoCheque)
        else:
            tipoChequeNoValido = True
            print('\n*** Elija una opción válida: ***\n')


    print("\n->")
    opcion = input("Estado de cheques: \n 1. PENDIENTE\n 2. APROBADO\n 3. RECHAZADO\n* Presionando ENTER selecciona todos por defecto * \n Ingrese el Estado a consultar: ")
    if opcion == '1':
        estadoCheque = "PENDIENTE"
    elif opcion == '2':
        estadoCheque = "APROBADO"
    elif opcion == '3':
        estadoCheque = "RECHAZADO"
    else:
        estadoCheque = "TODOS"


    strFechaInicio = str('1-1-2017') # fecha de Inicio por defecto
    strFechaFin = str('1-8-2022') # fecha de Finalización por defecto

    print("\n->")
    solicitaRango = True if str(input("¿Desea seleccionar un rango de fecha? S/N ")).upper() == "S" else False
    

    if solicitaRango:
        print("\n->")
        test_str = str(input("Seleccione fecha de Inicio(dd-mm-aaaa): "))
        try:
            res = bool(datetime.strptime(test_str, '%d-%m-%Y'))
        except ValueError:
            res = False
        if res:
            strFechaInicio = test_str
        else:
            strFechaInicio = str('1-1-2017') # fecha de Inicio por defecto
            print(strFechaInicio)

        print("\n->")
        test_str = str(input("Seleccione fecha de Finalización(dd-mm-aaaa): "))
        try:
            res = bool(datetime.strptime(test_str, '%d-%m-%Y'))
        except ValueError:
            res = False
        if res:
            strFechaFin = test_str
        else:
            strFechaFin = str('1-8-2022') # fecha de Finalización por defecto
            print(strFechaFin)

    print("\n->")
    salida = str(input("¿Desea impresión por PANTALLA (por defecto) o en un ARCHIVO CSV?\n 1. PANTALLA\n 2. ARCHIVO CSV \nIngrese una opción: "))
    # Variable a evaluar sobre preferencia del Usuario

    return nombreArchivo, dni, tipoCheque, estadoCheque, strFechaInicio, strFechaFin, salida
''' Función para obtener datos del usuario '''

def salidaPantalla(lista_cheques, cabecera):
    formato = "{:<10} {:<12} {:<15} {:<19} {:<20} {:<6} {:<12} {:<10} {:<10} {:<11} {:<10}"
    print(formato.format(cabecera[0], cabecera[1], cabecera[2], cabecera[3], cabecera[4], cabecera[5], cabecera[6], cabecera[7], cabecera[8], cabecera[9], cabecera[10]))
    for lista in lista_cheques:
        print(formato.format(lista[0], lista[1], lista[2], lista[3], lista[4], lista[5], lista[6], lista[7], lista[8], lista[9], lista[10]))

    print("\n")

def salidaCsv(lista_cheques, cabecera):
    nombre = nombreCsv(lista_cheques)
    with open(nombre, 'w', newline='') as archivoCsv:
        writer=csv.writer(archivoCsv)
        writer.writerow(cabecera[3:8])
        for line in lista_cheques:
            seleccion = line[3:8]
            writer.writerow(seleccion)


def nombreCsv(lista_cheques):
    dni = str(lista_cheques[0][8]) 
    fecha = str(int(datetime.now().timestamp()))
    return dni + '_' + fecha + '.csv'
