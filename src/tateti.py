from tablero import Tablero
from excepciones import PosicionInvalida, CasilleroOcupado

class Tateti:
    def __init__(self):
        self.turno = 'X'
        self.tablero = Tablero()

    def ocupar_un_casillero(self, fil, col):
        # Ponemos la ficha en el tablero
        self.tablero.poner_ficha(fil, col, self.turno)
        # Cambiamos el turno
        if self.turno == "X":
            self.turno = "O" 
        else:
            self.turno = "X"

    def hay_ganador(self):
        t = self.tablero.casilleros 
        # Filas y columnas
        for i in range(3):
            if t[i][0] == t[i][1] == t[i][2] != ' ':
                return t[i][0]
            if t[0][i] == t[1][i] == t[2][i] != ' ':
                return t[0][i]
        # Diagonales
        if t[0][0] == t[1][1] == t[2][2] != ' ':
            return t[0][0]
        if t[0][2] == t[1][1] == t[2][0] != ' ':
            return t[0][2]
        return None
    
    def tablero_lleno(self):
        """Verifica si el tablero está lleno (empate)"""
        for fila in self.tablero.casilleros:
            for casillero in fila:
                if casillero == ' ':
                    return False
        return True