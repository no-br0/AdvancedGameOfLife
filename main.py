from DisplayManager import DisplayManager
from LifeManager import LifeManager
import pygame
import random
from Life.Mushroom import Mushroom
from Life.Grass import Grass
from Life.Rabbit import Rabbit
from Pos import Pos
from Utils import *

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
        spawn_life(Mushroom(Pos(col,row)))
    else:
        for life in _life.life:

            availCells = []
            EmptyNeigh = 0
            MushroomNeigh = 0
            GrassNeigh = 0
            RabbitNeigh = 0


            

            if life.name == 'Mushroom':
                for row in range(life.row-1, life.row+2):
                    for col in range(life.col-1, life.col+2):
                        if row == life.row and col == life.col:
                            EmptyNeigh += 0
                        else:
                            num = calc(col, row)
                            if _life.is_empty(num):
                                EmptyNeigh += 1
                                availCells.append(Pos(col,row))
                            else:
                                if _life.grid[num].name == 'Mushroom':
                                    MushroomNeigh += 1
                                elif _life.grid[num].name == 'Grass':
                                    GrassNeigh += 1

                if EmptyNeigh >= 1:
                    relative_target = None
                    target_achieved = False
                    while target_achieved == False:
                        #while relative_target == None or relative_target == 4:
                        #    relative_target = random.randint(0,8)
                        if len(availCells) > 0:
                            relative_target = availCells[random.randint(0, len(availCells)-1)]
                        
                        if _life.is_empty(calc(relative_target.col, relative_target.row)):
                            spawn_life(Mushroom(relative_target))
                            target_achieved = True
                        else:
                            relative_target = None
                
                if MushroomNeigh >= 1:
                    remove_life(life)
                
                if MushroomNeigh >= 5:
                    remove_life(life)
                    spawn_life(Grass(Pos(life.col,life.row)))

                #if MushroomNeigh == 2:
                #    remove_life(life)
                #    spawn_life(Rabbit(Pos(life.col,life.row)))
            

            elif life.name == 'Grass':
                if EmptyNeigh >= 5:
                    relative_target = None
                    target_achieved = False
                    while target_achieved == False:
                        

                        if _life.is_empty(calc(col,row)):
                            spawn_life(Grass(relative_target))
                            target_achieved = True
                        else:
                            relative_target = None

                if GrassNeigh >= 4:
                    remove_life(life)


                    


    _life.update_lists()
    update_display()





def Reset():
    _life.Reset()
    _display.reset_grid()
    



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
                Reset()

            


        if simulating:
            next_epoch()

        pygame.display.update()
        clock.tick(FPS)