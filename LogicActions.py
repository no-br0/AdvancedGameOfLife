from Utils import _life, _display
from calc import calc


def display_life():
    global _display
    global _life
    for life in _life.life:
        _display.set_color(life.col, life.row, life.color)

def update_display():
    global _display
    _display.reset_grid()
    display_life()

def spawn_life(life):
    global _life
    if _life.is_empty(calc(life.col, life.row)):
        _life.add_life(life)
        #print("life spawned.")

def remove_life(life):
    global _life
    if _life.is_empty(calc(life.col, life.row)) == False:
        _life.remove_life(life)
        #print('life Removed')