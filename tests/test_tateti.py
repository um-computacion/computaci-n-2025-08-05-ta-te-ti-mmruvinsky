import unittest
from src.tablero import Tablero
from src.tateti import Tateti

class TestTateti(unittest.TestCase):
    
    def setUp(self):
        self.juego = Tateti()
    
    def test_juego_nuevo(self):
        self.assertEqual(self.juego.turno, 'X')
    
    def test_cambio_turno(self):
        self.juego.ocupar_un_casillero(0, 0)
        self.assertEqual(self.juego.turno, 'O')
        
        self.juego.ocupar_un_casillero(0, 1)
        self.assertEqual(self.juego.turno, 'X')
    
    def test_ganador_fila(self):
        self.juego.tablero.casilleros[0] = ['X', 'X', 'X']
        self.assertEqual(self.juego.hay_ganador(), 'X')
    
    def test_ganador_columna(self):
        self.juego.tablero.casilleros[0][0] = 'O'
        self.juego.tablero.casilleros[1][0] = 'O'
        self.juego.tablero.casilleros[2][0] = 'O'
        self.assertEqual(self.juego.hay_ganador(), 'O')
    
    def test_ganador_diagonal(self):
        self.juego.tablero.casilleros[0][0] = 'X'
        self.juego.tablero.casilleros[1][1] = 'X'
        self.juego.tablero.casilleros[2][2] = 'X'
        self.assertEqual(self.juego.hay_ganador(), 'X')
    
    def test_sin_ganador(self):
        self.assertIsNone(self.juego.hay_ganador())
    
    def test_tablero_no_lleno(self):
        self.assertFalse(self.juego.tablero_lleno())

if __name__ == '__main__':
    unittest.main(verbosity=2)