class Tablero:
    def __init__(self):
       self.casilleros = [[' ' for _ in range(3)] for _ in range(3)]

       def poner_ficha(self, fila, columna, ficha):
           if self.__tablero[fila][columna] == ' ':
               self.__tablero[fila][columna] = ficha
           else:
               raise ValueError("Casillero ya ocupado")
           
       def obtener_casillero(self, fil, col):
           return self.casilleros[fil][col]