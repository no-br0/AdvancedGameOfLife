import Utils
from calc import calc


#def display_life():
#    for life in Utils._life.life:
#        Utils._display.set_color(life.col, life.row, life.color)

#def update_display():
#    Utils._display.reset_grid()
#    display_life()

def spawn_life(life):
    if Utils._life.is_empty(calc(life.col, life.row)):
        Utils._life.add_life(life)
        #print("life spawned.")

def remove_life(life):
    if Utils._life.is_empty(calc(life.col, life.row)) == False:
        Utils._life.remove_life(life)
        #print('life Removed')