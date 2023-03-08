import pygame
import random
from Life.Mushroom import Mushroom
from Pos import Pos
from Utils import _life, _display
from Variables import FPS
import threading
from NeighCount import NeighCount
from LogicActions import *
from Logic.MushroomLogic import MushroomLogic
from Logic.GrassLogic import GrassLogic



def next_epoch():
    global _display
    global _life

    if len(_life.life) == 0:
        col = random.randint(0, _life._cols-1)
        row = random.randint(0, _life._rows-1)
        spawn_life(Mushroom(Pos(col,row)))
    else:
        for life in _life.life:

            relative_target = None
            availCells = []
            neigh_count = NeighCount()
            if MushroomLogic(life, neigh_count, availCells):
                continue
            elif GrassLogic(life, neigh_count, availCells):
                continue
            
            # END GRASS
                    

    #print("next_epoch: Finished")
    _life.update_lists()
    update_display()


class NextEpochThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self.running = False
        self.started = False

    def run(self):
        self.running = True
        next_epoch()
        pygame.display.update()
        #print('Display: Updated')
        self.running = False


def Reset():
    _life.Reset()
    _display.reset_grid()
    




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

    
    next_epoch_thread = NextEpochThread()
    if not next_epoch_thread.running and simulating:
        next_epoch_thread.start()

    #if simulating:
    #    print(f"Number of active threads: {threading.active_count()}")

    #pygame.display.update()
    clock.tick(FPS)