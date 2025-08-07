def es_posicion_valida(fil, col):
    return 0 < fil <= 3 and 0 < col <= 3

def casillero_libre(tablero, fil, col):
    return tablero.obtener_casillero(fil, col) == ' '