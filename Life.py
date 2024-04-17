# # Симулятор клеточных организмов
# import pygame
# from pygame.locals import *

# class LifeBoard:
#     """
#     Класс для создания и управления игровой доской жизни.
#     """

#     def __init__(self, width: int = 640, height: int = 480, cell_size: int = 10, speed: int = 10) -> None:
#         """
#         Инициализация параметров игровой доски.
#         """
#         self.width = width
#         self.height = height
#         self.screen_size = width, height
#         self.cell_size = cell_size
#         self.screen = pygame.display.set_mode(self.screen_size)
#         self.cell_width = self.width // self.cell_size
#         self.cell_height = self.height // self.cell_size
#         self.speed = speed

#     def draw_lines(self) -> None:
#         """
#         Отрисовка сетки на экране.
#         """
#         for x in range(0, self.width, self.cell_size):
#             pygame.draw.line(self.screen, pygame.Color('black'), (x, 0), (x, self.height))
#         for y in range(0, self.height, self.cell_size):
#             pygame.draw.line(self.screen, pygame.Color('black'), (0, y), (self.width, y))

#     def run(self) -> None:
#         """
#         Запуск игры.
#         """
#         pygame.init()
#         clock = pygame.time.Clock()
#         pygame.display.set_caption('Game of Life')
#         self.screen.fill(pygame.Color('green'))
#         running = True
#         while running:
#             for event in pygame.event.get():
#                 if event.type == QUIT:
#                     running = False
#             self.draw_lines()
#             self.draw_grid()
#             pygame.display.flip()
#             clock.tick(self.speed)
#             self.create_grid()
#         pygame.quit()

#     def drow_grid(self):
#         """
#         Создание сетки для игры.
#         """
#         grid = [[0 for _ in range(self.cell_width)] for _ in range(self.cell_height)]
#         return grid

# if __name__ == '__main':
#     game = LifeBoard(640, 480, 10, 10)
#     game.run()


import pygame
from pygame.locals import *


class GameOfLife:

    def __init__(self, width: int=640, height: int=480, cell_size: int=10, speed: int=10) -> None:
        self.width = width
        self.height = height
        self.cell_size = cell_size

        # Устанавливаем размер окна
        self.screen_size = width, height
        # Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)

        # Вычисляем количество ячеек по вертикали и горизонтали
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

        # Скорость протекания игры
        self.speed = speed


    def draw_lines(self) -> None:
        # @see: http://www.pygame.org/docs/ref/draw.html#pygame.draw.line
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'), 
                (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'), 
                (0, y), (self.width, y))


    def run(self) -> None:
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
        pygame.quit()


if __name__ == '__main__':
    game = GameOfLife(640, 480, 10)
    game.run()