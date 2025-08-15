import json
from pathlib import Path
from .tablero import Tablero
from .excepciones import ArchivoPuntajesInexistente
from typing import Dict

_BASE_DIR = Path(__file__).resolve().parent
_ARCHIVO_PUNTAJE = _BASE_DIR / "scores.json"
_PUNTAJES_DEFAULT: Dict[str, int] = {"X": 0, "O": 0, "E": 0}

def cargar_puntajes() -> Dict[str, int]:
    """Lee scores.json si existe; si no o si está corrupto, devuelve los defaults."""
    try:
        if not _ARCHIVO_PUNTAJE.exists():
            return _PUNTAJES_DEFAULT.copy()
        data = json.loads(_ARCHIVO_PUNTAJE.read_text(encoding="utf-8"))
        # Normalizá: solo claves esperadas y a int
        return {k: int(data.get(k, 0)) for k in _PUNTAJES_DEFAULT}
    except (json.JSONDecodeError, ValueError):
        return _PUNTAJES_DEFAULT.copy()

def guardar_puntajes(scores: Dict[str, int]) -> None:
    """Guarda los puntajes normalizados en scores.json."""
    safe = {k: int(scores.get(k, 0)) for k in _PUNTAJES_DEFAULT}
    _ARCHIVO_PUNTAJE.write_text(json.dumps(safe, ensure_ascii=False, indent=2), encoding="utf-8")
