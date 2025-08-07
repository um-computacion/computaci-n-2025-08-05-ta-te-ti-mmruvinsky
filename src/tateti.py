from tablero import Tablero

class Tateti:
    def __init__(self):
        self.turno = 'X'
        self.tablero = Tablero()

    def ocupar_un_casillero(self, fil, col):
        if self.turno == "X":
            self.turno = "0"
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
    
    from excepciones import PosicionInvalida, CasilleroOcupado


