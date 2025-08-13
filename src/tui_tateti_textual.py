"""
TUI para Ta‑Te‑Ti usando Textual
Requisitos: `pip install textual`
Ejecución desde la raíz del repo:  

`python3 -m src.tui_tateti_textual`

Controles:
- Flechas: mover el foco entre celdas
- Enter/Espacio: colocar la marca en la celda
- R: reiniciar
- Q: salir
"""
from __future__ import annotations
from typing import List, Optional, Tuple
from textual.app import App, ComposeResult
from textual.containers import Vertical, Grid
from textual.reactive import reactive
from textual.widgets import Button, Static
from textual.screen import ModalScreen
from .tateti import Tateti 
from .tablero import Tablero
from pyfiglet import figlet_format
from rich.text import Text

Coord = Tuple[int, int]  

LINES: list[list[Coord]] = [
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)],
]

class GameAdapter:
    def __init__(self) -> None:
        self.game = Tateti()

    def board_matrix(self) -> list[list[str]]:
        return self.game.tablero.casilleros 

    def current_turn(self) -> str:
        return self.game.turno
    
    def play(self, r: int, c: int) -> None:
        self.game.ocupar_un_casillero(r, c)

    def winning_cells(self) -> list[Coord] | None:
        m = self.board_matrix()
        for line in LINES:
            (r1, c1), (r2, c2), (r3, c3) = line
            v = m[r1][c1]
            if v != ' ' and v == m[r2][c2] == m[r3][c3]:
                return line
        return None

    def is_full(self) -> bool:
        return self.game.tablero_lleno()
    
    def reset(self) -> None:
        self.game.reiniciar()

    def get_scores(self) -> dict[str, int]:
        return self.game.get_puntajes()

    def reset_scores(self) -> None:
        self.game.resetear_puntajes()


class Cell(Button):
    def __init__(self, r: int, c: int, label: str = "") -> None:
        super().__init__(label or " ", id=f"cell-{r}-{c}")
        self.r, self.c = r, c

