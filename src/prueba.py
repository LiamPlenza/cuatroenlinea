  
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
def tiroValido(secuencia):
	for column in secuencia:
		if column < 1 or column > 7:
			return False
	return True
def mostrarTablero(tablero):
	for row in range(0,6):
		print(' | ', end='')
		for cell in range(0,7):
			if tablero[row][cell] == 0:
				print('   ',end='')
			else:
				print(f' {tablero[row][cell]} ',end='')
		print(' | ', end='')
		print()
	print(" +- - - - - - - - - - - -+",end="")


def contenidoFila(fila, tablero):
    mostrarCF = []
    cf = 6 - int(fila)
    for a in range(0, 7, +1):
        celda = tablero[cf][a]
        mostrarCF.append(celda)
    return mostrarCF
def contenidoCol(columna, tablero):
    mostrarCC = []
    for a in range(5, -1, -1):
        celda = tablero[a][int(columna) - 1]
        mostrarCC.append(celda)
    return mostrarCC
def contenidoTodasLasFilas(tablero):
	rows_all = []
	for row in tablero:
		rows_all.append(row)
	return rows_all

def contenidoTodasLasColumnas(tablero):
	columns_all = []
	for nro_column in range(1, 8):
		columns_all.append(contenidoCol(nro_column,tablero))
	return columns_all

tablero = tableroVacio()
#secuencia_texto = input("Ingrese la secuencia de numeros")
secuencia = [1,1]
#for items in secuencia_texto.split(','):
 #   secuencia.append(int(items))
if tiroValido(secuencia):
	tablero = completarTableroEnOrden(secuencia, tablero)
	mostrarTablero(tablero)
	print(contenidoCol(1, tablero))
	print(f'¨{contenidoFila(6, tablero)}')
	print(f'Contenido de todas las filas: \n{contenidoTodasLasFilas(tablero)}')
	print(f'Contenido de todas las columnas: \n{contenidoTodasLasColumnas(tablero)}')
else:
	print("Uno de los numeros ingresados en la secuencia no se encuentra dentro de los parametros requeridos")