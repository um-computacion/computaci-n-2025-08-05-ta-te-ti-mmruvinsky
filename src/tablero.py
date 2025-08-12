from excepciones import PosicionInvalida, CasilleroOcupado

class Tablero:
    """Representa el tablero del juego"""
    def __init__(self):
        self.casilleros = [[' ' for _ in range(3)] for _ in range(3)]

    def es_posicion_valida(self, fil, col):
        return 0 <= fil <= 2 and 0 <= col <= 2

    def casillero_libre(self, fil, col):
        return self.casilleros[fil][col] == ' '

    def poner_ficha(self, fila, columna, ficha):
        if not self.es_posicion_valida(fila, columna):
            raise PosicionInvalida("La posición no es válida.")
        if not self.casillero_libre(fila, columna):
            raise CasilleroOcupado("El casillero ya está ocupado.")
        self.casilleros[fila][columna] = ficha
           
    def obtener_casillero(self, fil, col):
        return self.casilleros[fil][col]
    
    def __str__(self):
        resultado = ""
        for i in range(3):
            resultado += " | ".join(self.casilleros[i]) + "\n"
            if i < 2:
                resultado += "-" * 9 + "\n"
        return resultado