Ta-Te-Ti (CLI + TUI con Textual)

    Implementación de Ta-Te-Ti con motor de juego puro (tateti.py + tablero.py), una interfaz TUI retro con [Textual], y un CLI simple para entornos sin interfaz.

Requisitos:

    Python 3.10+

    (Opcional) virtualenv/venv para aislar dependencias

Estructura del proyecto:

    src/
    __init__.py
    tateti.py
    tablero.py
    tui_tateti_textual.py   
    cli.py                   
    tests/  
    test_juego_completo.py
    test_tateti.py
    test_tablero.py
    __init__.py                 
    requirements.txt
    .gitignore

Asegurate de que exista src/__init__.py para que src sea un paquete y se pueda ejecutar con -m.



Instalación:

1) Clonar:

    git clone <URL-DEL-REPO>
    cd <carpeta-del-repo>


2) (Recomendado) Crear y activar un entorno virtual:

    Linux / macOS:
        python -m venv .venv
        source .venv/bin/activate
        Windows (PowerShell)

    powershell:
        python -m venv .venv
        .venv\Scripts\Activate.ps1


3) Instalar dependencias:

    pip install -r requirements.txt



Dependencias clave:

    textual (TUI)
    pyfiglet (título ASCII retro para el TUI)



Ejecución:


    TUI:

    --> Siempre ejecutá desde la raíz del repo (la carpeta que contiene src/).

    --> python3 -m src.tui_tateti_textual

        Controles:

            Flechas: mover el foco
            Enter/Espacio: jugar en la celda
            R: reiniciar
            Q: salir



    CLI: 

    --> Siempre ejecutá desde la raíz del repo (la carpeta que contiene src/).

    --> python3 -m src.cli
