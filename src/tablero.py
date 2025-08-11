from excepciones import PosicionInvalida, CasilleroOcupado
from validadores import es_posicion_valida, casillero_libre

class Tablero:
    """Representa el tablero del juego"""
    def __init__(self):
        self.casilleros = [[' ' for _ in range(3)] for _ in range(3)]

    def poner_ficha(self, fila, columna, ficha):
        if casillero_libre(self, fila, columna):
            self.casilleros[fila][columna] = ficha
        else:
            raise CasilleroOcupado("Casillero ya ocupado")
           
    def obtener_casillero(self, fil, col):
        return self.casilleros[fil][col]
    
    def __str__(self):
        resultado = ""
        for i in range(3):
            resultado += " | ".join(self.casilleros[i]) + "\n"
            if i < 2:
                resultado += "-" * 9 + "\n"
        return resultado