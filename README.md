Ta-Te-Ti 

Proyecto en Python que implementa el clásico juego de Ta-Te-Ti (Tres en Línea) en modo consola, siguiendo principios de programación estructurada y modular. Incluye un conjunto de tests automatizados para verificar la correcta funcionalidad de las clases y métodos.
📂 Estructura del proyecto

tateti/
├── src/ → Código fuente del juego
│ ├── init.py
│ ├── cli.py → Interfaz por línea de comandos
│ ├── excepciones.py → Excepciones personalizadas
│ ├── tablero.py → Lógica del tablero
│ ├── tateti.py → Lógica principal del juego
│ └── validadores.py → Funciones de validación
├── tests/ → Tests unitarios
│ ├── init.py
│ ├── test_tablero.py
│ ├── test_tateti.py
│ └── test_juego_completo.py
└── README.md
🚀 Requisitos

    Python 3.10 o superior

    pip para instalar dependencias

🔧 Instalación

    Clonar este repositorio y entrar a la carpeta del proyecto.

    (Opcional) Crear un entorno virtual para aislar las dependencias.

    Instalar las dependencias necesarias como coverage para medir la cobertura de los tests.

▶️ Ejecución del juego

Para jugar desde la consola se ejecuta el archivo cli.py dentro de la carpeta src.
🧪 Ejecutar los tests

El proyecto incluye tests unitarios que validan el correcto funcionamiento de las clases Tablero y Tateti, así como el flujo completo del juego. Pueden ejecutarse con unittest.
