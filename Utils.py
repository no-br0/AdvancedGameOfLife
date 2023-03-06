from DisplayManager import DisplayManager
from LifeManager import LifeManager
from Variables import COLS, ROWS, CELL_SIZE

_display = DisplayManager(CELL_SIZE, COLS, ROWS)
_life = LifeManager(COLS, ROWS)