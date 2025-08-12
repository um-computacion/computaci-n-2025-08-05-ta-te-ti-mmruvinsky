import unittest
from src.tablero import Tablero
from src.tateti import Tateti
from src.excepciones import PosicionInvalida, CasilleroOcupado

class TestJuegoCompleto(unittest.TestCase):
    
    def test_juego_basico(self):
        juego = Tateti()
        
        # X juega en centro
        juego.ocupar_un_casillero(1, 1)
        self.assertEqual(juego.tablero.obtener_casillero(1, 1), 'X')
        self.assertEqual(juego.turno, 'O')
        
        # O juega en esquina
        juego.ocupar_un_casillero(0, 0)
        self.assertEqual(juego.tablero.obtener_casillero(0, 0), 'O')
        self.assertEqual(juego.turno, 'X')

if __name__ == '__main__':
    unittest.main(verbosity=2)