class EndScreen(ModalScreen[None]):
    def __init__(self, mensaje: str) -> None:
        super().__init__()
        self.mensaje = mensaje
            
    def compose(self):
        yield Vertical(
            Static(self.mensaje, id="end-msg"),
            Button("Reiniciar [R]", id="restart", classes="modal-btn"),
            Button("Salir [Q]", id="quit", classes="modal-btn"),
            id="end-box"
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "restart":
            self.app.action_restart_game()
        else:
            self.app.exit()
        self.dismiss()


class TTTApp(App):
    CSS = (
        """
        Screen {
            align: center middle;
            background: black;
        }

        .wrap { width: 56; }

        #title {
            height: auto;
            content-align: center middle;
            color: magenta;
            background: black;
            text-style: bold reverse;
            border: heavy deeppink;
        }
        #subtitle {
            height: 3;
            content-align: center middle;
            color: cyan;
            background: black;
            text-style: bold reverse;
            border: heavy cyan;
        }

        #status {
            height: 3;
            content-align: center middle;
            color: cyan;
            text-style: bold;
            border: heavy cyan;
            background: #101010;
        }

        Grid#board {
            grid-size: 3 3;
            grid-gutter: 2 1;
            padding: 2;
            background: #111111;
            border: double magenta;   /* marco exterior estilo arcade */
        }

        Button {
            height: 5;
            width: 14;
            content-align: center middle;
            color: white;
            background: #151515;
            border: round #444444;
        }

        Button:focus {
            border: heavy magenta;
            background: #1e1e1e;
        }
        Button:hover {
            border: heavy cyan;
        }

        Button.-x { color: deeppink; text-style: bold reverse; }
        Button.-o { color: cyan;     text-style: bold reverse; }

        Button.-last { background: yellow; color: black; text-style: bold; }
        Button.-win  { border: heavy lime; }

        #end-box {
            align: center middle;
            width: auto;
            height: auto;
            border: heavy magenta;
            background: black;
            padding: 1;
        }

        #end-box .modal-btn {
            height: auto;
            width: 22;
            align: center middle;
            content-align: center middle;
            color: cyan;
            background: #111;
            border: round #333;      
        }

        #end-box .modal-btn:focus {
            border: none;
            background: #151515;
        }

        Button.focus-x {
            border: heavy magenta; /* Rosado */
        }

        Button.focus-o {
            border: heavy cyan; /* Celeste */
        }

        #score {
            height: 3;
            content-align: center middle;
            color: white;
            border: heavy #333333;
            background: #101010;
        }




        """
    )

    adapter: GameAdapter
    turn: str = reactive("X")
    last_move: Coord = reactive((-1, -1))
    win_cells: Optional[list[Coord]] = reactive(None)

    def _maybe_show_end(self) -> None:
        if self.win_cells:
            r, c = self.win_cells[0]
            winner = self.adapter.board_matrix()[r][c]
            self.push_screen(EndScreen(f"¡Ganó {winner}!"))
        elif self.adapter.is_full():
            self.push_screen(EndScreen("¡Empate!"))

    def _update_focus_style(self) -> None:
        for r in range(3):
            for c in range(3):
                cell = self.query_one(f"#cell-{r}-{c}", Cell)
                cell.remove_class("-focus-x", "-focus-o")

        focused = self.focused
        if isinstance(focused, Cell):
            if (self.turn or self.adapter.current_turn()) == "X":
                focused.add_class("-focus-x")
            else:
                focused.add_class("-focus-o")



    def compose(self) -> ComposeResult:
        ascii_title = figlet_format("TA-TE-TI", font="slant")  # Podés probar "banner", "block", "slant", etc.
        yield Static(Text(ascii_title, style="bold magenta"), id="title", classes="wrap")
        yield Static("(Flechas + Enter)", id="subtitle", classes="wrap")
        yield Static("Turno ---> X", id="status", classes="wrap")
        yield Grid(id="board", classes="wrap")
        yield Static("Marcador  X:0  O:0  E:0", id="score", classes="wrap")
        yield Static("Atajos: R = reiniciar, Q = salir", id="footer", classes="wrap")


    def on_mount(self) -> None:
        self.adapter = GameAdapter()
        self.turn = self.adapter.current_turn()
        grid = self.query_one("#board", Grid)
        for r in range(3):
            for c in range(3):
                grid.mount(Cell(r, c))
        self.query_one("#cell-1-1", Cell).focus()
        self._refresh()
        self._refresh_score()  
        self._update_focus_style()

    def action_restart_game(self) -> None:
        self.adapter.reset()
        self.last_move = (-1, -1)
        self.win_cells = None
        self.turn = self.adapter.current_turn()
        # foco al centro y refresco
        self.query_one("#cell-1-1", Cell).focus()
        self._refresh()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if isinstance(event.button, Cell):
            self._play_at(event.button.r, event.button.c)

    def on_key(self, event) -> None:
        key = event.key.lower()
        focused = self.focused  

        # cerrar/salir y reiniciar
        if key == "q":
            self.exit()
        if key == "r":
            self.adapter.reset()
            self.last_move = (-1, -1)
            self.win_cells = None
            self.turn = self.adapter.current_turn() or "X"
            self.query_one("#cell-1-1", Cell).focus()
            self._refresh()
            return

        # ignorar si no hay celda enfocada
        if not isinstance(focused, Cell):
            return

        r, c = focused.r, focused.c

        # mover foco con flechas
        if key == "left":
            c = max(0, c - 1)
        elif key == "right":
            c = min(2, c + 1)
        elif key == "up":
            r = max(0, r - 1)
        elif key == "down":
            r = min(2, r + 1)
        elif key in ("enter", "space"):
            # simular click en la celda enfocada
            self._play_at(focused.r, focused.c)
            return
        else:
            return 

        self.query_one(f"#cell-{r}-{c}", Cell).focus()
        self._update_focus_style()

    def _refresh_score(self) -> None:
        sc = self.adapter.get_scores()  
        self.query_one("#score", Static).update(
            f"Marcador  X:{sc['X']}  O:{sc['O']}  E:{sc['E']}"
        )


    def _refresh(self) -> None:
        status = self.query_one("#status", Static)
        board = self.adapter.board_matrix()
        if self.win_cells:
            # marca ganadora leyendo una de las celdas de la línea
            r, c = self.win_cells[0]
            status.update(f"Ganó: {board[r][c]}")
        elif self.adapter.is_full():
            status.update("Empate")
        else:
            status.update(f"Turno: {self.turn}")
        # pintar celdas
        for r in range(3):
            for c in range(3):
                cell: Cell = self.query_one(f"#cell-{r}-{c}")
                val = board[r][c] or " "
                cell.label = val
                cell.remove_class("-x", "-o", "-last", "-win")
                if val == "X":
                    cell.add_class("-x")
                elif val == "O":
                    cell.add_class("-o")
                if (r, c) == self.last_move:
                    cell.add_class("-last")
                if self.win_cells and (r, c) in self.win_cells:
                    cell.add_class("-win")

    def _play_at(self, r: int, c: int) -> None:
            
        if self.win_cells:
                return
        board = self.adapter.board_matrix()
        if board[r][c] != " ":
            return

        # ejecutar jugada
        self.adapter.play(r, c)
        self.last_move = (r, c)
        self.win_cells = self.adapter.winning_cells()

        self._refresh()
        self._refresh_score()
        self._update_focus_style()
        self._maybe_show_end()

if __name__ == "__main__":
    TTTApp().run()
