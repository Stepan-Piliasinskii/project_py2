import pygame
import sys
import random


CELL = 20            # pixel size of a cell
COLS = 30            # number of cells horizontally
ROWS = 20            # number of cells vertically
WIDTH = CELL * COLS
HEIGHT = CELL * ROWS
FPS = 10             # game speed (increase to make snake faster)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (50, 200, 50)
RED = (200, 50, 50)
GRAY = (40, 40, 40)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))


def random_food_position():
    pass


if __name__ == "__main__":
    main()

