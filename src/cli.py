from .tateti import Tateti
from .excepciones import PosicionInvalida, CasilleroOcupado

def main():
    print("¡Bienvenido al juego de Tateti!")
    juego = Tateti()

    while True:
        print("\nTablero actual:")
        print(juego.tablero)
        print(f"Turno de: {juego.turno}")
        
        try:
            fil = int(input("Ingrese la fila (1-3): ")) - 1
            col = int(input("Ingrese la columna (1-3): ")) - 1
            
            juego.ocupar_un_casillero(fil, col)
            
            # Verificar si hay ganador
            ganador = juego.hay_ganador()
            if ganador:
                print("\nTablero final:")
                print(juego.tablero)
                print(f"¡Felicitaciones! Ganó el jugador {ganador}")
                break
            
            # Verificar empate
            if juego.tablero_lleno():
                print("\nTablero final:")
                print(juego.tablero)
                print("¡Es un empate!")
                break
                
        except (PosicionInvalida, CasilleroOcupado) as e:
            print(f"Error: {e}")
        except ValueError:
            print("Error: Debe ingresar números válidos.")
        except Exception as e:
            print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()