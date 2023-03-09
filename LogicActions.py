import Utils
from calc import calc


def spawn_life(life):
    if Utils._life.is_empty(calc(life.col, life.row)):
        Utils._life.add_life(life)
        print("life spawned.")

def remove_life(life):
    if not Utils._life.is_empty(calc(life.col, life.row)):
        Utils._life.remove_life(life)
        print('life Removed')