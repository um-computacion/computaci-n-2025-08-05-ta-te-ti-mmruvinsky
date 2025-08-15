import unittest
from src.tablero import Tablero
from src.tateti import Tateti
from src.excepciones import PosicionInvalida, CasilleroOcupado


class TestTablero(unittest.TestCase):
    
    def setUp(self):
        self.tablero = Tablero()
    
    def test_tablero_vacio(self):
        self.assertEqual(self.tablero.obtener_casillero(0, 0), ' ')
        self.assertEqual(self.tablero.obtener_casillero(1, 1), ' ')
        self.assertEqual(self.tablero.obtener_casillero(2, 2), ' ')
    
    def test_poner_ficha(self):
        self.tablero.poner_ficha(1, 1, 'X')
        self.assertEqual(self.tablero.obtener_casillero(1, 1), 'X')
    
    def test_posicion_invalida(self):
        with self.assertRaises(PosicionInvalida):
            self.tablero.poner_ficha(-1, 0, 'X')
        with self.assertRaises(PosicionInvalida):
            self.tablero.poner_ficha(3, 0, 'X')
        with self.assertRaises(PosicionInvalida):
            self.tablero.poner_ficha(400, 200, 'X')
        with self.assertRaises(PosicionInvalida):
            self.tablero.poner_ficha(0, -1, 'X')
        with self.assertRaises(PosicionInvalida):
            self.tablero.poner_ficha(0, 3, 'X')
    
    def test_casillero_ocupado(self):
        self.tablero.poner_ficha(1, 1, 'X')
        with self.assertRaises(CasilleroOcupado):
            self.tablero.poner_ficha(1, 1, 'O')

    def test_str(self):
        tablero = Tablero()
        tablero.casilleros = [
            ["X", "O", " "],
            [" ", "X", "O"],
            ["O", " ", "X"]
        ]

        esperado = (
            "X | O |  \n"
            "---------\n"
            "  | X | O\n"
            "---------\n"
            "O |   | X\n"
        )

        self.assertEqual(str(tablero), esperado)

if __name__ == '__main__':
    unittest.main(verbosity=2)