  
def tableroVacio ():
        return[
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]
def tirarFichas (ficha, columna, tablero):
    for row in range(6, 0, -1):
	    if tablero[row - 1][columna - 1] == 0:
		    tablero[row -1][columna - 1] = ficha
	    return
def completarTableroEnOrden(secuencia, tablero):
	c = 0
	for column in secuencia:
		if c % 2 != 0:
			tirarFichas(2, column, tablero)
		else:
			tirarFichas(1, column, tablero)
		c += 1
	return tablero
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
def columnaValida (secuencia):
    for columna in secuencia:
	    if columna < 1 or columna > 7:
		    return False
    return True

#secuencia_texto = input("Ingrese la secuencia de numeros")
secuencia = []
#for items in secuencia_texto.split(','):
 #   secuencia.append(int(items))


tablero = tableroVacio()
if columnaValida(secuencia):
	tablero = completarTableroEnOrden(secuencia, tablero)
	mostrarTablero(tablero)
else:
	print("Para que la secuencia sea valida los valores tienen que estar comprendidos entre el 1 y el 7")
fila = 6

if filaValida:
    mostrarCF = contenidoFila(fila, tablero)
    print(mostrarCF)
else:
    print ("La fila indicada no corresponde a una perteneciente al talero")

columna = 5

def columna_Valida (secuencia):
    if 0 > columna > 8:
        return True
    else:
        print ("La columna ingresada debe encontrarse entre 1 y 7")

if columna_Valida:
    mostrarCC = contenidoFila(fila, tablero)
    print(mostrarCC)
else:
    print ("La columna indicada no corresponde a una perteneciente al talero")