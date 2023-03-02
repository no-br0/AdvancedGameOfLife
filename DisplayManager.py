import pygame
from LifeManager import calc

dead_color = (0,0,0,255)

class DisplayManager():
    def __init__(self, cell_size, cols, rows):
        self._cell_size = cell_size
        self._cols = cols
        self._rows = rows
        self._width = cols * cell_size
        self._height = rows * cell_size

        self._grid = []
        self._screen = pygame.display.set_mode((self._width, self._height))
        self.create_grid()

    def create_grid(self):
        if len(self._grid) > 0:
            self._grid.clear()

        for row in range(self._rows):
            for col in range(self._cols):
                x = col * self._cell_size
                y = row * self._cell_size
                color = pygame.Color(dead_color)
                rect = pygame.Rect(x,y, self._cell_size, self._cell_size)
                self._grid.append(rect)
                pygame.draw.rect(self._screen, color, rect)

    def reset_grid(self):
        for row in range(self._rows):
            for col in range(self._cols):
                color = pygame.Color(dead_color)
                self.set_color(col, row, color)

    def clear_grid(self):
        self._grid.clear()

    def set_color(self, col, row, color):
        num = calc(self._cols, col, row)
        pygame.draw.rect(self._screen, color, self._grid[num])

    def get_color(self, col, row):
        num = calc(self._cols, col, row)
        return self._screen.get_at((self._grid[num][0], self._grid[num][1]))

if __name__ == '__main__':
    pygame.init()
    display = DisplayManager(10,3,3)
    running = True
    clock = pygame.time.Clock()
    print(display.get_color(0,0))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        pygame.display.update()
        clock.tick(60)
