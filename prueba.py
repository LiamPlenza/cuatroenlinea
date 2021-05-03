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
def mostrarTablero(tablero, secuencia):
    todoOk = columnaCorrecta(secuencia)
    if todoOk:
        for row in tablero:
            print(row)
    else:
        print("La secuencia se sale del tablero proporcionado")

def contenidoColumna(numeroColumna, tablero):
    columna = []
    for row in tablero:
        celda = row[numeroColumna - 1]
        columna.append(celda)
    return columna


secuencia = [1, 2, 3, 4, 1, 2, 3, 4]
tablero = tableroVacio()
tirarFichas(tablero, secuencia)
mostrarTablero(tablero, secuencia)
print(contenidoColumna(2, tablero))