from calc import calc
from Pos import Pos
import random
from LogicActions import remove_life, spawn_life
from Life.Mushroom import Mushroom
from Life.Grass import Grass
from Life.Rabbit import Rabbit
from Utils import _life

def MushroomLogic(life, neigh_count, availCells):
    if life.name == 'Mushroom':
        for row in range(life.row-1, life.row+2):
            for col in range(life.col-1, life.col+2):
                if row == life.row and col == life.col:
                    neigh_count.EmptyNeigh += 0
                else:
                    num = calc(col, row)
                    if _life.is_empty(num):
                        neigh_count.EmptyNeigh += 1
                        availCells.append(Pos(col,row))
                    else:
                        if _life.grid[num] != None:
                            if _life.grid[num].name == 'Mushroom':
                                neigh_count.MushroomNeigh += 1
                            elif _life.grid[num].name == 'Grass':
                                neigh_count.GrassNeigh += 1
                            elif _life.grid[num].name == 'Rabbit':
                                neigh_count.RabbitNeigh += 1

        if neigh_count.EmptyNeigh >= 1:
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
                    remove_life(_life.grid[calc(relative_target.col, relative_target.row)])
                    spawn_life(Mushroom(relative_target))
                    target_achieved = True
                
        if neigh_count.MushroomNeigh >= 2:
            remove_life(life)
                
        if neigh_count.MushroomNeigh >= 5:
            remove_life(life)
            spawn_life(Grass(Pos(life.col,life.row)))

        #if MushroomNeigh == 2:
        #    remove_life(life)
        #    spawn_life(Rabbit(Pos(life.col,life.row)))

        return True
    else:
        return False