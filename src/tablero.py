class Tablero:
    def __init__(self):
       self.__tablero = [[' ' for _ in range(3)] for _ in range(3)]

       def poner_ficha(self, fila, columna, ficha):
           if self.__tablero[fila][columna] == ' ':
               self.__tablero[fila][columna] = ficha
           else:
               raise ValueError("Casillero ya ocupado")