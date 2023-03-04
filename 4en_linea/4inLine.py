import numpy as np

NumeroFilas = 6
NumeroColumnas = 7

def crear_tablero():
    Tablero = np.zeros((NumeroFilas, NumeroColumnas))
    return Tablero

def ficha(Tablero, fila, col, ficha):
    Tablero[fila][col] = ficha

def lugar_valido(Tablero, col):
    return Tablero[NumeroFilas-1][col] == 0

def siguiente_fila(Tablero, col):
    for r in range(NumeroFilas):
        if Tablero[r][col] == 0:
            return r

def print_board(Tablero):
    print(np.flip(Tablero, 0))

def movimiento_ganador(Tablero, ficha):
    # Verificar las fichas horizontales para ganar
    for c in range(NumeroColumnas-3):
        for r in range(NumeroFilas):
            if Tablero[r][c] == ficha and Tablero[r][c+1] == ficha and Tablero[r][c+2] == ficha and Tablero[r][c+3] == ficha:
                return True

    # Verificar las fichas verticales para ganar
    for c in range(NumeroColumnas):
        for r in range(NumeroFilas-3):
            if Tablero[r][c] == ficha and Tablero[r+1][c] == ficha and Tablero[r+2][c] == ficha and Tablero[r+3][c] == ficha:
                return True

    # Comprobar diagonales con pendiente positiva
    for c in range(NumeroColumnas-3):
        for r in range(NumeroFilas-3):
            if Tablero[r][c] == ficha and Tablero[r+1][c+1] == ficha and Tablero[r+2][c+2] == ficha and Tablero[r+3][c+3] == ficha:
                return True

    # Comprobar diagonales con pendiente negativa
    for c in range(NumeroColumnas-3):
        for r in range(3, NumeroFilas):
            if Tablero[r][c] == ficha and Tablero[r-1][c+1] == ficha and Tablero[r-2][c+2] == ficha and Tablero[r-3][c+3] == ficha:
                return True

def main():
    Tablero = crear_tablero()
    fin_juego = False
    turn = 0
    jugador_1 = str(input("digite su nombre"))
    jugador_2 = str(input("digite el nombre del siguiente jugador"))
    while not fin_juego:
        # preguntar por datos del primer jugador
        if turn == 0:
            col = int(input(f"{jugador_1} escoge la posicion que desees jugar del (0-6):"))
            if lugar_valido(Tablero, col):
                fila = siguiente_fila(Tablero, col)
                ficha(Tablero, fila, col, 1)

                if movimiento_ganador(Tablero, 1):
                    print(f"felicidades {jugador_1} ganaste!")
                    fin_juego = True

        # preguntar por datos del segundo jugador
        else:
            col = int(input(f"{jugador_2} escoge la posicion que desees jugar del (0-6):"))
            if lugar_valido(Tablero, col):
                fila = siguiente_fila(Tablero, col)
                ficha(Tablero, fila, col, 2)

                if movimiento_ganador(Tablero, 2):
                    print(f"felicidades {jugador_2} ganaste!")
                    fin_juego = True


        print_board(Tablero)
        turn += 1
        turn = turn % 2

    print("Fin del Juego")

if __name__ == '__main__':
    main()