from .tablero import Tablero

def es_posicion_valida(fil, col):
    return 0 <= fil <= 2 and 0 <= col <= 2

def casillero_libre(tablero, fil, col):
    return tablero.obtener_casillero(fil, col) == ' '