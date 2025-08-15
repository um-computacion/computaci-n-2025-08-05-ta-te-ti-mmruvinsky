
import unittest, json
from pathlib import Path
from tempfile import TemporaryDirectory
import src.puntajes as puntajes

class TestPuntajes(unittest.TestCase):
    def test_cargar_devuelve_defaults_si_no_existe(self):
        with TemporaryDirectory() as td:
            puntajes._ARCHIVO_PUNTAJE = Path(td) / "scores.json"
            self.assertEqual(puntajes.cargar_puntajes(), {"X":0,"O":0,"E":0})

    def test_cargar_ok_con_archivo_valido(self):
        with TemporaryDirectory() as td:
            puntajes._ARCHIVO_PUNTAJE = Path(td) / "scores.json"
            puntajes._ARCHIVO_PUNTAJE.write_text(json.dumps({"X":2,"O":1,"E":3}), encoding="utf-8")
            self.assertEqual(puntajes.cargar_puntajes(), {"X":2,"O":1,"E":3})

    def test_cargar_json_corrupto_usa_defaults(self):
        with TemporaryDirectory() as td:
            puntajes._ARCHIVO_PUNTAJE = Path(td) / "scores.json"
            puntajes._ARCHIVO_PUNTAJE.write_text("{no-json}", encoding="utf-8")
            self.assertEqual(puntajes.cargar_puntajes(), {"X":0,"O":0,"E":0})

    def test_guardar_normalización(self):
        with TemporaryDirectory() as td:
            puntajes._ARCHIVO_PUNTAJE = Path(td) / "scores.json"
            puntajes.guardar_puntajes({"X":"5","O":2})  
            data = json.loads(puntajes._ARCHIVO_PUNTAJE.read_text(encoding="utf-8"))
            self.assertEqual(data, {"X":5,"O":2,"E":0})

if __name__ == "__main__":
    unittest.main()
