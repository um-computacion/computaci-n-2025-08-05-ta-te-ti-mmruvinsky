from tateti import Tateti
from excepciones import PosicionInvalida, CasilleroOcupado
from validadores import es_posicion_valida, casillero_libre

def main():

    print("Bienvenido al juego de Tateti!")
    juego = Tateti()

    while True:

        print("Tablero actual:")
        print(juego.tablero)
        print(f"Turno de {juego.turno}")
        fil = (int(input("Ingrese la fila (1-3): ")))
        col = (int(input("Ingrese la columna (1-3): ")))
        fil = fil - 1
        col = col - 1
        if not es_posicion_valida(fil, col):
            raise PosicionInvalida("La posición no es válida.")
        if not casillero_libre(tablero, fil, col):
            raise CasilleroOcupado("El casillero ya está ocupado.")


        try:
            juego.ocupar_un_casillero(fil, col)
        except ValueError as e:
            print(e)



if __name__ == "__main__":
    main() 