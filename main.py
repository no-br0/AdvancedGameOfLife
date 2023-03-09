import pygame
import random
from Life.Mushroom import Mushroom
from Pos import Pos
import Utils
from Variables import FPS, COLS, ROWS
import threading
from NeighCount import NeighCount
from LogicActions import *
from Logic.MushroomLogic import MushroomLogic
from Logic.GrassLogic import GrassLogic



def next_epoch():
    if len(Utils._life.life) == 0:
        col = random.randint(0, COLS-1)
        row = random.randint(0, ROWS-1)
        spawn_life(Mushroom(Pos(col,row)))
    else:
        for life in Utils._life.life:

            availCells = []
            neigh_count = NeighCount()
            if life.name == 'Mushroom':
                MushroomLogic(life, neigh_count, availCells)
            elif life.name == 'Grass':
                GrassLogic(life, neigh_count, availCells)
            
                    

    Utils._life.update_lists()


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
    Utils._life.Reset()
    Utils._display.reset_grid()
    




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
                print('Pause')
            else:
                simulating = True
                print('Play')
        if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
            Reset()

    
    next_epoch_thread = NextEpochThread()
    if not next_epoch_thread.running and simulating:
        next_epoch_thread.start()

    #if simulating:
    #    print(f"Number of active threads: {threading.active_count()}")

    #pygame.display.update()
    clock.tick(FPS)