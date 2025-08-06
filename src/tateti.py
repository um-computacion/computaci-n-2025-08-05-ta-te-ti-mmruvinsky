

class Tateti:
    def __init__(self):
        self.turno = 'X'
        self.tablero =

    def ocupar_un_casillero(self, fil, col):
        self.tablero.poner_ficha(fil, col, self.turno)
        if self.turno == 'X':
            self.turno = 'O' Tablero()
        else:
            self.turno = 'X'
