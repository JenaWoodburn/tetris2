# Imports
import pygame
import random
import sys

pygame.init()

# Constant Variables
WIDTH, HEIGHT = (300, 500)
FPS = 35

CELL = 20
ROWS = (HEIGHT - 120) // CELL
COLS = WIDTH // CELL

# Game settings
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Tetris")

# Colours
BLACK = (0,0,0,)
WHITE = (255, 255, 255)
BG_COLOUR = (31, 25, 76)
GRID = (31, 25,132)
WIN = (50, 230, 50)
LOSE = (252, 91, 122)

# Load / Store images
ASSETS = {
    1: pygame.image.load("Assets/1.png"),
    2: pygame.image.load("Assets/2.png"),
    3: pygame.image.load("Assets/3.png"),
    4: pygame.image.load("Assets/4.png")
}

# Fonts
font1 = pygame.font.SysFont("verdana", 50)
font2 = pygame.font.SysFont("verdana", 15)


# Shape Class
    # Constructor

    # Image - choose correct images

    # Rotate


# Game Class
    # Constructor

    # Make grid

    # Make new shape


# Main game loop
def main():
    run = True
    while run:
        SCREEN.fill(BG_COLOUR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()



        pygame.display.update()
        clock.tick(FPS)


if __name__ == '__main__':
    main()