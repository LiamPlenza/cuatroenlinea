def tableroVacio ():
        return[
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]
def tirarFichas (tablero, secuencia):
    todoOk = columnaCorrecta(secuencia)
    if todoOk:
        for row in range(5, 0, -1):
            for c in range(len(secuencia)):
                if c % 2 == 0:
                    if tablero[row][secuencia[c] - 1] == 0:
                        tablero[row][secuencia[c] - 1] = 1
                else:
                    if tablero[row][secuencia[c] - 1] == 0:
                     tablero[row][secuencia[c] - 1] = 2
    return
def columnaCorrecta(secuencia):
    a = 0
    b = 0
    for c in range(len(secuencia)):
        if 8 > secuencia[c] > 0:
            a += 1
        else:
            b += 1
    if len(secuencia) == (a - b):
        return True
    else:
        return False
def mostrarTablero(tablero):
    for row in range(0,6):
	    print(" | "  , end='')
	    for cell in range(0,7):
		    if tablero[row][cell] == 0:
			    print('   ',end='')
		    else:
			    print(f' {tablero[row][cell]} ',end='')
	    print(' | ')
    print(" +- - - - - - - - - - - -+")

def contenidoFila(fila, tablero):
    mostrarCF = []
    cf = 6 - int(fila)
    for a in range(0, 7, +1):
        celda = tablero[cf][a]
        mostrarCF.append(celda)
    return mostrarCF

def filaValida (fila):
    if 0 > fila > 7:
        return True
    else:
        return False
def contenidoCol(columna, tablero):
    mostrarCC = []
    for a in range(5, -1, -1):
        celda = tablero[a][int(columna) - 1]
        mostrarCC.append(celda)
    return mostrarCC
def columnaValida (columna):
    if 0 > columna > 8:
        return True
    else:
        return False

secuencia = [1, 2, 3, 4, 1, 2, 3, 4]
tablero = tableroVacio()
tirarFichas(tablero, secuencia)

if columnaCorrecta:
    mostrarTablero(tablero) #tablero agregado
else:
    print("Una de las fichas tiradas no fue arrojada en una columna valida (1 a 7)")

fila = 6

if filaValida:
    mostrarCF = contenidoFila(fila, tablero)
    print(mostrarCF)
else:
    print ("La fila indicada no corresponde a una perteneciente al talero")

columna = 5

if columnaValida:
    mostrarCC = contenidoFila(fila, tablero)
    print(mostrarCC)
else:
    print ("La columna indicada no corresponde a una perteneciente al talero")
