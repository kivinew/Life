# Симулятор клеточных организмов
import pygame
from pygame.locals import *

class LifeBoard:
    """
    Класс для создания и управления игровой доской жизни.
    """

    def __init__(self, width: int = 640, height: int = 480, cell_size: int = 10, speed: int = 10) -> None:
        """
        Инициализация параметров игровой доски.
        """
        pygame.init()
        self.width = width
        self.height = height
        self.screen_size = width, height
        self.cell_size = cell_size
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size
        self.screen = pygame.display.set_mode(self.screen_size)
        self.speed = speed
        pygame.display.flip()

    def draw_lines(self) -> None:
        """
        Отрисовка сетки на экране.
        """
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'), (0, y), (self.width, y))
        pygame.display.update()            

    def run(self) -> None:
        """
        Запуск игры.
        """
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('green'))
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            self.draw_lines()
            pygame.display.flip()
            clock.tick(self.speed)
            self.create_grid()
        pygame.quit()

    def create_grid(self):
        """
        Создание сетки для игры.
        """
        grid = [[0 for _ in range(self.cell_width)] for _ in range(self.cell_height)]
        return grid

if __name__ == '__main':
    game = LifeBoard(640, 480, 10, 10)
    game.run()
