from DisplayManager import DisplayManager
from LifeManager import LifeManager
import pygame
import random
from Life.Mushroom import Mushroom
from Pos import Pos
#from LifeManager import calc
from Utils import *

#FPS = 10

#CELL_SIZE = 4
#COLS = 100
#ROWS = 100

_display = DisplayManager(CELL_SIZE, COLS, ROWS)
_life = LifeManager(COLS, ROWS)

def display_life():
    for life in _life.life:
        _display.set_color(life.col, life.row, life.color)

def update_display():
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


def next_epoch():
    global _display
    global _life

    if len(_life.life) == 0:
        col = random.randint(0, _life._cols-1)
        row = random.randint(0, _life._rows-1)
        #spawn_life(Mushroom(Pos(1,1)))
        spawn_life(Mushroom(Pos(col,row)))
    else:
        for life in _life.life:
            #apply game logic here
            availCells = []
            EmptyNeigh = 0
            MushroomNeigh = 0

            #count neighbours to determine what logic to use
            for row in range(life.row-1, life.row+2):
                for col in range(life.col-1, life.col+2):
                    if row == life.row and col == life.col:
                        #do nothing
                        EmptyNeigh += 0
                    else:
                        num = calc(col, row)
                        if _life.is_empty(num):
                            EmptyNeigh += 1
                            availCells.append(Pos(col,row))
                        else:
                            if _life.grid[num].name == 'Mushroom':
                                MushroomNeigh += 1

            #print(EmptyNeigh)
            #print(MushroomNeigh)
            #check neighbours counts and apply the logic

            if life.name == 'Mushroom':
                #if all neighbours are empty add a single mushroom in a random direction
                if EmptyNeigh >= 5:
                    relative_target = None
                    target_achieved = False
                    while target_achieved == False:
                        while relative_target == None or relative_target == 4:
                            relative_target = random.randint(0,8)
                        #if len(availCells) > 0:
                        #    target_pos = availCells[random.randint(0, len(availCells)-1)]
                        col = (relative_target%3) - 1

                        row = (relative_target//3) - 1


                        col += life.col
                        row += life.row
                        if _life.is_empty(calc(col,row)):
                            spawn_life(Mushroom(Pos(col, row)))
                            target_achieved = True
                        else:
                            relative_target = None
                
                if MushroomNeigh >= 8:
                    remove_life(life)


    _life.update_lists()
    update_display()







if __name__ == '__main__':
    pygame.init()
    running = True
    clock = pygame.time.Clock()
    simulating = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if simulating:
                    simulating = False
                else:
                    simulating = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                print(_life.life)


        if simulating:
            next_epoch()

        pygame.display.update()
        clock.tick(FPS)