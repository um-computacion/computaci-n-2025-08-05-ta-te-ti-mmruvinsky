from Tateti import Tateti

def main():

    print("Bienvenido al juego de Tateti!")
    juego = Tateti()

    while True:
        print("Tablero actual:")
        print(juego.tablero)
        print(f"Turno de {juego.turno}")
        fil = (int(input("Ingrese la fila (0-2): ")))
        col = (int(input("Ingrese la columna (0-2): ")))
        try:
            juego.ocupar_un_casillero(fil, col)
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main() 