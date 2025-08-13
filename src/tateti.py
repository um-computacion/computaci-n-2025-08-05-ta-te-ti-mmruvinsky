from .tablero import Tablero
from .excepciones import PosicionInvalida, CasilleroOcupado, ArchivoPuntajesInexistente
from pathlib import Path
import json

# Guardamos JSON junto al archivo tateti.py para almacenar puntajes
_BASE_DIR = Path(__file__).resolve().parent
_ARCHIVO_PUNTAJE = _BASE_DIR / "scores.json"
_PUNTAJES_DEFAULT = {"X": 0, "O": 0, "E": 0}

def _cargar_puntajes() -> dict[str, int]:
    try:
        if _ARCHIVO_PUNTAJE.exists():
            data = json.loads(_ARCHIVO_PUNTAJE.read_text(encoding="utf-8"))

            return {k: int(data.get(k, 0)) for k in _PUNTAJES_DEFAULT}
    except ArchivoPuntajesInexistente:
            print(f"Error: El archivo de puntajes no existe.")
    return _PUNTAJES_DEFAULT.copy()


def _guardar_puntajes(scores: dict[str, int]) -> None:
    safe = {k: int(scores.get(k, 0)) for k in _PUNTAJES_DEFAULT}
    _ARCHIVO_PUNTAJE.write_text(json.dumps(safe), encoding="utf-8")


class Tateti:
    def __init__(self) -> None:
        self.turno: str = "X"
        self.tablero: Tablero = Tablero()
        self.puntajes: dict[str, int] = _cargar_puntajes()  

    def ocupar_un_casillero(self, fil: int, col: int) -> None:
        """Coloca la ficha del turno actual y alterna el turno.
        Si la partida termina (victoria/empate), actualiza puntajes y persiste.
        """
        self.tablero.poner_ficha(fil, col, self.turno)
        self._registrar_resultado_si_termina()
        self.turno = "O" if self.turno == "X" else "X"

    def hay_ganador(self) -> str | None:
        """Devuelve 'X' o 'O' si hay ganador; en caso contrario None."""
        t = self.tablero.casilleros

        for i in range(3):
            if t[i][0] == t[i][1] == t[i][2] != " ":
                return t[i][0]
            if t[0][i] == t[1][i] == t[2][i] != " ":
                return t[0][i]

        if t[0][0] == t[1][1] == t[2][2] != " ":
            return t[0][0]
        if t[0][2] == t[1][1] == t[2][0] != " ":
            return t[0][2]
        return None

    def tablero_lleno(self) -> bool:
        """True si no quedan casilleros vacíos (posible empate)."""
        return all(c != " " for fila in self.tablero.casilleros for c in fila)

    def reiniciar(self) -> None:
        """Reinicia tablero y turno (NO toca puntajes)."""
        self.turno = "X"
        for r in range(3):
            for c in range(3):
                self.tablero.casilleros[r][c] = " "

    # Puntajes

    def get_puntajes(self) -> dict[str, int]:
        """Copia de puntajes actuales (X, O, E)."""
        return dict(self.puntajes)

    def resetear_puntajes(self) -> None:
        """Pone el marcador en cero y lo persiste."""
        self.puntajes = _PUNTAJES_DEFAULT.copy()
        _guardar_puntajes(self.puntajes)

    # Internos

    def _registrar_resultado_si_termina(self) -> None:
        """Si hay ganador o empate, incrementa y guarda puntajes."""
        ganador = self.hay_ganador()
        if ganador in ("X", "O"):
            self.puntajes[ganador] = self.puntajes.get(ganador, 0) + 1
            _guardar_puntajes(self.puntajes)
        elif self.tablero_lleno():
            self.puntajes["E"] = self.puntajes.get("E", 0) + 1
            _guardar_puntajes(self.puntajes)