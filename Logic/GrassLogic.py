from calc import calc
from Pos import Pos
import random
from LogicActions import *
from Life.Mushroom import Mushroom
from Life.Grass import Grass
from Life.Rabbit import Rabbit
import Utils

def GrassLogic(life, neigh_count, availCells):
        
    for row in range(life.row-1, life.row+2):
        for col in range(life.col-1, life.col+2):
            if row == life.row and col == life.col:
                neigh_count.EmptyNeigh += 0
            else:
                num = calc(col, row)
                if Utils._life.is_empty(num):
                    neigh_count.EmptyNeigh += 1
                else:
                    if Utils._life.grid[num].name == 'Mushroom':
                        neigh_count.MushroomNeigh += 1
                        availCells.append(Pos(col,row))

                    elif Utils._life.grid[num].name == 'Grass':
                        neigh_count.GrassNeigh += 1

    if neigh_count.EmptyNeigh >= 6:
        remove_life(life)

    if neigh_count.MushroomNeigh == 3:
        if len(availCells) > 0:
            relative_target = availCells[random.randint(0, len(availCells)-1)]
            remove_life(Utils._life.grid[calc(relative_target.col, relative_target.row)])
            spawn_life(Grass(relative_target))


    if neigh_count.GrassNeigh <= 2 and neigh_count.MushroomNeigh == 0:
        remove_life(life)
    elif neigh_count.MushroomNeigh > 2:
        remove_life(life)


